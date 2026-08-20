import os
import json
import hashlib
from datetime import datetime

class ImmutableAuditLedger:
    """
    Maintains a tamper-evident chain of custody using cryptographic hashing (SHA-256).
    Each audit entry links to the hash of the preceding entry.
    """
    def __init__(self, ledger_path="audit/immutable_ledger.json"):
        self.ledger_path = ledger_path
        os.makedirs(os.path.dirname(self.ledger_path), exist_ok=True)
        self.chain = self._load_chain()

    def _load_chain(self):
        if os.path.exists(self.ledger_path):
            try:
                with open(self.ledger_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def record_event(self, actor, action, details):
        previous_hash = self.chain[-1]["current_hash"] if self.chain else "0" * 64
        timestamp = datetime.utcnow().isoformat()
        
        block = {
            "index": len(self.chain) + 1,
            "timestamp": timestamp,
            "actor": actor,
            "action": action,
            "details": details,
            "previous_hash": previous_hash
        }
        
        block_string = json.dumps(block, sort_keys=True).encode('utf-8')
        current_hash = hashlib.sha256(block_string).hexdigest()
        block["current_hash"] = current_hash
        
        self.chain.append(block)
        self._save_chain()
        return block

    def _save_chain(self):
        with open(self.ledger_path, 'w', encoding='utf-8') as f:
            json.dump(self.chain, f, indent=4)

    def verify_integrity(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current["previous_hash"] != previous["current_hash"]:
                return False, f"Chain broken at block {current['index']}: previous hash mismatch."
            
            block_copy = current.copy()
            c_hash = block_copy.pop("current_hash")
            block_string = json.dumps(block_copy, sort_keys=True).encode('utf-8')
            if hashlib.sha256(block_string).hexdigest() != c_hash:
                return False, f"Block {current['index']} content has been tampered with."
        return True, "Audit ledger integrity verified successfully. 0 tampering detected."

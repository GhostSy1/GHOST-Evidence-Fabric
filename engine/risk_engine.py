import json
import hashlib
from datetime import datetime

class ExplainableRiskEngine:
    def __init__(self):
        self.version = "v3.0-PRO"

    def evaluate(self, finding):
        score = 0.0
        factors = []
        cvss = finding.get("cvss", 0.0)
        if cvss > 0:
            score += cvss * 6.5
            factors.append(f"CVSS score {cvss} contribution: {cvss * 6.5}")
        if finding.get("exploit_available", False):
            score += 25.0
            factors.append("Weaponized exploit publicly available (+25)")
        if not finding.get("auth_required", True):
            score += 15.0
            factors.append("Unauthenticated access vector (+15)")
        if finding.get("public_facing", False):
            score += 10.0
            factors.append("Internet-facing asset exposure (+10)")
        
        score = min(max(score, 0.0), 100.0)
        level = "CRITICAL" if score >= 85 else "HIGH" if score >= 70 else "MEDIUM" if score >= 40 else "LOW"
        return {"risk_score": round(score, 2), "risk_level": level, "factors": factors}

import os
import sys
import json
import csv
import argparse
import hashlib
from datetime import datetime

TOOL_NAME = "GHOST-Evidence-Fabric"
VERSION = "v2.0-ENTERPRISE"

def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(r"""
  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗ █████╗ ██████╗ ██╗██████╗ ██╗ ██████╗ 
 ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ 
 ██║  ███╗███████║██║   ██║███████╗   ██║        ████ât  ███████║██████╔╝██║██║  ██║██║  ███╗
 ██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔══   ██╔══██║██╔══██╗██║██║  ██║██║   ██║
 ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║        ███████╗██║  ██║██████╔╝██║██████╔╝╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝        ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝  ╚══════╝ 
    %s: Unified Security Evidence, Asset Intelligence & Explainable Risk Fabric (%s)
""" % (TOOL_NAME, VERSION))

def compute_sha256(filepath):
    sha = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                sha.update(chunk)
        return sha.hexdigest()
    except Exception:
        return None

def evaluate_risk(finding):
    score = 0.0
    factors = []
    
    cvss = finding.get("cvss", 0.0)
    if cvss > 0:
        score += cvss * 7.0
        factors.append(f"CVSS base score {cvss} contributed {cvss * 7.0:.1f}")
    
    exploit_available = finding.get("exploit_available", False)
    if exploit_available:
        score += 25.0
        factors.append("Public exploit or weaponized PoC available (+25)")
        
    auth_required = finding.get("auth_required", True)
    if not auth_required:
        score += 15.0
        factors.append("Unauthenticated remote access vector (+15)")
        
    exposure = finding.get("public_facing", False)
    if exposure:
        score += 10.0
        factors.append("Asset directly exposed to internet (+10)")
        
    score = min(max(score, 0.0), 100.0)
    
    if score >= 85.0:
        level = "CRITICAL"
    elif score >= 70.0:
        level = "HIGH"
    elif score >= 40.0:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    return {
        "risk_score": round(score, 2),
        "risk_level": level,
        "explainable_factors": factors
    }

def main():
    banner()
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - Enterprise Security Evidence & Risk Fabric")
    parser.add_argument("--ingest", help="Path to input assessment findings or tool output JSON")
    parser.add_argument("--vault", default="vault/evidence_vault.json", help="Path to secure local vault store")
    parser.add_argument("--json", default="reports/fabric_report.json", help="Export unified JSON report")
    parser.add_argument("--csv", default="reports/fabric_report.csv", help="Export unified CSV report")
    args = parser.parse_args()

    target = args.ingest
    if not target:
        target = input("[*] Enter path to tool output file or directory to ingest findings: ").strip()

    print(f"\n[+] Ingesting evidence and running explainable risk engine for: {target}")
    findings = []

    if os.path.exists(target):
        if os.path.isfile(target):
            file_hash = compute_sha256(target)
            try:
                with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            if isinstance(item, dict):
                                risk = evaluate_risk(item)
                                item.update(risk)
                                item["integrity_hash"] = file_hash
                                item["provenance_source"] = target
                                findings.append(item)
                    elif isinstance(data, dict):
                        risk = evaluate_risk(data)
                        data.update(risk)
                        data["integrity_hash"] = file_hash
                        data["provenance_source"] = target
                        findings.append(data)
            except Exception:
                with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                item = {
                    "source_file": target,
                    "raw_content_preview": content[:200],
                    "integrity_hash": file_hash,
                    "ingestion_timestamp": datetime.utcnow().isoformat(),
                    "status": "Raw Evidence Ingested"
                }
                item.update(evaluate_risk(item))
                findings.append(item)
        else:
            for root, _, files in os.walk(target):
                for file in files:
                    fp = os.path.join(root, file)
                    fh = compute_sha256(fp)
                    item = {
                        "file_path": fp,
                        "size": os.path.getsize(fp),
                        "integrity_hash": fh,
                        "ingestion_timestamp": datetime.utcnow().isoformat(),
                        "status": "Discovered Asset"
                    }
                    item.update(evaluate_risk(item))
                    findings.append(item)
    else:
        item = {
            "target": target,
            "status": "Unknown / Target Path Not Found",
            "integrity_hash": None,
            "ingestion_timestamp": datetime.utcnow().isoformat()
        }
        item.update(evaluate_risk(item))
        findings.append(item)

    os.makedirs(os.path.dirname(args.vault), exist_ok=True)
    with open(args.vault, 'w', encoding='utf-8') as vf:
        json.dump(findings, vf, indent=4)
    print(f"[+] Secure local vault updated with {len(findings)} records at: {args.vault}")

    os.makedirs(os.path.dirname(args.json), exist_ok=True)
    with open(args.json, 'w', encoding='utf-8') as jf:
        json.dump(findings, jf, indent=4)
    print(f"[+] Unified JSON Risk Report saved to: {args.json}")

    with open(args.csv, 'w', newline='', encoding='utf-8') as cf:
        if findings:
            keys = ["provenance_source", "status", "risk_score", "risk_level", "integrity_hash"]
        else:
            keys = ["target", "status", "risk_score", "risk_level"]
        writer = csv.DictWriter(cf, fieldnames=keys, extrasaction='ignore')
        writer.writeheader()
        for row in findings:
            writer.writerow({k: row.get(k, "") for k in keys})
    print(f"[+] Unified CSV Risk Report saved to: {args.csv}")

if __name__ == "__main__":
    main()

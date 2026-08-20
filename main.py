import os
import sys
import json
import csv
import argparse
import hashlib
from datetime import datetime

TOOL_NAME = "GHOST-Evidence-Fabric"
VERSION = "v1.0-ENTERPRISE"

def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(r"""
  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗ █████╗ ██████╗ ██╗██████0██╗ ██████╗ 
 ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ 
 ██║  ███╗███████║██║   ██║███████╗   ██║        ████ât  ███████║██████╔╝██║██║  ██║██║  ███╗
 ██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔══   ██╔══██║██╔══██╗██║██║  ██║██║   ██║
 ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║        ███████╗██║  ██║██████╔╝██║██████╔╝╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝        ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝  ╚══════╝ 
    %s: Unified Security Evidence, Asset Intelligence & Provenance Fabric (%s)
""" % (TOOL_NAME, VERSION))

def main():
    banner()
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - Enterprise Security Evidence & Asset Fabric")
    parser.add_argument("--ingest", help="Path to input assessment findings or tool output JSON")
    parser.add_argument("--query", help="Query ingested assets or findings")
    parser.add_argument("--json", default="fabric_report.json", help="Export unified JSON report")
    parser.add_argument("--csv", default="fabric_report.csv", help="Export unified CSV report")
    args = parser.parse_args()

    target = args.ingest
    if not target:
        target = input("[*] Enter path to tool output file or directory to ingest findings: ").strip()

    print(f"\n[+] Processing security evidence fabric ingestion for: {target}")
    ledger = []

    if os.path.exists(target):
        if os.path.isfile(target):
            try:
                with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        ledger.extend(data)
                    else:
                        ledger.append(data)
            except Exception:
                with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                ledger.append({
                    "source_file": target,
                    "raw_content_preview": content[:200],
                    "ingestion_timestamp": datetime.utcnow().isoformat(),
                    "status": "Raw Evidence Ingested"
                })
        else:
            for root, _, files in os.walk(target):
                for file in files:
                    fp = os.path.join(root, file)
                    ledger.append({
                        "file_path": fp,
                        "size": os.path.getsize(fp),
                        "ingestion_timestamp": datetime.utcnow().isoformat(),
                        "status": "Discovered Asset"
                    })
    else:
        ledger.append({
            "target": target,
            "status": "Unknown / Target Path Not Found",
            "ingestion_timestamp": datetime.utcnow().isoformat()
        })

    with open(args.json, 'w', encoding='utf-8') as jf:
        json.dump(ledger, jf, indent=4)
    print(f"[+] Unified Evidence JSON Report saved to: {args.json}")

    with open(args.csv, 'w', newline='', encoding='utf-8') as cf:
        if ledger:
            keys = list(ledger[0].keys())
        else:
            keys = ["target", "status", "ingestion_timestamp"]
        writer = csv.DictWriter(cf, fieldnames=keys)
        writer.writeheader()
        for row in ledger:
            writer.writerow({k: row.get(k, "") for k in keys})
    print(f"[+] Unified Evidence CSV Report saved to: {args.csv}")

if __name__ == "__main__":
    main()

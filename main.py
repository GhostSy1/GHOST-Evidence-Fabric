import os
import sys
import argparse
import json
from engine.risk_engine import ExplainableRiskEngine

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
    GHOST-Evidence-Fabric: Enterprise Multi-Language Security Platform (v3.0)
""")

def main():
    banner()
    parser = argparse.ArgumentParser(description="GHOST-Evidence-Fabric CLI")
    parser.add_argument("--target", help="Target asset or scan report file")
    args = parser.parse_args()

    target = args.target
    if not target:
        target = input("[*] Enter target asset IP or report path: ").strip()

    print(f"\n[+] Initializing multi-engine evaluation for target: {target}")
    engine = ExplainableRiskEngine()
    
    sample_finding = {
        "asset": target,
        "finding_type": "Remote Code Execution & Buffer Overflow",
        "cvss": 9.8,
        "exploit_available": True,
        "auth_required": False,
        "public_facing": True
    }
    
    result = engine.evaluate(sample_finding)
    print(json.dumps(result, indent=4))
    print("\n[+] Authorized evaluation completed successfully.")

if __name__ == "__main__":
    main()

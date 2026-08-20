import os
import json

def parse_report(filepath):
    """
    Plugin parser for standardized Ghost tool output files.
    Normalizes raw tool findings into GHOST-Evidence-Fabric evidentiary schema.
    """
    findings = []
    if not os.path.exists(filepath):
        return findings
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    findings.append({
                        "asset": item.get("target") or item.get("host") or "Unknown",
                        "finding_type": item.get("type") or item.get("vulnerability") or "Generic Asset Finding",
                        "cvss": item.get("cvss", 5.0),
                        "exploit_available": item.get("exploit_available", False),
                        "auth_required": item.get("auth_required", True),
                        "public_facing": item.get("public_facing", True),
                        "source_plugin": "ghost_scanner_plugin"
                    })
            elif isinstance(data, dict):
                findings.append({
                    "asset": data.get("target") or data.get("host") or "Unknown",
                    "finding_type": data.get("type") or data.get("vulnerability") or "Generic Asset Finding",
                    "cvss": data.get("cvss", 5.0),
                    "exploit_available": data.get("exploit_available", False),
                    "auth_required": data.get("auth_required", True),
                    "public_facing": data.get("public_facing", True),
                    "source_plugin": "ghost_scanner_plugin"
                })
    except Exception as e:
        findings.append({
            "asset": filepath,
            "finding_type": "Parse Error",
            "cvss": 0.0,
            "error": str(e),
            "source_plugin": "ghost_scanner_plugin"
        })
    return findings

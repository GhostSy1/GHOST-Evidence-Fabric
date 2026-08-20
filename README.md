# GHOST-Evidence-Fabric

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Unified Security Evidence, Asset Intelligence & Explainable Risk Fabric**  
> Developed by Abdulaziz (Ghost-SY1).

---

## Overview
**GHOST-Evidence-Fabric** is an advanced open-source enterprise platform designed to solve a critical challenge for security teams and penetration testers: **fragmented tool outputs, conflicting findings, and lack of verifiable evidence provenance across multi-vector assessments**.

---

## Core Architecture & Features
- **Evidence Ingestion & Normalization**: Standardizes disparate findings from network scanners, web evaluators, static analyzers, and cloud audits into a unified evidentiary schema.
- **Secure Local Vault & Integrity Hashing**: Automatically calculates SHA-256 hashes for all ingested evidence and stores tamper-evident records locally.
- **Explainable Risk Engine**: Evaluates findings based on CVSS scores, exploit availability, authentication requirements, and internet exposure, providing transparent factor breakdowns rather than opaque numbers.
- **Visual Web UI**: Modern dark-mode web dashboard (`web/index.html`) for managing assets, evidence ledger, and risk registers.
- **Audit-Ready Export**: Generates tamper-evident JSON and CSV audit trails suitable for executive presentation and technical validation.

---

## Installation & Usage
```bash
git clone https://github.com/GhostSy1/GHOST-Evidence-Fabric.git
cd GHOST-Evidence-Fabric
pip install -r requirements.txt
python3 main.py --ingest /path/to/tool_output.json
```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

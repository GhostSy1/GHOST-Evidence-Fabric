# GHOST-Evidence-Fabric

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Unified Security Evidence, Asset Intelligence & Explainable Risk Fabric**  
> Developed by Abdulaziz (Ghost-SY1).

---

## Overview
**GHOST-Evidence-Fabric** is an advanced enterprise security platform designed to unify disparate scanner outputs, enforce tamper-evident chain of custody, and evaluate risk using an explainable mathematical engine.

---

## Key Features & Architecture
1. **Explainable Risk Engine**: Evaluates CVSS base scores, exploit availability, authentication requirements, and public internet exposure to generate transparent risk scores.
2. **Secure Local Vault & Integrity Hashing**: Computes cryptographic `SHA-256` hashes for all ingested files to guarantee data authenticity.
3. **Immutable Audit Ledger**: Maintains a tamper-evident blockchain-style hash chain for all operational events and evidence ingestions.
4. **Plugin Architecture**: Modular parser plugins (`plugins/ghost_scanner_plugin.py`) to standardize outputs from various security tools.
5. **Visual Web UI**: Interactive dark-mode dashboard (`web/index.html`) for asset and finding management.

---

## Installation & Usage
```bash
git clone https://github.com/GhostSy1/GHOST-Evidence-Fabric.git
cd GHOST-Evidence-Fabric
pip install -r requirements.txt

# Ingest scan report and run risk engine
python3 main.py --ingest /path/to/scan_report.json

# Verify immutable audit ledger integrity
python3 main.py --verify-audit
```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

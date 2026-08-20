# GHOST-Evidence-Fabric

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![Go](https://img.shields.io/badge/Go-1.21%2B-blue)]()
[![Rust](https://img.shields.io/badge/Rust-Edition%202021-orange)]()
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Unified Security Evidence, Asset Intelligence & Explainable Risk Fabric**  
> Developed by Abdulaziz (Ghost-SY1).

---

## Overview & Purpose
**GHOST-Evidence-Fabric** is an enterprise-grade, multi-language security platform engineered to solve fragmentation in vulnerability management. It combines a Python **Explainable Risk Engine**, a Go high-performance network prober, a Rust cryptographic integrity verifier, and a TypeScript contract validator.

---

## Architecture & Multi-Language Components
| Component | Language | Purpose |
|---|---|---|
| `main.py` | Python | Interactive CLI, banner initialization, orchestration |
| `engine/risk_engine.py` | Python | Explainable risk scoring model (ERE) |
| `core/scanner.go` | Go | High-performance concurrent TCP port prober |
| `core/hasher.rs` | Rust | SHA-256 cryptographic file fingerprinting |
| `api/validator.ts` | TypeScript | Strict evidentiary schema validation |

---

## Installation & Usage
```bash
git clone https://github.com/GhostSy1/GHOST-Evidence-Fabric.git
cd GHOST-Evidence-Fabric

# Run Python CLI Engine
python3 main.py --target 159.26.100.226

# Run Go Prober
go run core/scanner.go 159.26.100.226
```

---

## Integration & API Contracts
The platform supports modular ingestion plugins (`plugins/`) and tamper-evident audit ledgers (`audit/`). See `docs/` for full API specifications.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

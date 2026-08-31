# Quantinuum Singapore Grand Challenge

Quantum computing submission project exploring two complementary programming approaches for running quantum programs on Quantinuum'sSystems via the Nexus cloud platform.

## Overview

This project demonstrates quantum program development using two distinct frameworks:

- **Guppy** - A Pythonic quantum-classical programming language with high-level abstractions
- **Pytket** - A quantum circuit optimization toolkit with lower-level circuit control

Both submissions target Quantinuum's H2-2E quantum processor through the AQORA (Azure Quantum Resource API) interface, with intermediate compilation via HUGR-QIR.

## Softwarte

- **Guppy** - Quantum-first programming language, and now exectuble on System Model H2 via the hugr-qir compiler.
- **Pytket** - Quantum circuit toolkit and optimizing compiler


## Getting Started

### Installation

```bash
uv sync
```

### Running Submissions

```bash
python src/guppy_submission.py
python src/pytket_submission.py
```

## License

This project is licensed under the Apache License 2.0 - see LICENSE file for details.

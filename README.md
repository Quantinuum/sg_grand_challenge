# Quantinuum Singapore Grand Challenge

Quantum computing submission project exploring two complementary programming approaches for running quantum programs on Quantinuum'sSystems via the Nexus cloud platform.

## Overview

This project demonstrates quantum program development using two distinct frameworks:

- **Guppy** - A Pythonic quantum-classical programming language with high-level abstractions.
- **Pytket** - A quantum circuit builder and optimizing compiler toolkit.
- **Qiskit** - 3rd part quantum circuit builder package.

Job submissions target Quantinuum's H2 emulators through Aqora's interface. Guppy is backwards compatible on H2 emulators by lowering source programs to QIR via HUGR-QIR.

The table below shows support for Guppy, Pytket & Qiskit across all the emulator and syntax checker targets available to users during the Grand Challenge.

| Framework / Target | H2-1E | H2-2E | H2-Emulator | H2-1SC | H2-2SC |
| ------------------ | :---: | :---: | :---------: | :----: | :----: |
| Guppy (hugr-qir)   |   ✅   |   ✅   |             |    ✅   |    ✅   |
| Pytket             |   ✅   |   ✅   |      ✅      |    ✅   |    ✅   |
| Qiskit             |   ✅   |   ✅   |      ✅      |    ✅   |    ✅   |


- `H2-Emulator`: A Nexus-tier emulation resource with state-vector and stabilizer simulation support. An average error model across all H2 hardware instances is used to model noise mechanisms. This is costed in seconds.
- `H2-1E`: A hardware-tier emulator instance with state-vector and stabilizer simulation support. The noise model and physical properties of the emulator corresponds to H2-1 hardware. This is costed in hardware quantum credits (HQCs).
- `H2-2E`: A hardware-tier emulator instance with state-vector and stabilizer simulation support. The noise model and physical properties of the emulator corresponds to H2-2 hardware. This is costed in hardware quantum credits (HQCs).
- `H2-1SC`, `H2-2SC`: A debug tool, also known as a syntax checker, to verify user programs and to estimate the job cost of running a program on hardware or hardware-tier emulators.

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

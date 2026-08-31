from pytket.circuit import Circuit, OpType
from pytket.predicates import GateSetPredicate
from typing import Dict

from aqora.pytket.backend import GATESET

predicate = GateSetPredicate(GATESET)

def _get_stats(
    circuit: Circuit,
    n_shots: int
) -> Dict[str, int]:
    """Estimate the cost of a given circuit based on the number of each type of gate."""
    if not predicate.verify(circuit):
        raise ValueError("Circuit contains gates not in the allowed gate set.")
    stats = {
        "n1q": 0,
        "n2q": 0,
        "spam": circuit.n_qubits,
        "shots": n_shots
    }
    for com in circuit.get_commands():
        if com.op.type == OpType.PhasedX:
            stats["n1q"] += 1
        elif com.op.type == OpType.ZZMax:
            stats["n2q"] += 1
        elif com.op.type == OpType.ZZPhase:
            stats["n2q"] += 1
        elif com.op.type == OpType.Measure:
            stats["spam"] += 1
        elif com.op.type == OpType.Reset:
            stats["spam"] += 1

    return stats


def estimate_cost(
    circuit: Circuit,
    n_shots: int
) -> float:
    _stats = _get_stats(circuit, n_shots)
    gating_cost = _stats["n1q"] + 10 * _stats["n2q"] + 5 * _stats["spam"]
    shot_factor = _stats["shots"] / 5000
    return 5 +  gating_cost * shot_factor


if __name__ == "__main__":
    from pytket.circuit import Qubit

    # Example usage
    circ = Circuit(2, 1)
    circ.PhasedX(0.5, 0, 0)
    circ.ZZMax(0, 1)
    circ.Measure(0, 0)
    circ.Reset(1)
    print(estimate_cost(circ, 1000))
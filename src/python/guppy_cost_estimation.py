from hugr import Hugr
import hugr

def _count_ops(hugr_binary: Hugr, string_name: str) -> int:
    count = 0
    for _, data in hugr_binary.nodes():
        if string_name in data.op.name():
            count += 1
    return count

def _program_stats(hugr_binary: Hugr) -> dict:
    return {
        "PhasedX": _count_ops(hugr_binary, "PhasedX"),
        "ZZMax": _count_ops(hugr_binary, "ZZMax"),
        "ZZPhase": _count_ops(hugr_binary, "ZZPhase"),
        "Measure": _count_ops(hugr_binary, "Measure"),
    }


def estimate_cost(hugr: Hugr, n_qubits: int, n_shots: int) -> float:
    stats = _program_stats(hugr)
    gating_cost = stats["PhasedX"] + 10 * (stats["ZZMax"] + stats["ZZPhase"]) + 5 * (n_qubits + stats["Measure"])
    shot_factor = n_shots / 5000
    return 5 + gating_cost * shot_factor

if __name__ == "__main__":
    from guppylang import guppy
    from guppylang.std.quantum import qubit, discard
    from guppylang.std.angles import angle
    from guppylang.std.qsystem import phased_x, zz_max, measure_and_reset
    from guppylang.std.builtins import output

    @guppy.comptime
    def main() -> None:
        q0 = qubit()
        q1 = qubit()

        phased_x(q0, angle(0.5), angle(0))
        zz_max(q0, q1)
        c0 = measure_and_reset(q0)
        discard(q0)
        discard(q1)
        output("c0", c0.read())

    # Add nodes and operations to the Hugr instance as needed
    n_qubits = 2
    n_shots = 1000
    print(estimate_cost(main.compile().modules[0], n_qubits, n_shots))
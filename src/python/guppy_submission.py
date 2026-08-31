
from guppylang import guppy
from guppylang.std.builtins import output
from guppylang.std.quantum import qubit, measure, h, cx, measure

from hugr_qir.hugr_to_qir import hugr_to_qir
from hugr_qir.output import OutputFormat

from aqora import QPU


N = 10

@guppy.comptime
def main() -> None:
    qubit_top = qubit()
    h(qubit_top)
    qubits = [qubit() for _ in range(N)]
    for i in range(N):
        cx(qubit_top, qubits[i])
        m = measure(qubits[i])
        output(f"result_{i}", m.read())
    m_top = measure(qubit_top)
    output("result_top", m_top.read())
from hugr_qir.hugr_to_qir import hugr_to_qir
from hugr_qir.output import OutputFormat

hugr = main.compile()
qir_program = hugr_to_qir(
    hugr, 
    output_format=OutputFormat.BITCODE
)

qpu = QPU(platform="nexus:H2-2E")

job = qpu.run(qir_program, shots=10)

counts = job.counts(timeout=600)[0]
print(counts)
print(job.result_items())
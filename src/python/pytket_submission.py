from pytket.circuit import Circuit
from pytket.circuit.display import get_circuit_renderer
from pytket.passes import AutoRebase

from aqora import QPU
from aqora.pytket.backend import GATESET

def bell_circuit() -> Circuit:
    """Prepare (|00> + |11>)/sqrt(2) and measure both qubits."""
    circ = Circuit(2, 2)
    circ.H(0)
    circ.CX(0, 1)
    circ.measure_all()
    return circ

bell = bell_circuit()

compiled = bell.copy()
AutoRebase(GATESET).apply(compiled)

qpu = QPU(platform="nexus:H2-2E")

job = qpu.run(compiled, shots=10)

counts = job.counts(timeout=600)[0]
print(counts)
print(job.result_items())

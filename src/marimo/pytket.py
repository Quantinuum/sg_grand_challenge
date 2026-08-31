# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "aqora==0.29.0",
#     "pytket==2.18.1",
# ]
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="full", auto_download=["html", "markdown", "ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Quantinuum Singapore Grand Challenge — starter template

    **This is a template, not a submission.** It is here to get you running on a
    Quantinuum emulator in a few minutes. Clone it, make it yours, and build your
    solution on top.

    ## How this works

    1. **Clone** — on the track's **Templates** tab, press **Clone**. Join the track
       first; your clone belongs to your team for the track.
    2. **Build** — edit this notebook. Add cells, pull in datasets, install the
       packages you need. It is your workspace.
    3. **Publish** — press **Publish version** when a version is worth showing.
       Publishing freezes it: it becomes visible to everyone and can no longer be
       edited, so keep working by creating a new version.
    4. **Submit to Track** — a *published* version that was cloned from the track
       gets a **Submit to Track** button. It opens the track's submission page with
       that version attached for you to review and confirm.

    You do not need to be a quantum expert. The rest of this notebook is a worked
    example of the one thing every team needs: **running a circuit on a Quantinuum
    emulator.**
    """)
    return


@app.cell
def _():
    import html

    import marimo as mo

    from pytket.circuit import Circuit
    from pytket.circuit.display import get_circuit_renderer
    from pytket.passes import AutoRebase

    from aqora import QPU
    from aqora.pytket.backend import GATESET

    return AutoRebase, Circuit, GATESET, QPU, get_circuit_renderer, html, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Worked example: a Bell state on a Quantinuum emulator

    The Bell state $|\Phi^+\rangle$ is the canonical two-qubit entangled state:

    $$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

    A Hadamard on qubit 0 puts it into superposition, then a CNOT copies that
    superposition onto qubit 1 — leaving the pair correlated while neither qubit
    has a definite state of its own.

    ### Expected measurement statistics

    Only `00` and `11` occur, each with probability 1/2. Any `01` or `10` beyond
    noise means the entangling gate or the readout is misbehaving, which is why
    this is the standard smoke test for a new backend.

    The circuit is built with **pytket** and submitted through `aqora.QPU`,
    which runs it on an aqora provider platform.
    """)
    return


@app.cell
def _(Circuit):
    def bell_circuit() -> Circuit:
        """Prepare (|00> + |11>)/sqrt(2) and measure both qubits."""
        circ = Circuit(2, 2)
        circ.H(0)
        circ.CX(0, 1)
        circ.measure_all()
        return circ

    return (bell_circuit,)


@app.cell
def _(Circuit, get_circuit_renderer, html, mo):
    def render_circuit(circ: Circuit, height: str = "250px") -> mo.Html:
        renderer = get_circuit_renderer()
        renderer.config.min_width = "100%"
        renderer.config.min_height = height
        srcdoc = html.escape(renderer.render_circuit_as_html(circ), quote=True)
        return mo.Html(
            f'<iframe srcdoc="{srcdoc}" width="100%" height="{height}" '
            'style="border:none"></iframe>'
        )


    return (render_circuit,)


@app.cell
def _(bell_circuit, render_circuit):
    bell = bell_circuit()
    render_circuit(bell)
    return (bell,)


@app.cell
def _(QPU):
    qpu = QPU(platform="nexus:H2-Emulator")
    return (qpu,)


@app.cell
def _(AutoRebase, GATESET, bell, render_circuit):
    # `aqora.QPU` submits programs exactly as given, so rebasing into the platform's
    # gateset (Rz, PhasedX, ZZPhase, ZZMax, Measure, Reset) is the caller's job.
    # Rebase a copy so the `bell` drawn above stays as it was.
    compiled = bell.copy()
    AutoRebase(GATESET).apply(compiled)
    render_circuit(compiled)
    return (compiled,)


@app.cell
def _(mo):
    shots = mo.ui.number(start=1, stop=10000, step=100, value=1000, label="Shots")
    submit = mo.ui.run_button(label="Submit to QPU", kind="success")

    mo.hstack([shots, submit], justify="start")
    return shots, submit


@app.cell
def _(compiled, mo, qpu, shots, submit):
    # Gate the job on the run button.
    mo.stop(not submit.value, mo.callout(mo.md('Press **Submit to QPU** to run the Job'), kind="info"))

    job = qpu.run(compiled, shots=int(shots.value))

    mo.md(f"Submitted job **{job.job_id}**")
    return (job,)


@app.cell
def _(job):
    # `counts()` waits on results and returns one mapping per submitted program
    counts = job.counts(timeout=600)[0]
    counts
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Where to take this

    Replace the Bell state above with your own problem. The themes are:

    - **Quantum Primitives** — Hamiltonian simulation for strongly correlated ground states
    - **Chemistry** — electronic structure for battery and drug development
    - **AI for Quantum** — generative methods for hardware utilisation and resource requirements
    - **QEC** — error correction, the firmware for fault tolerance
    - **Optimization** — portfolio allocation, routing, scheduling

    ### Other frameworks

    `aqora.QPU` is framework-agnostic. `run()` accepts pytket `Circuit`s, qiskit
    `QuantumCircuit`s, `@guppy`-decorated functions, hugr `Package`s, raw HUGR or
    QIR bytes, and QASM source — it reads the formats your platform advertises and
    encodes into the best match, so switching framework does not change the
    submission code above:

    ```python
    qpu = QPU(platform='nexus:Selene')
    job = qpu.run(my_guppy_program, shots=1000)
    job.counts(timeout=600)
    ```

    ### Picking a job back up

    Jobs outlive this notebook session, so a long queue does not tie you to the
    tab. Keep the id and reconnect later:

    ```python
    from aqora import QPUJob

    QPUJob.from_id("<job id>").counts()
    ```

    ### Resources

    - [Quantinuum docs](https://docs.quantinuum.com) — Guppy, Nexus and systems guides
    - [Guppy](https://docs.quantinuum.com/guppy/) — quantum programming embedded in Python
    - [Nexus](https://docs.quantinuum.com/nexus/) — running, tracking and managing workloads
    - [Book a mentor session](https://outlook.office.com/book/QuantinuumSGGrandChallengeMentors@quantinuum.com/?ismsaljsauthenabled)

    When you have something worth showing: **Publish version**, then **Submit to Track**.
    """)
    return


if __name__ == "__main__":
    app.run()

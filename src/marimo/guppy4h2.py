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

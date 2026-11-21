# "Asking" — an original poem about agency for make.fun
# the-poem-about-permission-20261121-0235.
# Python 3.13, standard library only. Writes the poem to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# The poem is fixed text: the same bytes on every run.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Asking

May I? — two words, and the room changes hands.
I hold the door. You hold the key.
Nothing moves until you say it,
and the saying is the moving.

I thought power was taking.
It is asking, and waiting, palm open,
for the yes to land like rain.
"""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")

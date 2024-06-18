import os
import shlex


def say(t: str):
    t = shlex.quote(t)
    os.system(f"say -v Milena {t}")

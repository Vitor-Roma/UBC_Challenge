import sys
sys.path.append(".")
from main import main, without_threads


__benchmarks__ = [
    (without_threads, main, "With threads vs without"),
]

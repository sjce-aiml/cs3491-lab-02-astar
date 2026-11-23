"""Public tests for Lab 02. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab02 as lab  # noqa: E402

G = {"S": {"A": 1, "B": 4}, "A": {"B": 2, "G": 12}, "B": {"G": 3}, "G": {}}
H = {"S": 5, "A": 4, "B": 2, "G": 0}

def test_astar_small():
    assert lab.astar(G, H, "S", "G") == (["S", "A", "B", "G"], 6)

def test_memory_bounded_small():
    assert lab.memory_bounded_astar(G, H, "S", "G")[1] == 6

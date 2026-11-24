"""Lab 2 starter code: informed search (A*, memory-bounded A* as IDA*)."""
import heapq
import itertools

def astar(graph, h, start, goal):
    """graph: {node: {nbr: cost}}, h: {node: heuristic}. Return (path, cost) or (None, inf)."""
    raise NotImplementedError('TODO: implement this')

def memory_bounded_astar(graph, h, start, goal):
    """Iterative-deepening A* (memory grows only with path depth). Return (path, cost)."""
    raise NotImplementedError('TODO: implement this')

def uniform_cost_search(graph, start, goal):
    """Dijkstra / uniform-cost search: expand the cheapest path first (no heuristic).
Return (path, cost) or (None, inf)."""
    raise NotImplementedError('TODO: implement this')

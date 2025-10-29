import heapq
from heuristics import hamming, manhattan


def get_neighbors(state):
    """
    Gibt alle möglichen Nachbarn (Zustände) zurück,
    die durch Verschieben der leeren Kachel entstehen.
    """
    zero = state.index(0)
    x, y = divmod(zero, 3)
    moves = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state[:]
            ni = nx * 3 + ny
            new_state[zero], new_state[ni] = new_state[ni], new_state[zero]
            moves.append(new_state)
    return moves


def astar(start, goal, heuristic):
    """
    Führt den A*-Algorithmus für das 8-Puzzle aus.
    Misst die Anzahl expandierter Knoten bis zur Lösung.

    Eingabe:
        start (list[int]): Startzustand
        goal (list[int]): Zielzustand
        heuristic (function): Heuristikfunktion

    Ausgabe:
        int: Anzahl der expandierten Knoten
    """
    open_set = [(heuristic(start, goal), 0, start)]
    g = {tuple(start): 0}
    expanded = 0

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        expanded += 1
        if current == goal:
            return expanded
        for neighbor in get_neighbors(current):
            ng = g[tuple(current)] + 1
            if ng < g.get(tuple(neighbor), float("inf")):
                g[tuple(neighbor)] = ng
                f = ng + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, ng, neighbor))
    return expanded
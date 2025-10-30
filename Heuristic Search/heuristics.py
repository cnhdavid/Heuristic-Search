def hamming(state, goal):
    """
    Hamming-Heuristik:
    Zählt, wie viele Kacheln sich nicht an der richtigen Position befinden.
    """
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)


def manhattan(state, goal):
    """
    Manhattan-Heuristik:
    Summe der Manhattan-Distanzen (Zeilen- und Spalten-Abstand)
    zwischen aktueller und Zielposition jeder Kachel.
    """
    dist = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        goal_pos = goal.index(val)
        dist += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return dist

import random
import time

def is_solvable(state):
    """
    Prüft, ob ein gegebener 8-Puzzle-Zustand lösbar ist.
    Ein Zustand ist lösbar, wenn die Anzahl der Inversionen gerade ist.

    Eingabe:
        state (list[int]): Liste mit 9 Zahlen (0–8), wobei 0 das leere Feld ist.
    Ausgabe:
        bool: True, wenn lösbar, sonst False.
    """
    inv_count = sum(
        1 for i in range(8) for j in range(i + 1, 9)
        if state[i] and state[j] and state[i] > state[j]
    )
    return inv_count % 2 == 0


def random_puzzle():
    """
    Erzeugt ein zufälliges, lösbares 8-Puzzle.
    """
    while True:
        s = random.sample(range(9), 9)
        if is_solvable(s):
            return s


def measure_time(func):
    """
    Misst die Laufzeit einer Funktion in Sekunden.
    Gibt (Ergebnis, Zeit) zurück.
    """
    start = time.time()
    result = func()
    end = time.time()
    return result, end - start

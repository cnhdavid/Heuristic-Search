import csv
import statistics
from utils import random_puzzle, measure_time
from solver import astar
from heuristics import hamming, manhattan

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
results = {"hamming": [], "manhattan": []}

# CSV-Datei mit Semikolon (Excel-kompatibel)
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')

    # ===== Tabelle 1: Einzelergebnisse =====
    writer.writerow(["Run", "Heuristic", "Time (s)", "Expanded Nodes"])

    for i in range(100):
        s = random_puzzle()
        for name, heuristic in [("hamming", hamming), ("manhattan", manhattan)]:
            def run(): return astar(s, goal, heuristic)
            expanded, t = measure_time(run)
            results[name].append((t, expanded))
            writer.writerow([i + 1, name, f"{t:.6f}", expanded])
        print(f"Fortschritt: {i + 1}/100")

    # Leerzeile zwischen Tabellen
    writer.writerow([])

    # ===== Tabelle 2: Zusammenfassung =====
    writer.writerow(["Summary", "Heuristic", "Mean Time (s)", "Std Time", "Mean Nodes", "Std Nodes"])
    for name in results:
        times = [r[0] for r in results[name]]
        nodes = [r[1] for r in results[name]]
        writer.writerow([
            "",
            name,
            f"{statistics.mean(times):.4f}",
            f"{statistics.stdev(times):.4f}",
            f"{statistics.mean(nodes):.1f}",
            f"{statistics.stdev(nodes):.1f}"
        ])

print("Fertig! results.csv enthält zwei Tabellen (Runs + Summary).")

#!/usr/bin/env python3
"""tracker.py — Plattformübergreifendes Zeit-/Einnahmen-Tracking für
Mini-AI-Aufgaben-Nebenverdienst.

Zweck: den tatsächlichen effektiven Stundenlohn je Plattform ermitteln,
statt sich auf unbelegte Zahlen aus Hook-Videos zu verlassen.

Nutzung:
    python3 tracker.py add --platform Outlier --date 2026-09-12 \\
        --hours 1.5 --earnings-usd 32.50 --eur-rate 0.92 --tasks 14

    python3 tracker.py report
    python3 tracker.py report --platform Outlier
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "sessions.csv"
FIELDS = ["date", "platform", "hours", "earnings_usd", "eur_rate", "earnings_eur", "tasks", "note"]


def _ensure_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()


def add_session(args: argparse.Namespace) -> None:
    _ensure_file()
    earnings_eur = args.earnings_usd * args.eur_rate if args.earnings_usd is not None else args.earnings_eur
    if earnings_eur is None:
        raise SystemExit("Gib entweder --earnings-eur oder --earnings-usd zusammen mit --eur-rate an.")
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(
            {
                "date": args.date,
                "platform": args.platform,
                "hours": args.hours,
                "earnings_usd": args.earnings_usd or "",
                "eur_rate": args.eur_rate or "",
                "earnings_eur": round(earnings_eur, 2),
                "tasks": args.tasks or "",
                "note": args.note or "",
            }
        )
    print(f"Gespeichert: {args.platform} am {args.date} — {args.hours} h, {earnings_eur:.2f} EUR")


def report(args: argparse.Namespace) -> None:
    if not DATA_FILE.exists():
        print("Noch keine Daten erfasst. Erst 'add' benutzen.")
        return

    totals: dict[str, dict[str, float]] = defaultdict(lambda: {"hours": 0.0, "eur": 0.0, "tasks": 0.0})
    with DATA_FILE.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if args.platform and row["platform"].lower() != args.platform.lower():
                continue
            totals[row["platform"]]["hours"] += float(row["hours"] or 0)
            totals[row["platform"]]["eur"] += float(row["earnings_eur"] or 0)
            totals[row["platform"]]["tasks"] += float(row["tasks"] or 0)

    if not totals:
        print("Keine passenden Einträge gefunden.")
        return

    rows = []
    for platform, t in totals.items():
        rate = t["eur"] / t["hours"] if t["hours"] else 0.0
        rows.append((platform, t["hours"], t["eur"], rate, t["tasks"]))
    rows.sort(key=lambda r: r[3], reverse=True)

    print(f"{'Plattform':<20}{'Stunden':>10}{'EUR gesamt':>14}{'EUR/h':>10}{'Tasks':>10}")
    print("-" * 64)
    grand_hours = grand_eur = 0.0
    for platform, hours, eur, rate, tasks in rows:
        print(f"{platform:<20}{hours:>10.2f}{eur:>14.2f}{rate:>10.2f}{tasks:>10.0f}")
        grand_hours += hours
        grand_eur += eur
    print("-" * 64)
    overall_rate = grand_eur / grand_hours if grand_hours else 0.0
    print(f"{'GESAMT':<20}{grand_hours:>10.2f}{grand_eur:>14.2f}{overall_rate:>10.2f}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Eine Arbeits-Session eintragen")
    add_p.add_argument("--platform", required=True)
    add_p.add_argument("--date", required=True, help="YYYY-MM-DD")
    add_p.add_argument("--hours", type=float, required=True)
    add_p.add_argument("--earnings-usd", type=float, default=None)
    add_p.add_argument("--eur-rate", type=float, default=None, help="USD->EUR Kurs des Auszahlungstages")
    add_p.add_argument("--earnings-eur", type=float, default=None, help="Alternative: direkt in EUR")
    add_p.add_argument("--tasks", type=int, default=None)
    add_p.add_argument("--note", default=None)
    add_p.set_defaults(func=add_session)

    report_p = sub.add_parser("report", help="Effektiven EUR/h je Plattform anzeigen")
    report_p.add_argument("--platform", default=None)
    report_p.set_defaults(func=report)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

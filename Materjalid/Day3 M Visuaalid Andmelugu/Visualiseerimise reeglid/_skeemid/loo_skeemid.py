# -*- coding: utf-8 -*-
"""Skeemid töö dokumentatsioonile — Liikumisaktiivsuse programmid."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parent
TEAL = "#0A3D3A"
TEAL2 = "#1A3D40"
ACCENT = "#2EC4B6"
BLUE = "#4A9FE8"
CORAL = "#FF8B6A"
PURPLE = "#7B68C7"
GOLD = "#C9A227"
GREEN = "#2FA36B"
RED = "#C0392B"
BG = "#F5F5F5"
WHITE = "#FFFFFF"
MUTED = "#3D6B68"
INK = "#1A3D40"
LIGHT = "#E8F6F4"

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Segoe UI", "Calibri", "Arial"],
        "axes.unicode_minus": False,
        "figure.facecolor": WHITE,
        "savefig.facecolor": WHITE,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.18,
    }
)


def box(ax, x, y, w, h, text, fc=WHITE, ec=TEAL, lw=1.4, ts=9.5, tc=INK, weight="medium", radius=0.08, va="center"):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
        zorder=2,
    )
    ax.add_patch(p)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va=va,
        fontsize=ts,
        color=tc,
        weight=weight,
        zorder=3,
        linespacing=1.25,
    )
    return p


def arrow(ax, x1, y1, x2, y2, color=TEAL2, rad=0):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.4,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
            zorder=1,
        )
    )


def finish(ax, title, fname, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13, color=TEAL, weight="semibold", pad=10, loc="left")
    fig = ax.figure
    fig.savefig(OUT / fname)
    plt.close(fig)


def skeem_tahemodel():
    fig, ax = plt.subplots(figsize=(11.2, 6.6))
    # fact center
    box(ax, 4.15, 2.35, 2.9, 2.0, "fact_activity\n100 tegevust\n(tähe keskus)", fc=ACCENT, ec=TEAL, ts=11, tc=TEAL, weight="bold", lw=2)
    # dims
    box(ax, 4.25, 5.15, 2.7, 1.35, "dim_date\nkalender 2023–2030\nAlguskuupäev (aktiivne)", fc=LIGHT, ts=9)
    box(ax, 0.2, 2.55, 2.7, 1.55, "dim_direction\n4 WHO suunda\nwho_direction_id", fc=LIGHT, ts=9)
    box(ax, 8.3, 2.55, 2.7, 1.55, "dim_organization\n51 asutust\nlead_org_id", fc=LIGHT, ts=9)
    box(ax, 4.25, 0.15, 2.7, 1.2, "Lõppkuupäev → dim_date\nseos mitteaktiivne", fc=WHITE, ec=GOLD, ts=8.5, tc=MUTED)
    # extras
    box(ax, 0.2, 0.15, 2.7, 1.2, "_Measures\n18 DAX-mõõdikut", fc=WHITE, ec=BLUE, ts=8.5)
    box(ax, 8.3, 0.15, 2.7, 1.2, "INFO.VIEW\nkataloog Info-lehel", fc=WHITE, ec=PURPLE, ts=8.5)

    arrow(ax, 5.6, 4.35, 5.6, 5.15)
    arrow(ax, 4.15, 3.35, 2.9, 3.35)
    arrow(ax, 7.05, 3.35, 8.3, 3.35)
    arrow(ax, 5.6, 2.35, 5.6, 1.35, color=GOLD)

    ax.text(5.6, 4.55, "m : 1", ha="center", fontsize=7.5, color=MUTED)
    ax.text(3.5, 3.52, "m : 1", ha="center", fontsize=7.5, color=MUTED)
    ax.text(7.7, 3.52, "m : 1", ha="center", fontsize=7.5, color=MUTED)

    ax.text(
        0.2,
        6.55,
        "Partnerid, meetmed, sihtrühmad ja indikaatorid on tegevuse real ühel tekstiväljal — mitu-mitmele seoseid ei ole.",
        fontsize=8,
        color=MUTED,
        style="italic",
    )
    finish(ax, "Joonis 1. Semantiline mudel (tähemudel)", "skeem_tahemodel.png", (-0.15, 11.2), (-0.1, 7.0))


def skeem_andmevoog():
    fig, ax = plt.subplots(figsize=(11.2, 5.8))
    # sources
    box(ax, 0.15, 4.15, 2.35, 1.05, "API activities\n100 tegevust", fc=LIGHT, ts=8.5)
    box(ax, 0.15, 2.75, 2.35, 1.05, "API organizations\n51 asutust", fc=LIGHT, ts=8.5)
    box(ax, 0.15, 1.35, 2.35, 1.05, "API policies\n4 suunda + 20 meedet", fc=LIGHT, ts=8.5)
    ax.text(1.32, 5.45, "app.liigume.ee", ha="center", fontsize=8, color=MUTED, weight="semibold")

    box(ax, 3.35, 2.35, 2.5, 1.9, "Power Query (M)\nühendused, lookup,\nloendurid, tüübid\nImport · Anonymous", fc=WHITE, ec=ACCENT, lw=2, ts=8.5)

    box(ax, 6.55, 2.5, 2.15, 1.6, "Tähemudel\nfact + 3 dimi\n+ DAX mõõdikud", fc=ACCENT, tc=TEAL, weight="bold", ts=9)

    pages = ["Ülevaade", "Organisat-\nsioonid", "Poliitikad", "Edenemine", "Info"]
    colors = [ACCENT, BLUE, PURPLE, CORAL, GOLD]
    for i, (name, c) in enumerate(zip(pages, colors)):
        box(ax, 9.15, 4.55 - i * 0.95, 1.9, 0.8, name, fc=WHITE, ec=c, ts=8, lw=1.6)

    arrow(ax, 2.5, 4.65, 3.35, 3.7)
    arrow(ax, 2.5, 3.25, 3.35, 3.3)
    arrow(ax, 2.5, 1.85, 3.35, 2.9)
    arrow(ax, 5.85, 3.3, 6.55, 3.3)
    arrow(ax, 8.7, 3.3, 9.15, 3.3)

    ax.text(4.6, 0.55, "Värskendus: Power BI Desktop  →  Home  →  Refresh", fontsize=8.5, color=MUTED, ha="center")
    finish(ax, "Joonis 2. Andmeallikad ja andmevoog", "skeem_andmevoog.png", (-0.1, 11.25), (0.25, 5.85))


def skeem_grupitoo():
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    stages = [
        ("A", "Probleem\nja mõisted", "ptk 1–4", ACCENT),
        ("B", "Andmed\nja mudel", "ptk 5–9", BLUE),
        ("C", "Visuaalid", "5 lehte", PURPLE),
        ("D", "Analüüs\nja lugu", "ptk 10–12", CORAL),
    ]
    for i, (let, title, result, col) in enumerate(stages):
        x = 0.35 + i * 2.75
        circ = Circle((x + 0.45, 2.85), 0.32, facecolor=col, edgecolor=TEAL, linewidth=1.2, zorder=3)
        ax.add_patch(circ)
        ax.text(x + 0.45, 2.85, let, ha="center", va="center", fontsize=13, color=TEAL, weight="bold", zorder=4)
        box(ax, x, 0.7, 2.25, 1.7, f"{title}\n\n{result}", fc=WHITE, ec=col, ts=10, lw=1.8)
        if i < 3:
            arrow(ax, x + 2.25, 1.55, x + 2.75, 1.55, color=col)
    finish(ax, "Joonis 3. Grupitöö neli etappi", "skeem_grupitoo.png", (-0.1, 11.3), (0.35, 3.55))


def skeem_who():
    fig, ax = plt.subplots(figsize=(11.2, 5.2))
    items = [
        (0.25, 2.55, "4  Struktuurid", "Loome aktiivseid struktuure", "47 tegevust", "juhtimine, andmed, teadus, rahastus", ACCENT, 47),
        (5.75, 2.55, "3  Inimene", "Loome aktiivset inimest", "22 tegevust", "programmid, haridus, tervis", BLUE, 22),
        (0.25, 0.25, "2  Keskkond", "Loome aktiivset keskkonda", "19 tegevust", "taristu, ruum, liiklusohutus", PURPLE, 19),
        (5.75, 0.25, "1  Ühiskond", "Loome aktiivset ühiskonda", "12 tegevust", "hoiakud, kampaaniad, teadlikkus", CORAL, 12),
    ]
    max_n = 47
    for x, y, kood, nimi, arv, selgitus, col, n in items:
        w, h = 5.2, 2.1
        box(ax, x, y, w, h, "", fc=WHITE, ec=col, lw=2, radius=0.1)
        # bar
        bw = 4.6 * (n / max_n)
        ax.add_patch(Rectangle((x + 0.28, y + 0.28), bw, 0.22, facecolor=col, edgecolor="none", zorder=3))
        ax.add_patch(Rectangle((x + 0.28, y + 0.28), 4.6, 0.22, facecolor=BG, edgecolor="#DDDDDD", linewidth=0.6, zorder=2))
        ax.text(x + 0.28, y + 1.55, kood, fontsize=11, color=col, weight="bold", zorder=3)
        ax.text(x + 3.55, y + 1.55, arv, fontsize=12, color=TEAL, weight="bold", zorder=3)
        ax.text(x + 0.28, y + 1.12, nimi, fontsize=9.5, color=INK, zorder=3)
        ax.text(x + 0.28, y + 0.68, selgitus, fontsize=8, color=MUTED, zorder=3)
    finish(ax, "Joonis 4. WHO GAPPA suunad tegevuste arvu järgi (n = 100)", "skeem_who_suunad.png", (-0.15, 11.2), (-0.15, 4.9))


def skeem_aruanne():
    fig, ax = plt.subplots(figsize=(11.2, 4.0))
    pages = [
        ("Ülevaade", "maht, staatus, suunad", ACCENT),
        ("Organisatsioonid", "juhid ja võrgustik", BLUE),
        ("Poliitikad", "meetmed, sihtrühmad", PURPLE),
        ("Edenemine", "indikaatorid, kvaliteet", CORAL),
        ("Info", "mudel ja allikad", GOLD),
    ]
    for i, (name, sub, col) in enumerate(pages):
        x = 0.25 + i * 2.2
        box(ax, x, 0.85, 2.0, 2.15, f"{i+1}\n{name}\n\n{sub}", fc=WHITE, ec=col, ts=9, lw=2, weight="medium")
        if i < 4:
            arrow(ax, x + 2.0, 1.95, x + 2.2, 1.95, color=MUTED)
    ax.text(5.6, 0.25, "Ühised filtrid: WHO suund, tüüp, algusaasta, staatus, juhtorganisatsioon", ha="center", fontsize=8, color=MUTED)
    finish(ax, "Joonis 5. Power BI aruande viis lehte", "skeem_aruanne.png", (-0.1, 11.3), (0.0, 3.35))


def skeem_kvaliteet():
    fig, ax = plt.subplots(figsize=(11.2, 4.2))
    cards = [
        ("72%", "ilma edenemise %-ta", "Keskmine 78% kehtib\nainult 28 real", RED),
        ("38%", "ilma alguskuupäevata", "Kõik 38 on perioodiga\nPidev", GOLD),
        ("22%", "ilma partnerita", "176 partnerlussuhet\nülejäänud 78 tegevusel", CORAL),
        ("0", "tähtaeg ületatud", "Möödunud lõpp ja\nstaatus ≠ Tehtud", GREEN),
    ]
    for i, (big, label, note, col) in enumerate(cards):
        x = 0.25 + i * 2.75
        box(ax, x, 0.45, 2.5, 3.15, "", fc=WHITE, ec=col, lw=2)
        ax.text(x + 1.25, 2.7, big, ha="center", fontsize=22, color=col, weight="bold", zorder=3)
        ax.text(x + 1.25, 2.05, label, ha="center", fontsize=9, color=TEAL, weight="semibold", zorder=3)
        ax.text(x + 1.25, 1.2, note, ha="center", fontsize=8, color=MUTED, zorder=3)
    finish(ax, "Joonis 6. Andmekvaliteedi neli signaali (n = 100)", "skeem_kvaliteet.png", (-0.1, 11.3), (0.15, 3.9))


def skeem_staatus():
    fig, ax = plt.subplots(figsize=(11.2, 3.2))
    # stacked bar 0-100
    segs = [(0, 19, GREEN, "Tehtud 19"), (19, 58, ACCENT, "Töös 58"), (77, 23, GOLD, "Pole alustatud 23")]
    y, h = 1.15, 0.85
    for x, w, c, lab in segs:
        ax.add_patch(FancyBboxPatch((0.4 + x * 0.102, y), w * 0.102, h, boxstyle="square,pad=0", facecolor=c, edgecolor=WHITE, linewidth=1.5, zorder=2))
        ax.text(0.4 + (x + w / 2) * 0.102, y + h / 2, lab, ha="center", va="center", fontsize=10, color=TEAL if c != GREEN else WHITE, weight="bold", zorder=3)
    ax.text(0.4, 2.25, "100 tegevust   ·   tehtud osakaal 19%", fontsize=10, color=TEAL, weight="semibold")
    ax.text(0.4, 0.45, "Rulluv kava 2023–2030: 19 tehtud rida ei tähenda, et kava on 19% valmis. 41 tegevust on pidevad.", fontsize=8, color=MUTED)
    ax.set_xlim(0, 11.2)
    ax.set_ylim(0.15, 2.85)
    ax.axis("off")
    ax.set_title("Joonis 7. Tegevuste staatus", fontsize=13, color=TEAL, weight="semibold", pad=8, loc="left")
    fig.savefig(OUT / "skeem_staatus.png")
    plt.close(fig)


if __name__ == "__main__":
    skeem_tahemodel()
    skeem_andmevoog()
    skeem_grupitoo()
    skeem_who()
    skeem_aruanne()
    skeem_kvaliteet()
    skeem_staatus()
    print("OK", list(OUT.glob("*.png")))

"""
SW02 – Chart-Generator für ZUSAMMENFASSUNG_SW02
Erzeugt Demonstrations-Charts zu Visual Encodings, Chart-Typen und Wahrnehmung.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os

# Ausgabe-Ordner
OUT = os.path.dirname(os.path.abspath(__file__))

# ── Globales Styling ─────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': '#FAFAFA',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
})

COLORS = ['#2196F3', '#FF5722', '#4CAF50', '#FFC107', '#9C27B0', '#00BCD4']

# ═══════════════════════════════════════════════════════════════════════════
# Chart 1: Visual Encodings – Scatter, Bubble, Color-Mapped Bubble
# ═══════════════════════════════════════════════════════════════════════════
def chart_visual_encodings():
    np.random.seed(42)
    n = 30
    x = np.random.rand(n) * 100
    y = np.random.rand(n) * 100
    sizes = np.random.rand(n) * 400 + 50
    categories = np.random.choice(['A', 'B', 'C'], n)
    cat_colors = {'A': COLORS[0], 'B': COLORS[1], 'C': COLORS[2]}

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Scatter (2 Variablen: Position x, Position y)
    axes[0].scatter(x, y, color=COLORS[0], alpha=0.7, edgecolors='white', s=60)
    axes[0].set_title('Scatter Plot\n2 Variablen (Position)')
    axes[0].set_xlabel('Variable 1')
    axes[0].set_ylabel('Variable 2')

    # Bubble (3 Variablen: + Grösse)
    axes[1].scatter(x, y, s=sizes, color=COLORS[0], alpha=0.5, edgecolors='white')
    axes[1].set_title('Bubble Chart\n3 Variablen (+Grösse)')
    axes[1].set_xlabel('Variable 1')
    axes[1].set_ylabel('Variable 2')

    # Bubble + Farbe (4 Variablen)
    for cat in ['A', 'B', 'C']:
        mask = categories == cat
        axes[2].scatter(x[mask], y[mask], s=sizes[mask], color=cat_colors[cat],
                        alpha=0.6, edgecolors='white', label=f'Kategorie {cat}')
    axes[2].set_title('Bubble + Farbe\n4 Variablen (+Kategorie)')
    axes[2].set_xlabel('Variable 1')
    axes[2].set_ylabel('Variable 2')
    axes[2].legend(loc='upper right', fontsize=9)

    fig.suptitle('Visual Encodings: Mehr Variablen durch zusätzliche Kanäle', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'visual_encodings_scatter.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ visual_encodings_scatter.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 2: Bar Chart Familie – Standard, Stacked, Floating
# ═══════════════════════════════════════════════════════════════════════════
def chart_bar_family():
    categories = ['A', 'B', 'C', 'D']
    vals1 = [45, 72, 38, 55]
    vals2 = [30, 45, 22, 40]
    vals3 = [15, 27, 16, 15]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Standard Bar
    axes[0].bar(categories, vals1, color=COLORS[0], edgecolor='white', linewidth=1.5)
    axes[0].set_title('Bar Chart\nWerte vergleichen')
    axes[0].set_ylabel('Wert')
    axes[0].set_ylim(0, max(vals1) * 1.15)

    # Stacked Bar
    axes[1].bar(categories, vals1, color=COLORS[0], edgecolor='white', linewidth=1, label='Typ 1')
    axes[1].bar(categories, vals2, bottom=vals1, color=COLORS[1], edgecolor='white', linewidth=1, label='Typ 2')
    bottom2 = [a + b for a, b in zip(vals1, vals2)]
    axes[1].bar(categories, vals3, bottom=bottom2, color=COLORS[2], edgecolor='white', linewidth=1, label='Typ 3')
    axes[1].set_title('Stacked Bar Chart\nTeile vom Ganzen')
    axes[1].set_ylabel('Kumulierter Wert')
    axes[1].legend(fontsize=9, loc='upper right')

    # Floating Bar
    low = [20, 30, 15, 25]
    high = [60, 85, 50, 70]
    heights = [h - l for h, l in zip(high, low)]
    axes[2].bar(categories, heights, bottom=low, color=COLORS[3], edgecolor='white', linewidth=1.5, alpha=0.85)
    axes[2].set_title('Floating Bar Chart\nSpannweite / Range')
    axes[2].set_ylabel('Wert')

    fig.suptitle('Bar Chart Familie: Verschiedene Varianten für unterschiedliche Aufgaben', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'bar_chart_family.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ bar_chart_family.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 3: Encoding-Genauigkeit (Munzner-Ranking)
# ═══════════════════════════════════════════════════════════════════════════
def chart_encoding_accuracy():
    encodings = [
        'Position (gemeinsame Achse)',
        'Position (nicht-ausgerichtet)',
        'Länge',
        'Neigung / Winkel',
        'Fläche',
        'Farbsättigung',
        'Farbton (Hue)',
    ]
    accuracy = [95, 82, 75, 55, 42, 30, 20]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    colors_gradient = plt.cm.RdYlGn(np.linspace(0.15, 0.85, len(encodings)))[::-1]
    bars = ax.barh(encodings[::-1], accuracy[::-1], color=colors_gradient, edgecolor='white', linewidth=1.5, height=0.6)

    for bar, val in zip(bars, accuracy[::-1]):
        ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height() / 2,
                f'{val}%', va='center', fontsize=10, fontweight='bold')

    ax.set_xlim(0, 110)
    ax.set_xlabel('Relative Genauigkeit der Wahrnehmung', fontsize=12)
    ax.set_title('Encoding-Genauigkeit nach Tamara Munzner\n(Welche visuellen Kanäle nehmen wir am präzisesten wahr?)',
                 fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'encoding_accuracy.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ encoding_accuracy.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 4: Warum Nulllinie bei Balken wichtig ist (Do vs. Don't)
# ═══════════════════════════════════════════════════════════════════════════
def chart_zero_baseline():
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [82, 85, 84, 88]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # ❌ Ohne Nulllinie
    axes[0].bar(categories, values, color='#E53935', edgecolor='white', linewidth=1.5)
    axes[0].set_ylim(80, 90)
    axes[0].set_title('❌ FALSCH: Ohne Nulllinie\n(Unterschiede wirken riesig)', fontsize=13, fontweight='bold', color='#C62828')
    axes[0].set_ylabel('Umsatz (Mio CHF)')

    # ✅ Mit Nulllinie
    axes[1].bar(categories, values, color='#43A047', edgecolor='white', linewidth=1.5)
    axes[1].set_ylim(0, 100)
    axes[1].set_title('✅ KORREKT: Mit Nulllinie\n(Realistische Proportionen)', fontsize=13, fontweight='bold', color='#2E7D32')
    axes[1].set_ylabel('Umsatz (Mio CHF)')

    fig.suptitle('Warum Balkendiagramme bei Null starten müssen', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'zero_baseline.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ zero_baseline.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 5: Daten-Typen Übersicht (Categorical vs. Continuous)
# ═══════════════════════════════════════════════════════════════════════════
def chart_data_types():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Titel
    ax.text(5, 6.5, 'Datentypen für Visual Encodings', ha='center', fontsize=16, fontweight='bold')

    # Categorical Box
    rect1 = plt.Rectangle((0.5, 3.5), 4, 2.5, fill=True, facecolor='#E3F2FD', edgecolor=COLORS[0], linewidth=2, zorder=1)
    ax.add_patch(rect1)
    ax.text(2.5, 5.6, 'Kategorisch (Categorical)', ha='center', fontsize=13, fontweight='bold', color=COLORS[0])
    ax.text(2.5, 5.0, '• Nominal: Kartoffel, Banane, Beere…', ha='center', fontsize=10)
    ax.text(2.5, 4.5, '• Ordinal: gross, mittel, klein…', ha='center', fontsize=10)
    ax.text(2.5, 3.9, '→ Encoding: Farbton, Form, Position', ha='center', fontsize=9, style='italic', color='#555')

    # Continuous Box
    rect2 = plt.Rectangle((5.5, 3.5), 4, 2.5, fill=True, facecolor='#FFF3E0', edgecolor=COLORS[1], linewidth=2, zorder=1)
    ax.add_patch(rect2)
    ax.text(7.5, 5.6, 'Kontinuierlich (Continuous)', ha='center', fontsize=13, fontweight='bold', color=COLORS[1])
    ax.text(7.5, 5.0, '• Linear: 0, 10, 20, 30…', ha='center', fontsize=10)
    ax.text(7.5, 4.5, '• Zyklisch: Jan, Feb, Mar…', ha='center', fontsize=10)
    ax.text(7.5, 3.9, '→ Encoding: Position, Länge, Sättigung', ha='center', fontsize=9, style='italic', color='#555')

    # Warning box
    rect3 = plt.Rectangle((1.5, 0.5), 7, 2.2, fill=True, facecolor='#FFF9C4', edgecolor='#F9A825', linewidth=2, zorder=1)
    ax.add_patch(rect3)
    ax.text(5, 2.3, '⚠️ Wichtig: Encoding muss zum Datentyp passen!', ha='center', fontsize=12, fontweight='bold', color='#E65100')
    ax.text(5, 1.7, '• Farbton (Hue) ist NICHT kontinuierlich → nicht für metrische Daten', ha='center', fontsize=10)
    ax.text(5, 1.2, '• Linien verbinden nur geordnete Daten → nie für Kategorien!', ha='center', fontsize=10)
    ax.text(5, 0.7, '• Position auf gemeinsamer Achse ist der genaueste Kanal', ha='center', fontsize=10)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'data_types.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ data_types.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 6: Pie Chart vs. Bar Chart Vergleich (Wahrnehmung)
# ═══════════════════════════════════════════════════════════════════════════
def chart_pie_vs_bar():
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [28, 25, 22, 15, 10]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Pie Chart (schwieriger zu lesen)
    wedges, texts, autotexts = axes[0].pie(values, labels=labels, autopct='%1.0f%%',
                                            colors=COLORS[:5], startangle=90,
                                            textprops={'fontsize': 11})
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    axes[0].set_title('Pie Chart\n(Winkel schwer zu vergleichen)', fontsize=13, fontweight='bold')

    # Bar Chart (leichter zu lesen)
    bars = axes[1].barh(labels[::-1], values[::-1], color=COLORS[:5][::-1], edgecolor='white', linewidth=1.5, height=0.5)
    for bar, val in zip(bars, values[::-1]):
        axes[1].text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                     f'{val}%', va='center', fontsize=11, fontweight='bold')
    axes[1].set_title('Bar Chart\n(Position = genaueste Wahrnehmung)', fontsize=13, fontweight='bold')
    axes[1].set_xlim(0, 35)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)

    fig.suptitle('Wahrnehmungsvergleich: Welcher Chart lässt sich genauer ablesen?', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'pie_vs_bar.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ pie_vs_bar.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 7: Line Chart – Interpolation vs. Schrittweise
# ═══════════════════════════════════════════════════════════════════════════
def chart_line_variants():
    x = np.arange(0, 10)
    y = [3, 5, 4, 7, 6, 8, 7, 9, 8, 10]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Interpolierter Line Chart
    axes[0].plot(x, y, 'o-', color=COLORS[0], linewidth=2, markersize=6)
    axes[0].set_title('Line Chart (interpoliert)\nZeigt Trends', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Zeit'); axes[0].set_ylabel('Wert')

    # Step Chart (dezret)
    axes[1].step(x, y, where='mid', color=COLORS[2], linewidth=2)
    axes[1].plot(x, y, 'o', color=COLORS[2], markersize=6)
    axes[1].set_title('Step Chart (diskret)\nKeine Interpolation', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Zeit'); axes[1].set_ylabel('Wert')

    # ❌ Smooth Line Trap
    from scipy.interpolate import make_interp_spline
    x_smooth = np.linspace(0, 9, 200)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    axes[2].plot(x_smooth, y_smooth, '-', color='#E53935', linewidth=2, label='Geglättet (gefährlich!)')
    axes[2].plot(x, y, 'o', color='#333', markersize=6, zorder=5, label='Echte Datenpunkte')
    axes[2].set_title('❌ Smooth Line Trap!\nSuggeriert falsche Präzision', fontsize=12, fontweight='bold', color='#C62828')
    axes[2].set_xlabel('Zeit'); axes[2].set_ylabel('Wert')
    axes[2].legend(fontsize=9)

    fig.suptitle('Line Chart Varianten: Interpolation richtig einsetzen', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'line_variants.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ line_variants.png')


# ═══════════════════════════════════════════════════════════════════════════
# Chart 8: 4 Guidelines – Übersicht als Infografik
# ═══════════════════════════════════════════════════════════════════════════
def chart_guidelines_overview():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5, 9.5, '4 Guidelines für die Chart-Auswahl', ha='center', fontsize=18, fontweight='bold')

    guidelines = [
        ('1️⃣', 'Daten-Charakteristik', 'Welche Datentypen liegen vor?\nKategorial vs. Kontinuierlich\nLinear vs. Zyklisch', '#E3F2FD', COLORS[0]),
        ('2️⃣', 'Menschliche Wahrnehmung', 'Position > Länge > Winkel > Fläche > Farbe\nUnsere Sinne sind nicht linear!\nGenauigkeit der Kanäle beachten', '#E8F5E9', COLORS[2]),
        ('3️⃣', 'Nutzung & Aufgabe', 'Wie wird der Chart verwendet?\nÜberblick vs. Detail\nTrends vs. exakte Werte', '#FFF3E0', COLORS[1]),
        ('4️⃣', 'Botschaft', 'Was soll kommuniziert werden?\nVergleich, Trend, Teil-vom-Ganzen?\nDie Botschaft bestimmt den Chart-Typ', '#F3E5F5', COLORS[4]),
    ]

    for i, (num, title, desc, bg, color) in enumerate(guidelines):
        y_pos = 7.5 - i * 2.0
        rect = plt.Rectangle((0.5, y_pos - 0.7), 9, 1.7, fill=True, facecolor=bg, edgecolor=color, linewidth=2, zorder=1)
        ax.add_patch(rect)
        ax.text(1.2, y_pos + 0.5, f'{num} {title}', fontsize=14, fontweight='bold', color=color, va='center')
        ax.text(1.4, y_pos - 0.2, desc, fontsize=10, va='center', color='#333', linespacing=1.4)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'guidelines_overview.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('✓ guidelines_overview.png')


# ═══════════════════════════════════════════════════════════════════════════
# Alle Charts generieren
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generiere SW02 Charts...')
    chart_visual_encodings()
    chart_bar_family()
    chart_encoding_accuracy()
    chart_zero_baseline()
    chart_data_types()
    chart_pie_vs_bar()
    chart_line_variants()
    chart_guidelines_overview()
    print('\n✅ Alle Charts generiert!')

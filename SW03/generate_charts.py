"""
Generiert alle Visualisierungen für die DVIZ SW03 Zusammenfassung.
Ausführen: python generate_charts.py
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os

# Ausgabe-Ordner
OUT = os.path.dirname(os.path.abspath(__file__))
WEEK03 = os.path.join(OUT, 'week-03')

# Gemeinsame Farben
C_BLUE = '#2196F3'
C_ORANGE = '#FF5722'
C_GREEN = '#4CAF50'
C_YELLOW = '#FFC107'
C_PURPLE = '#9C27B0'
C_DARK = '#263238'
C_LIGHT = '#ECEFF1'
C_BG = '#FAFAFA'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'figure.facecolor': 'white',
    'axes.facecolor': C_BG,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.spines.top': False,
    'axes.spines.right': False,
})


# ============================================================================
# 1. MATPLOTLIB ARCHITEKTUR – Figure/Axes/Artists Diagramm
# ============================================================================
def chart_architecture():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_facecolor('white')

    # Figure box
    rect_fig = mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 7.2,
                                        boxstyle="round,pad=0.2",
                                        facecolor='#E3F2FD', edgecolor=C_BLUE,
                                        linewidth=2.5)
    ax.add_patch(rect_fig)
    ax.text(5, 7.1, 'Figure (f)', fontsize=16, fontweight='bold',
            color=C_BLUE, ha='center')
    ax.text(5, 6.6, 'plt.subplots() → f, ax', fontsize=10,
            color='#666', ha='center', style='italic')

    # Axes box 1 (main)
    rect_ax1 = mpatches.FancyBboxPatch((0.8, 0.8), 5.2, 5.2,
                                        boxstyle="round,pad=0.15",
                                        facecolor='#FFF3E0', edgecolor=C_ORANGE,
                                        linewidth=2)
    ax.add_patch(rect_ax1)
    ax.text(3.4, 5.6, 'Axes (ax)', fontsize=14, fontweight='bold',
            color=C_ORANGE, ha='center')
    ax.text(3.4, 5.15, 'ax.plot(), ax.scatter(), ...', fontsize=9,
            color='#666', ha='center', style='italic')

    # Artists inside Axes 1
    items_ax1 = [
        ('📏 XAxis / YAxis', 4.5),
        ('📝 Title, Labels', 3.9),
        ('📈 Line2D (Linien)', 3.3),
        ('⭕ PathCollection (Punkte)', 2.7),
        ('🟦 Patch (Balken, Hintergrund)', 2.1),
        ('📐 Spines (Rahmen)', 1.5),
    ]
    for label, y in items_ax1:
        rect = mpatches.FancyBboxPatch((1.2, y - 0.22), 4.4, 0.44,
                                        boxstyle="round,pad=0.08",
                                        facecolor='#E8F5E9', edgecolor=C_GREEN,
                                        linewidth=1)
        ax.add_patch(rect)
        ax.text(3.4, y, label, fontsize=9, ha='center', va='center',
                color=C_DARK)

    # Axes box 2 (second subplot)
    rect_ax2 = mpatches.FancyBboxPatch((6.5, 0.8), 3, 5.2,
                                        boxstyle="round,pad=0.15",
                                        facecolor='#FFF3E0', edgecolor=C_ORANGE,
                                        linewidth=2, linestyle='--')
    ax.add_patch(rect_ax2)
    ax.text(8, 5.6, 'Axes 2', fontsize=14, fontweight='bold',
            color=C_ORANGE, ha='center')
    ax.text(8, 5.15, '(weiterer Subplot)', fontsize=9,
            color='#666', ha='center', style='italic')

    items_ax2 = [
        ('📏 Achsen', 4.5),
        ('📝 Titel', 3.9),
        ('📊 Daten-Artists', 3.3),
        ('📐 Spines', 2.7),
    ]
    for label, y in items_ax2:
        rect = mpatches.FancyBboxPatch((6.8, y - 0.22), 2.4, 0.44,
                                        boxstyle="round,pad=0.08",
                                        facecolor='#E8F5E9', edgecolor=C_GREEN,
                                        linewidth=1, linestyle='--')
        ax.add_patch(rect)
        ax.text(8, y, label, fontsize=9, ha='center', va='center',
                color='#666')

    # Annotations
    ax.annotate('f.get_children()', xy=(5, 6.3), xytext=(8.5, 6.8),
                fontsize=9, color=C_BLUE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=1.5))
    ax.annotate('ax.get_children()', xy=(3.4, 4.8), xytext=(0.5, 6.5),
                fontsize=9, color=C_ORANGE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_ORANGE, lw=1.5))

    fig.suptitle('Matplotlib Architektur: Figure → Axes → Artists',
                 fontsize=16, fontweight='bold', y=0.98)
    fig.savefig(os.path.join(OUT, 'mpl_architecture.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ mpl_architecture.png')


# ============================================================================
# 2. PLT vs AX API – Vergleich
# ============================================================================
def chart_plt_vs_ax():
    np.random.seed(42)
    x = np.array([1, 2, 3, 4])
    y1 = np.array([10, 11, 12, 13])
    y2 = np.array([13, 12, 11, 10])

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # Method 1: OLD (MATLAB) – NOT recommended
    axes[0].plot(x, y1, 'o-', color=C_BLUE, linewidth=2, label='Daten 1')
    axes[0].plot(x, y2, 's--', color=C_ORANGE, linewidth=2, label='Daten 2')
    axes[0].set_title('❌ plt.plot() – MATLAB-Stil\n(nicht empfohlen)', fontsize=11,
                       fontweight='bold', color='#D32F2F')
    axes[0].text(2.5, 9.5, 'plt.subplot(1,2,1)\nplt.plot(x, y)\n→ Implicit "current axis"',
                 fontsize=8, ha='center', style='italic', color='#666',
                 bbox=dict(boxstyle='round', facecolor='#FFEBEE', alpha=0.8))
    axes[0].legend(fontsize=8)

    # Method 2: MIXED – Dangerous
    axes[1].plot(x, y1, 'o-', color=C_BLUE, linewidth=2, label='Daten 1')
    axes[1].plot(x, y2, 's--', color=C_ORANGE, linewidth=2, label='Daten 2')
    axes[1].set_title('⚠️ Mixed – Gefährlich!\n(plt.subplots + plt.plot)', fontsize=11,
                       fontweight='bold', color=C_YELLOW)
    axes[1].text(2.5, 9.5, 'f, axes = plt.subplots()\nplt.plot(x, y)\n→ Alles in LETZTER Axes!',
                 fontsize=8, ha='center', style='italic', color='#666',
                 bbox=dict(boxstyle='round', facecolor='#FFF8E1', alpha=0.8))
    axes[1].legend(fontsize=8)

    # Method 3: OOP – Recommended
    axes[2].plot(x, y1, 'o-', color=C_BLUE, linewidth=2, label='Daten 1')
    axes[2].plot(x, y2, 's--', color=C_ORANGE, linewidth=2, label='Daten 2')
    axes[2].set_title('✅ ax.plot() – Empfohlen!\n(objektorientiert)', fontsize=11,
                       fontweight='bold', color=C_GREEN)
    axes[2].text(2.5, 9.5, 'f, ax = plt.subplots()\nax.plot(x, y)\n→ Explizite Zuordnung!',
                 fontsize=8, ha='center', style='italic', color='#666',
                 bbox=dict(boxstyle='round', facecolor='#E8F5E9', alpha=0.8))
    axes[2].legend(fontsize=8)

    for a in axes:
        a.set_xlabel('x')
        a.set_ylabel('y')

    fig.suptitle('plt vs. ax: Drei API-Stile in Matplotlib',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'plt_vs_ax_api.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ plt_vs_ax_api.png')


# ============================================================================
# 3. LAYOUT BEISPIELE – subplots, subplot_mosaic, inset
# ============================================================================
def chart_layout_examples():
    fig = plt.figure(figsize=(14, 8))

    # --- Panel 1: subplots grid ---
    gs1 = fig.add_gridspec(2, 3, left=0.05, right=0.48, top=0.88, bottom=0.55,
                           wspace=0.3, hspace=0.4)
    colors1 = [C_BLUE, C_ORANGE, C_GREEN, C_YELLOW, C_PURPLE, '#795548']
    for i in range(2):
        for j in range(3):
            ax = fig.add_subplot(gs1[i, j])
            ax.set_facecolor(colors1[i*3+j] + '22')
            ax.text(0.5, 0.5, f'ax[{i},{j}]', transform=ax.transAxes,
                    ha='center', va='center', fontsize=10, fontweight='bold',
                    color=colors1[i*3+j])
            ax.set_xticks([])
            ax.set_yticks([])
    fig.text(0.27, 0.92, 'plt.subplots(nrows=2, ncols=3)',
             fontsize=12, fontweight='bold', ha='center', color=C_DARK)

    # --- Panel 2: subplot_mosaic ---
    gs2 = fig.add_gridspec(3, 3, left=0.55, right=0.98, top=0.88, bottom=0.55,
                           wspace=0.15, hspace=0.15)
    # a: top row, 2 cols
    ax_a = fig.add_subplot(gs2[0, 0:2])
    ax_a.set_facecolor(C_BLUE + '22')
    ax_a.text(0.5, 0.5, "ax['a']", transform=ax_a.transAxes,
              ha='center', va='center', fontsize=10, fontweight='bold', color=C_BLUE)
    ax_a.set_xticks([]); ax_a.set_yticks([])

    # b: right col, all rows
    ax_b = fig.add_subplot(gs2[0:3, 2])
    ax_b.set_facecolor(C_ORANGE + '22')
    ax_b.text(0.5, 0.5, "ax['b']", transform=ax_b.transAxes,
              ha='center', va='center', fontsize=10, fontweight='bold', color=C_ORANGE)
    ax_b.set_xticks([]); ax_b.set_yticks([])

    # c: left, rows 1-2
    ax_c = fig.add_subplot(gs2[1:3, 0])
    ax_c.set_facecolor(C_GREEN + '22')
    ax_c.text(0.5, 0.5, "ax['c']", transform=ax_c.transAxes,
              ha='center', va='center', fontsize=10, fontweight='bold', color=C_GREEN)
    ax_c.set_xticks([]); ax_c.set_yticks([])

    # d: middle
    ax_d = fig.add_subplot(gs2[1, 1])
    ax_d.set_facecolor(C_YELLOW + '22')
    ax_d.text(0.5, 0.5, "ax['d']", transform=ax_d.transAxes,
              ha='center', va='center', fontsize=10, fontweight='bold', color=C_YELLOW)
    ax_d.set_xticks([]); ax_d.set_yticks([])

    # e: bottom middle
    ax_e = fig.add_subplot(gs2[2, 1])
    ax_e.set_facecolor(C_PURPLE + '22')
    ax_e.text(0.5, 0.5, "ax['e']", transform=ax_e.transAxes,
              ha='center', va='center', fontsize=10, fontweight='bold', color=C_PURPLE)
    ax_e.set_xticks([]); ax_e.set_yticks([])

    fig.text(0.77, 0.92, 'plt.subplot_mosaic([...])',
             fontsize=12, fontweight='bold', ha='center', color=C_DARK)

    # --- Panel 3: add_axes / inset_axes ---
    gs3 = fig.add_gridspec(1, 2, left=0.05, right=0.98, top=0.42, bottom=0.05,
                           wspace=0.3)

    ax_main1 = fig.add_subplot(gs3[0])
    np.random.seed(42)
    ax_main1.plot(np.cumsum(np.random.randn(100)), color=C_BLUE, linewidth=2)
    ax_main1.set_title('f.add_axes() – Absolut positioniert', fontsize=11, fontweight='bold')

    # Inset via transAxes trick
    ax_inset1 = ax_main1.inset_axes([0.55, 0.55, 0.4, 0.4])
    ax_inset1.bar([1,2,3], [3,7,5], color=C_ORANGE, edgecolor='white')
    ax_inset1.set_title('Inset', fontsize=8)
    ax_inset1.set_facecolor('#FFF3E0')

    ax_main2 = fig.add_subplot(gs3[1])
    ax_main2.scatter(np.random.rand(30), np.random.rand(30),
                     c=C_GREEN, s=80, alpha=0.6, edgecolors='white')
    ax_main2.set_title('ax.inset_axes() – Relativ zum Parent', fontsize=11, fontweight='bold')

    ax_above = ax_main2.inset_axes([0, 1.08, 1, 0.25])
    ax_above.barh([0,1,2], [5,8,3], color=C_PURPLE, edgecolor='white')
    ax_above.set_yticks([0,1,2])
    ax_above.set_yticklabels(['A','B','C'], fontsize=8)
    ax_above.set_title('Axes darüber', fontsize=8)
    ax_above.set_facecolor('#F3E5F5')

    fig.suptitle('Layout-Methoden in Matplotlib',
                 fontsize=16, fontweight='bold', y=0.99)
    fig.savefig(os.path.join(OUT, 'layout_examples.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ layout_examples.png')


# ============================================================================
# 4. LOLLIPOP CHART – Schritt-für-Schritt Aufbau
# ============================================================================
def chart_lollipop_steps():
    df = pd.read_csv(os.path.join(WEEK03, 'lollipop_data.csv'))

    fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=True)

    # Step 1: nur Punkte
    axes[0].scatter(df['var1'], df['var2'], color=C_BLUE, s=60, zorder=5)
    axes[0].set_title('Schritt 1\nPunkte (scatter)', fontsize=11, fontweight='bold')
    axes[0].set_ylim(0, 900)

    # Step 2: + Stems
    for i in range(len(df)):
        axes[1].plot([df['var1'][i]]*2, [0, df['var2'][i]], color='#999', linewidth=1.5)
    axes[1].scatter(df['var1'], df['var2'], color=C_BLUE, s=60, zorder=5)
    axes[1].set_title('Schritt 2\n+ Stems (plot)', fontsize=11, fontweight='bold')
    axes[1].set_ylim(0, 900)

    # Step 3: + Farbe
    style = {'c': 'darkorange'}
    for i in range(len(df)):
        axes[2].plot([df['var1'][i]]*2, [0, df['var2'][i]], linewidth=2, **style)
    axes[2].scatter(df['var1'], df['var2'], s=80, zorder=5, **style)
    axes[2].set_title('Schritt 3\n+ Style (**style)', fontsize=11, fontweight='bold')
    axes[2].set_ylim(0, 900)

    # Step 4: + Labels
    for i in range(len(df)):
        axes[3].plot([df['var1'][i]]*2, [0, df['var2'][i]], linewidth=2, **style)
    axes[3].scatter(df['var1'], df['var2'], s=80, zorder=5, **style)
    axes[3].set_title('Schritt 4\n+ Titel & Labels', fontsize=11, fontweight='bold')
    axes[3].set_ylim(0, 900)
    axes[3].set_xlabel('Categories')
    axes[3].set_ylabel('Value')

    for a in axes:
        a.grid(axis='y', alpha=0.3)
        a.grid(axis='x', visible=False)

    # Arrows between steps
    for i in range(3):
        fig.text(0.25 + i*0.235, 0.02, '→', fontsize=24, ha='center',
                 color=C_GREEN, fontweight='bold')

    fig.suptitle('Lollipop Chart: Schrittweiser Aufbau',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'lollipop_steps.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ lollipop_steps.png')


# ============================================================================
# 5. KORRELATIONSPLOT
# ============================================================================
def chart_correlation():
    corr_data = pd.read_csv(os.path.join(WEEK03, 'correlation_data.csv'), sep=' ')
    corr_data2 = corr_data.unstack().rename('value').reset_index()
    corr_data2['color'] = corr_data2.apply(
        lambda x: '#D32F2F' if x['value'] <= 0 else C_BLUE, axis=1
    )

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Raw correlation matrix as heatmap
    vars_ = corr_data.columns.tolist()
    matrix = corr_data.values
    im = axes[0].imshow(matrix, cmap='RdBu', vmin=-1, vmax=1, aspect='auto')
    axes[0].set_xticks(range(len(vars_)))
    axes[0].set_yticks(range(len(vars_)))
    axes[0].set_xticklabels(vars_, fontsize=9, rotation=45, ha='right')
    axes[0].set_yticklabels(vars_, fontsize=9)
    # Add text annotations
    for i in range(len(vars_)):
        for j in range(len(vars_)):
            val = matrix[i, j]
            color = 'white' if abs(val) > 0.5 else 'black'
            axes[0].text(j, i, f'{val:.2f}', ha='center', va='center',
                        fontsize=8, color=color, fontweight='bold')
    axes[0].set_title('Korrelationsmatrix\n(Heatmap-Ansicht)', fontsize=12, fontweight='bold')
    plt.colorbar(im, ax=axes[0], shrink=0.8, label='Korrelation')

    # Right: Bubble plot
    axes[1].scatter(
        x=corr_data2['level_0'], y=corr_data2['level_1'],
        s=np.abs(corr_data2['value']) * 800,
        c=corr_data2['color'], alpha=0.7, edgecolors='white', linewidth=1.5
    )
    margin = 0.5
    axes[1].set_ylim(axes[1].get_ylim()[0]-margin, axes[1].get_ylim()[1]+margin)
    axes[1].set_xlim(axes[1].get_xlim()[0]-margin, axes[1].get_xlim()[1]+margin)
    axes[1].set_title('Korrelationsplot\n(Bubble-Ansicht)', fontsize=12, fontweight='bold')

    # Legend
    pos_patch = mpatches.Patch(color=C_BLUE, label='Positive Korrelation')
    neg_patch = mpatches.Patch(color='#D32F2F', label='Negative Korrelation')
    axes[1].legend(handles=[pos_patch, neg_patch], fontsize=9, loc='lower right')
    axes[1].tick_params(axis='x', rotation=45)

    fig.suptitle('Korrelationsdaten: Zwei Darstellungsformen',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'correlation_plot.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ correlation_plot.png')


# ============================================================================
# 6. HISTOGRAMME – 3 Ansätze Vergleich
# ============================================================================
def chart_histogram_comparison():
    np.random.seed(42)
    data_vals = np.concatenate([
        np.random.normal(300, 80, 500),
        np.random.normal(600, 50, 300)
    ])

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)

    # Ansatz 1: Pandas
    pd.Series(data_vals).hist(bins=30, ax=axes[0],
                               color=C_BLUE, edgecolor='white',
                               linewidth=0.8, alpha=0.8)
    axes[0].set_title('Ansatz 1: Pandas\ndf.hist(bins=30)', fontsize=12, fontweight='bold')
    axes[0].text(0.5, 0.92, '✅ Schnell & einfach\n❌ Wenig Kontrolle',
                 transform=axes[0].transAxes, ha='center', fontsize=9,
                 bbox=dict(boxstyle='round', facecolor=C_BLUE+'22', edgecolor=C_BLUE),
                 va='top')

    # Ansatz 2: Seaborn (simulate since we might not have seaborn)
    try:
        import seaborn as sns
        sns.histplot(data_vals, bins=30, kde=True, ax=axes[1],
                     color=C_ORANGE, edgecolor='white', linewidth=0.8, alpha=0.8)
    except ImportError:
        axes[1].hist(data_vals, bins=30, color=C_ORANGE, edgecolor='white',
                     linewidth=0.8, alpha=0.8, density=True)
    axes[1].set_title('Ansatz 2: Seaborn\nsns.histplot(kde=True)', fontsize=12, fontweight='bold')
    axes[1].text(0.5, 0.92, '✅ KDE + Statistik\n✅ Schönes Styling',
                 transform=axes[1].transAxes, ha='center', fontsize=9,
                 bbox=dict(boxstyle='round', facecolor=C_ORANGE+'22', edgecolor=C_ORANGE),
                 va='top')

    # Ansatz 3: NumPy + MPL
    values, bin_edges = np.histogram(data_vals, bins=30)
    barwidth = np.diff(bin_edges[:-1]).mean()
    axes[2].bar(bin_edges[:-1], values, width=barwidth,
                color=C_GREEN, edgecolor='white', linewidth=0.8, alpha=0.8)
    axes[2].set_title('Ansatz 3: NumPy + MPL\nnp.histogram() + ax.bar()', fontsize=12, fontweight='bold')
    axes[2].text(0.5, 0.92, '✅ Volle Kontrolle\n❌ Mehr Code nötig',
                 transform=axes[2].transAxes, ha='center', fontsize=9,
                 bbox=dict(boxstyle='round', facecolor=C_GREEN+'22', edgecolor=C_GREEN),
                 va='top')

    for a in axes:
        a.set_xlabel('Wert')
    axes[0].set_ylabel('Häufigkeit')

    fig.suptitle('Histogramme: 3 Ansätze im Vergleich',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'histogram_comparison.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ histogram_comparison.png')


# ============================================================================
# 7. 2D HISTOGRAMM / HEATMAP
# ============================================================================
def chart_2d_histogram():
    data = pd.read_csv(os.path.join(WEEK03, 'ALB_2020-03.csv'), index_col=[0])

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Method 1: Seaborn
    try:
        import seaborn as sns
        sns.histplot(x=data['DOWNSTREAM']/1e6, y=data['UPSTREAM']/1e6,
                     bins=15, ax=axes[0], cmap='Blues')
    except ImportError:
        axes[0].hist2d(x=data['DOWNSTREAM']/1e6, y=data['UPSTREAM']/1e6,
                       bins=15, cmap='Blues')
    axes[0].set_title('Seaborn\nsns.histplot(x, y)', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Downstream (MB)')
    axes[0].set_ylabel('Upstream (MB)')

    # Method 2: MPL hist2d
    h = axes[1].hist2d(x=data['DOWNSTREAM']/1e6, y=data['UPSTREAM']/1e6,
                       bins=15, cmap='Oranges')
    plt.colorbar(h[3], ax=axes[1], shrink=0.8)
    axes[1].set_title('Matplotlib\nax.hist2d()', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Downstream (MB)')
    axes[1].set_ylabel('Upstream (MB)')

    # Method 3: NumPy + imshow
    H, xedges, yedges = np.histogram2d(
        x=data['DOWNSTREAM']/1e6, y=data['UPSTREAM']/1e6, bins=15
    )
    im = axes[2].imshow(H.T, aspect='auto',
                        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                        origin='lower', cmap='Greens')
    plt.colorbar(im, ax=axes[2], shrink=0.8)
    axes[2].set_title('NumPy + imshow\n⚠️ H.T + origin=lower!', fontsize=12, fontweight='bold')
    axes[2].set_xlabel('Downstream (MB)')
    axes[2].set_ylabel('Upstream (MB)')

    fig.suptitle('2D-Histogramme: 3 Methoden im Vergleich (Internet-Traffic ALB)',
                 fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'heatmap_2d_comparison.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ heatmap_2d_comparison.png')


# ============================================================================
# 8. BAR STYLING OPTIONS
# ============================================================================
def chart_bar_styling():
    cats = ['A', 'B', 'C', 'D']
    vals = [180, 520, 810, 270]

    styles = [
        {'facecolor': C_BLUE, 'edgecolor': 'white', 'linewidth': 1.5, 'alpha': 1.0,
         'label': 'Standard\nfacecolor + edgecolor'},
        {'facecolor': C_ORANGE, 'edgecolor': 'k', 'linewidth': 2, 'alpha': 0.7,
         'label': 'Transparent\nalpha=0.7, edgecolor=k'},
        {'facecolor': '#840128', 'edgecolor': 'k', 'linewidth': 2, 'alpha': 0.5,
         'hatch': '///', 'label': 'Schraffiert\nhatch="///"'},
        {'facecolor': C_GREEN, 'edgecolor': C_DARK, 'linewidth': 1, 'alpha': 0.8,
         'hatch': '...', 'label': 'Gepunktet\nhatch="..."'},
        {'facecolor': C_PURPLE, 'edgecolor': 'white', 'linewidth': 2, 'alpha': 0.9,
         'hatch': 'xx', 'label': 'Gekreuzt\nhatch="xx"'},
    ]

    fig, axes = plt.subplots(1, 5, figsize=(16, 4), sharey=True)

    for ax, s in zip(axes, styles):
        label = s.pop('label')
        ax.bar(cats, vals, **s)
        ax.set_title(label, fontsize=10, fontweight='bold')
        ax.set_ylim(0, 900)

    axes[0].set_ylabel('Wert')

    fig.suptitle('Bar Chart Styling-Optionen: facecolor, edgecolor, alpha, hatch',
                 fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'bar_styling_options.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ bar_styling_options.png')


# ============================================================================
# 9. DASHBOARD BEISPIEL – Kombination aller Techniken
# ============================================================================
def chart_dashboard_example():
    data = pd.read_csv(os.path.join(WEEK03, 'ALB_2020-03.csv'), index_col=[0])
    data['DATE_TIME'] = pd.to_datetime(data['DATE_TIME'])

    fig, ax = plt.subplot_mosaic(
        mosaic=[
            ['hist_top', 'hist_top', '.'],
            ['heatmap', 'heatmap', 'hist_right'],
            ['heatmap', 'heatmap', 'hist_right'],
        ],
        figsize=(10, 8),
        gridspec_kw={'width_ratios': [2, 2, 1], 'height_ratios': [1, 2, 2],
                     'wspace': 0.08, 'hspace': 0.08}
    )

    ds = data['DOWNSTREAM'] / 1e6
    us = data['UPSTREAM'] / 1e6
    nbins = 20

    # Central: 2D histogram
    ax['heatmap'].hist2d(x=ds, y=us, bins=nbins, cmap='YlOrRd')
    ax['heatmap'].set_xlabel('Downstream (MB)', fontsize=10)
    ax['heatmap'].set_ylabel('Upstream (MB)', fontsize=10)

    # Top: Downstream histogram
    ax['hist_top'].hist(ds, bins=nbins, color=C_ORANGE, edgecolor='white',
                        linewidth=0.8, alpha=0.8)
    ax['hist_top'].set_xlim(ax['heatmap'].get_xlim())
    ax['hist_top'].set_xticklabels([])
    ax['hist_top'].set_ylabel('Häufigkeit', fontsize=9)

    # Right: Upstream histogram (horizontal)
    ax['hist_right'].hist(us, bins=nbins, orientation='horizontal',
                          color=C_BLUE, edgecolor='white',
                          linewidth=0.8, alpha=0.8)
    ax['hist_right'].set_ylim(ax['heatmap'].get_ylim())
    ax['hist_right'].set_yticklabels([])
    ax['hist_right'].set_xlabel('Häufigkeit', fontsize=9)

    fig.suptitle('Dashboard: Internet-Traffic Albanien (März 2020)\nErstellt mit plt.subplot_mosaic() + hist + hist2d',
                 fontsize=14, fontweight='bold', y=0.98)
    fig.savefig(os.path.join(OUT, 'dashboard_example.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ dashboard_example.png')


# ============================================================================
# 10. EXPORT-FORMATE Übersicht
# ============================================================================
def chart_export_formats():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)

    formats = [
        {'x': 1.5, 'name': 'PNG', 'ext': '.png', 'color': C_BLUE,
         'pros': 'Universell\nHohe Auflösung\nfür Web & Druck',
         'code': "f.savefig('chart.png',\n  dpi=300,\n  bbox_inches='tight')"},
        {'x': 4, 'name': 'PDF', 'ext': '.pdf', 'color': C_ORANGE,
         'pros': 'Verlustfrei\nIdeal für Reports\nDruckqualität',
         'code': "f.savefig('chart.pdf',\n  bbox_inches='tight')"},
        {'x': 6.5, 'name': 'SVG\n(Outlines)', 'ext': '.svg', 'color': C_GREEN,
         'pros': 'Vektorgrafik\nSkalierbar\nText = Kurven',
         'code': "f.savefig('chart.svg',\n  bbox_inches='tight')"},
        {'x': 9, 'name': 'SVG\n(Text)', 'ext': '.svg', 'color': C_PURPLE,
         'pros': 'Vektorgrafik\nText editierbar!\nFür Figma/AI',
         'code': "with plt.rc_context(\n  {'svg.fonttype':'none'}):\n  f.savefig('c.svg')"},
    ]

    for fmt in formats:
        x = fmt['x']
        # Box
        rect = mpatches.FancyBboxPatch((x-1, 0.4), 2, 4,
                                        boxstyle="round,pad=0.15",
                                        facecolor=fmt['color']+'15',
                                        edgecolor=fmt['color'], linewidth=2)
        ax.add_patch(rect)
        # Title
        ax.text(x, 4, fmt['name'], fontsize=14, fontweight='bold',
                ha='center', va='center', color=fmt['color'])
        # Pros
        ax.text(x, 3, fmt['pros'], fontsize=8.5, ha='center', va='center',
                color=C_DARK, linespacing=1.5)
        # Code
        ax.text(x, 1.3, fmt['code'], fontsize=7, ha='center', va='center',
                color='#555', family='monospace',
                bbox=dict(boxstyle='round', facecolor='#f5f5f5', edgecolor='#ddd'))

    fig.suptitle('Export-Formate: PNG vs. PDF vs. SVG',
                 fontsize=14, fontweight='bold', y=0.98)
    fig.savefig(os.path.join(OUT, 'export_formats.png'),
                dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('✅ export_formats.png')


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print(f'Generiere Charts in: {OUT}\n')
    chart_architecture()
    chart_plt_vs_ax()
    chart_layout_examples()
    chart_lollipop_steps()
    chart_correlation()
    chart_histogram_comparison()
    chart_2d_histogram()
    chart_bar_styling()
    chart_dashboard_example()
    chart_export_formats()
    print(f'\n🎉 Alle {10} Charts generiert!')

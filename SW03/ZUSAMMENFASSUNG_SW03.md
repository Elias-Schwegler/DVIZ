# 📊 DVIZ – Data Visualization for ML and AI

## SW 03 – Matplotlib Layouting, Chart Kombination & Histogramme

**Datum:** 6. März 2026
**Dozentin:** Dr. Teresa Kubacka
**Modul:** I.BA_DVIZ_MM.F2601
**Notebooks:** `01_layouting.ipynb`, `02_ax_vs_plt.ipynb`, `03_combine_charts.ipynb`, `04_histograms.ipynb`

---

## 🎯 Lernziele

Nach dieser Woche kannst du:

- [ ] Die **Matplotlib-Architektur** verstehen: Figure → Axes → Artists (Baumstruktur)
- [ ] **Layouts** erstellen mit `plt.subplots()`, `plt.subplot_mosaic()`, `f.add_axes()` und `ax.inset_axes()`
- [ ] Den Unterschied zwischen dem **alten plt-API** (MATLAB-Stil) und dem **neuen ax-API** (objektorientiert) erklären und anwenden
- [ ] **Charts Schritt für Schritt aufbauen**: Daten laden → Primitive zeichnen → Styling → Export
- [ ] **Lollipop Charts** und **Korrelationsplots** von Hand reproduzieren
- [ ] **Histogramme** mit drei verschiedenen Ansätzen erstellen: Pandas, Seaborn, NumPy+Matplotlib
- [ ] **2D-Histogramme** und **Heatmaps** mit `sns.histplot()`, `ax.hist2d()` und `ax.imshow()` erstellen
- [ ] **Dashboards** aus mehreren Subplots zusammensetzen
- [ ] Charts in verschiedenen Formaten exportieren: PNG, PDF, SVG (mit Textkontrolle)

---

## 🧰 Toolbox – Übersicht

| Tool / Bibliothek    | Zweck                                        | Import                              | Dokumentation                                 |
| -------------------- | -------------------------------------------- | ----------------------------------- | --------------------------------------------- |
| **Matplotlib** | Basis-Bibliothek für alle Plots             | `import matplotlib.pyplot as plt` | [matplotlib.org](https://matplotlib.org)         |
| **Pandas**     | DataFrames + eingebaute `.plot`-Funktionen | `import pandas as pd`             | [pandas.pydata.org](https://pandas.pydata.org)   |
| **NumPy**      | Datenverarbeitung, Histogramm-Berechnung     | `import numpy as np`              | [numpy.org](https://numpy.org)                   |
| **Seaborn**    | Statistische Plots (Histogramme, KDE)        | `import seaborn as sns`           | [seaborn.pydata.org](https://seaborn.pydata.org) |

**Neue Konzepte aus SW03:**

| Konzept                 | Beschreibung                                    | Notebook              |
| ----------------------- | ----------------------------------------------- | --------------------- |
| Figure/Axes-Architektur | Baumstruktur von Matplotlib verstehen           | `01_layouting`      |
| `plt` vs. `ax` API  | Warum immer das objektorientierte API verwenden | `02_ax_vs_plt`      |
| Chart-Reproduktion      | Schritt-für-Schritt Charts nachbauen           | `03_combine_charts` |
| Histogramme (3 Wege)    | Pandas, Seaborn, NumPy+MPL                      | `04_histograms`     |
| 2D-Histogramme          | Heatmaps aus zweidimensionalen Verteilungen     | `04_histograms`     |
| Dashboard-Komposition   | Mehrere Charts in einem Layout kombinieren      | `04_histograms`     |
| SVG-Textrendering       | `svg.fonttype: 'none'` für editierbaren Text | `03_combine_charts` |

**Ressourcen aus SW03:**

| Ressource                    | Typ                     | Link                                                                                   |
| ---------------------------- | ----------------------- | -------------------------------------------------------------------------------------- |
| MPL Axes-Dokumentation       | Offizielle Docs         | [matplotlib.org/axes](https://matplotlib.org/stable/users/explain/axes/index.html)        |
| DataViz Project – Lollipop  | Chart-Vorlage           | [datavizproject.com](https://datavizproject.com/data-type/lollipop-chart/)                |
| MPL Colormaps                | Farbpaletten-Übersicht | [matplotlib.org/colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html) |
| Real Python – kwargs & args | Dict-Unpacking erklärt | [realpython.com](https://realpython.com/python-kwargs-and-args/)                          |

---

## 📐 Konzepte & Theorie

### 1. Matplotlib-Architektur: Figure → Axes → Artists

**Kernidee:** Matplotlib hat eine **hierarchische Baumstruktur**. Jeder Plot besteht aus verschachtelten Objekten:

```
Figure (Leinwand)
├── Axes (Koordinatensystem / Subplot)
│   ├── Patch (Hintergrund-Rechteck)
│   ├── XAxis / YAxis (Achsen)
│   ├── Title, Labels (Text)
│   ├── Line2D, PathCollection, ... (gezeichnete Daten)
│   └── Spines (Rahmenlinien)
├── Axes (weiteres Subplot)
└── ...
```

| Objekt            | Was ist es?                                       | Erstellt mit                          |
| ----------------- | ------------------------------------------------- | ------------------------------------- |
| **Figure**  | Die gesamte Leinwand / das Bild                   | `plt.subplots()` → `f`           |
| **Axes**    | Ein einzelnes Koordinatensystem                   | `plt.subplots()` → `ax`          |
| **Artists** | Alles, was gezeichnet wird (Linien, Punkte, Text) | `ax.plot()`, `ax.scatter()`, etc. |

> **Wichtig:** `f.get_children()` und `ax.get_children()` zeigen die Baumstruktur an! Nützlich zum Debuggen: Was ist eigentlich im Plot?

**Warum das wichtig ist für Projekte:**

- Du musst wissen, **wo** du Eigenschaften setzt (Figure vs. Axes)
- `f.suptitle()` = Titel für *gesamte Figure*, `ax.set_title()` = Titel für *einzelnen Subplot*
- Mehrere Axes in einer Figure = **Dashboard**

---

### 2. plt vs. ax – Zwei APIs, ein Framework

Matplotlib hat historisch **zwei Wege**, Plots zu erstellen:

| API-Stil                                                | Empfehlung                  | Beispiel                                       | Problem                                                     |
| ------------------------------------------------------- | --------------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| **MATLAB-Stil** (`plt.plot()`)                  | ❌**NICHT empfohlen** | `plt.subplot(1,2,1); plt.plot(x,y)`          | Nutzt implizit "current axis" → Fehleranfällig            |
| **"Mixed"** (`plt.subplots()` + `plt.plot()`) | ⚠️ Gefährlich            | `f, axes = plt.subplots(...); plt.plot(...)` | `plt.plot()` zeichnet immer in die **letzte** Axes! |
| **Objektorientiert** (`ax.plot()`)              | ✅**Immer verwenden** | `f, ax = plt.subplots(); ax.plot(x,y)`       | Kein Problem – explizite Zuordnung                         |

> **⚠️ Die "Mixed"-Falle aus dem Notebook:** Wenn du `plt.subplots()` für die Erstellung nutzt, aber dann `plt.plot()` zum Zeichnen → landen alle Daten in der **letzten** Axes, nicht in der gewünschten!

```python
# ❌ FALSCH: plt.plot() zeichnet in die "current axis" (= letzte!)
f, axes = plt.subplots(ncols=2)
for i, ax in enumerate(axes):
    plt.plot(x+i, y)  # Alles landet in axes[1]!

# ✅ RICHTIG: ax.plot() zeichnet genau dort, wo gewünscht
f, axes = plt.subplots(ncols=2)
for i, ax in enumerate(axes):
    ax.plot(x+i, y)  # Jeder Plot in seiner Axes
```

**Merkregel:** Sobald du `f, ax = plt.subplots()` hast → alles über `ax.` machen!

---

### 3. Histogramme – Das richtige Werkzeug wählen

Histogramme zeigen die **Verteilung** einer Variablen. Es gibt drei Ansätze in Python:

| Ansatz                | Methode                           | Vorteile            | Nachteile          |
| --------------------- | --------------------------------- | ------------------- | ------------------ |
| **Pandas**      | `df['col'].hist()`              | Schnell, wenig Code | Wenig Kontrolle    |
| **Seaborn**     | `sns.histplot()`                | KDE, Styling, 2D    | Seaborn-Dependency |
| **NumPy + MPL** | `np.histogram()` + `ax.bar()` | Volle Kontrolle     | Mehr Code          |

> **Aus der Vorlesung:** Verschiedene **Bin-Grössen** zeigen verschiedene Strukturen! Die Wahl der Bins ist ein **analytischer Schritt** – nicht zu viele, nicht zu wenige.

---

### 4. 2D-Histogramme & Heatmaps

Zweidimensionale Verteilungen visualisieren die **gemeinsame Verteilung** zweier Variablen:

| Methode                  | Syntax                                             | Besonderheit                                           |
| ------------------------ | -------------------------------------------------- | ------------------------------------------------------ |
| **Seaborn**        | `sns.histplot(x=..., y=..., bins=10)`            | Am einfachsten, gleiche Funktion wie 1D                |
| **MPL**            | `ax.hist2d(x=..., y=..., bins=10, cmap='Greys')` | Eingebaut,`cmap` direkt                              |
| **NumPy + imshow** | `np.histogram2d()` + `ax.imshow(H.T)`          | Volle Kontrolle, aber**Achtung: Transponieren!** |

> **⚠️ numpy2d-Falle:** `np.histogram2d()` gibt eine Matrix zurück, bei der x entlang der **ersten** Dimension histogrammiert wird. Für `imshow` muss man `H.T` (transponiert) verwenden und `origin='lower'` setzen!

---

## 💻 Code-Baukasten

### 🏗️ Layout erstellen

#### Einfacher Plot (Standard)

```python
import matplotlib.pyplot as plt

# Ein einzelner Plot
f, ax = plt.subplots(figsize=(10, 6))
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title('Mein Plot')
plt.show()
```

#### Grid-Layout mit subplots

```python
# Grid aus 2 Zeilen × 3 Spalten
f, ax = plt.subplots(
    figsize=(10, 3),
    ncols=3, nrows=2,
    # Optionale Parameter:
    # gridspec_kw={'wspace': 0.4},                     # Horizontaler Abstand
    # gridspec_kw={'wspace': 0.4, 'width_ratios': [1,2,1]},  # Unterschiedliche Breiten
    # layout='constrained',                             # Automatisches Layout
    # sharex=True                                       # Gemeinsame x-Achse
)

# Zugriff auf einzelne Axes:
ax[0, 0].plot(...)  # Zeile 0, Spalte 0
ax[1, 2].plot(...)  # Zeile 1, Spalte 2

# Tipp: squeeze=False → ax ist IMMER ein 2D-Array (auch bei 1 Subplot)
f, ax = plt.subplots(squeeze=False)
# ax[0, 0] statt nur ax
```

#### Flexibles Layout mit subplot_mosaic

```python
# Unregelmässiges Layout: 'a' über 2 Spalten, 'b' über 3 Zeilen
f, ax = plt.subplot_mosaic(
    mosaic=[
        ['a', 'a', 'b'],
        ['c', 'd', 'b'],
        ['c', 'e', 'b']
    ]
)

# Zugriff über Keys (Strings!):
ax['a'].plot(...)
ax['b'].bar(...)
ax['c'].scatter(...)

# Leeres Feld mit '.'
mosaic=[
    ['a', 'a', 'b'],
    ['c', '.', 'b'],   # Mitte bleibt leer
    ['c', 'e', 'b']
]
```

#### Axes hinzufügen & verstecken

```python
# Methode 1: f.add_axes() – absolute Position [x0, y0, breite, höhe] (0-1)
f, ax = plt.subplots()
ax_oben = f.add_axes([0, 1.05, 1, 0.25])  # Über dem Hauptplot

# Methode 2: ax.inset_axes() – relative Position zum Parent-Axes
f, ax = plt.subplots()
ax_inset = ax.inset_axes([0, 1.05, 1, 0.25])

# Axes verstecken
f, ax = plt.subplots(nrows=3, ncols=3)
ax[2, 2].set_visible(False)  # Unten rechts ausblenden

# Projektion ändern (Polar, Hammer, etc.)
f, ax = plt.subplots(subplot_kw={'projection': 'polar'})
```

---

### 📊 Lollipop Chart – Schritt für Schritt

Das zentrale Beispiel aus dem Notebook: Eine Chart-Reproduktion von Grund auf.

```python
import matplotlib.pyplot as plt
import pandas as pd

# === Schritt 1: Daten laden ===
df = pd.read_csv('lollipop_data.csv')
# df enthält: var1 (Kategorien A-F), var2 (Werte 180-830)

# === Schritt 2: Style definieren (wiederverwendbar!) ===
style = {'c': 'darkorange'}  # Dict für Unpacking mit **style

# === Schritt 3: Figure & Axes erstellen ===
f, ax = plt.subplots(figsize=(3, 3), dpi=300)

# === Schritt 4: Stems zeichnen (vertikale Linien) ===
for i in range(df.shape[0]):
    ax.plot(
        [df['var1'][i], df['var1'][i]],  # x: gleiche Kategorie zweimal
        [0, df['var2'][i]],              # y: von 0 bis zum Wert
        **style                          # Farbe via Dict-Unpacking
    )

# === Schritt 5: Punkte oben drauf ===
ax.scatter(x=df['var1'], y=df['var2'], **style)

# === Schritt 6: Beschriftungen ===
ax.set_ylim([0, 900])
ax.set_title('The lollipop chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Value')

# === Schritt 7: Exportieren ===
f.savefig('reproduced_lollipop.png', dpi=300, bbox_inches='tight', facecolor='white')
```

> **Pattern:** Style als Dictionary definieren → bei jedem Zeichenbefehl mit `**style` entpacken. So ist das Styling **zentral** und **konsistent**.

---

### 📊 Korrelationsplot – Bubble-Grösse nach Wert

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Daten laden und transformieren
corr_data = pd.read_csv('correlation_data.csv', sep=' ')

# Unstack: Matrix → Long-Format
corr_data2 = corr_data.unstack()\
    .rename('value')\
    .reset_index()

# Farbe basierend auf Vorzeichen
corr_data2['color'] = corr_data2.apply(
    lambda x: 'darkred' if x['value'] <= 0 else 'dodgerblue',
    axis=1
)

# Plot
f, ax = plt.subplots(figsize=(4, 4))
ax.scatter(
    x=corr_data2['level_0'],
    y=corr_data2['level_1'],
    s=np.abs(corr_data2['value']) * 1000,  # Grösse = |Korrelation|
    c=corr_data2['color']                   # Farbe = Vorzeichen
)

# Rand hinzufügen
margin = 0.5
ax.set_ylim(ax.get_ylim()[0] - margin, ax.get_ylim()[1] + margin)
ax.set_xlim(ax.get_xlim()[0] - margin, ax.get_xlim()[1] + margin)
ax.set_title('Correlation plot of gambling data')
```

> **Pattern:** `unstack()` + `reset_index()` ist der Standardweg, um eine Korrelationsmatrix in Long-Format zu bringen → damit kann man sie als Scatter/Bubble plotten.

---

### 📊 Histogramme – 3 Ansätze

#### Ansatz 1: Pandas (schnellster Weg)

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ALB_2020-03.csv', index_col=[0])
data['DATE_TIME'] = pd.to_datetime(data['DATE_TIME'])

# Standard-Histogram mit Pandas
data['DOWNSTREAM'].hist(bins=50, orientation='vertical')

# In bestehendes Axes-Objekt zeichnen
f, ax = plt.subplots(figsize=(3, 1))
data['DOWNSTREAM'].hist(bins=50, ax=ax)

# Styling direkt in Pandas
data['DOWNSTREAM'].hist(
    bins=50,
    color='salmon',
    linewidth=1,
    edgecolor='k',
    grid=False
)

# Bar Chart aus gruppierten Daten
data\
    .groupby(data['DATE_TIME'].dt.day)['DOWNSTREAM']\
    .sum()\
    .plot.bar()
# Rückgabe ist ein Axes-Objekt → weiter anpassbar!
```

#### Ansatz 2: Seaborn (mit Statistik-Features)

```python
import seaborn as sns

# Einfaches Histogramm
sns.histplot(data, x='DOWNSTREAM', bins=10)

# In bestehendes Axes-Objekt
f, ax = plt.subplots(figsize=(3, 1))
sns.histplot(data, x='DOWNSTREAM', bins=10, ax=ax)

# Mit geschätzter Verteilung (KDE)
sns.histplot(data=data, x='DOWNSTREAM', bins=10, kde=True, element="step")

# Rotiertes Histogramm (y statt x!)
sns.histplot(data=data, y='DOWNSTREAM', bins=10, kde=True, element="step")

# Styling
sns.histplot(data, x='DOWNSTREAM', bins=10,
             color='salmon', linewidth=2)
```

#### Ansatz 3: NumPy + Matplotlib (volle Kontrolle)

```python
import numpy as np
import matplotlib.pyplot as plt

# Bins manuell berechnen
nbins = 10
values, bin_edges = np.histogram(data['DOWNSTREAM'], bins=nbins)
# values.shape = (10,), bin_edges.shape = (11,) → 1 Extra-Kante!

# Bar-Breite aus den Bins ableiten
barwidth = np.diff(bin_edges[:-1]).mean()

# Vertikales Histogramm
f, ax = plt.subplots()
ax.bar(x=bin_edges[:-1], height=values, width=barwidth)

# Horizontales Histogramm (x ↔ y tauschen!)
f, ax = plt.subplots()
ax.barh(y=bin_edges[:-1], height=barwidth, width=values)
# ⚠️ Bei barh sind height und width vertauscht!

# Styling
f, ax = plt.subplots()
ax.bar(x=bin_edges[:-1], height=values, width=barwidth,
       linewidth=2, edgecolor='k', facecolor='#840128',
       alpha=0.5, hatch="///")
ax.set_ylim([0, 300])
```

---

### 📊 2D-Histogramm / Heatmap

```python
# === Seaborn (einfachster Weg) ===
sns.histplot(x=data['DOWNSTREAM'], y=data['UPSTREAM'], bins=10)
# Für verschiedene Bin-Anzahlen: bins=(5, 10)
# Farbpalette ändern: cmap='Greys'

# === Matplotlib hist2d ===
f, ax = plt.subplots()
ax.hist2d(x=data['DOWNSTREAM'], y=data['UPSTREAM'],
          bins=10, cmap='Greys')

# === NumPy + imshow (volle Kontrolle) ===
nbins = 10
H, xedges, yedges = np.histogram2d(
    x=data['DOWNSTREAM'], y=data['UPSTREAM'], bins=nbins
)

f, ax = plt.subplots()
ax.imshow(
    H.T,          # ⚠️ TRANSPONIEREN! numpy histogrammiert x entlang Dim 0
    aspect='auto',
    extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
    origin='lower' # ⚠️ Sonst ist das Bild vertikal gespiegelt
)
```

---

### 💾 Export – Formate & Tricks

```python
# PNG mit hoher Auflösung
f.savefig('chart.png', dpi=300, bbox_inches='tight', facecolor='white')

# PDF (verlustfrei, ideal für Berichte)
f.savefig('chart.pdf', bbox_inches='tight')

# SVG – Text als Kurven (Standard)
f.savefig('chart_outlines.svg', bbox_inches='tight')

# SVG – Text als editierbarer Text (für Figma/Illustrator)
with plt.rc_context({'svg.fonttype': 'none'}):
    f.savefig('chart_text.svg', bbox_inches='tight')
```

> **Projekt-Tipp:** Für Poster/Präsentationen SVG mit `svg.fonttype: 'none'` exportieren → Text bleibt in Figma/Illustrator editierbar!

---

## 🎨 Styling & Design-Tipps

### Aus den Notebooks abgeleitete Prinzipien

| Prinzip                    | Erklärung                                             | Umsetzung                                                 |
| -------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| **Style als Dict**   | Styling zentral definieren, nicht überall wiederholen | `style = {'c': 'darkorange'}` → `**style`            |
| **DPI beachten**     | Zu niedrige DPI → Offset/Versatz bei kleinen Figuren  | `dpi=300` für Druck, `dpi=100` für Bildschirm       |
| **figsize anpassen** | Seitenverhältnis beeinflusst Lesbarkeit               | `figsize=(3,3)` für quadratisch, `(10,3)` für breit |
| **Grenzen setzen**   | Automatische Limits sind oft suboptimal                | `ax.set_ylim([0, 900])`                                 |
| **get/set Paare**    | Jede `set_`-Methode hat ein `get_`-Pendant         | `ax.get_ylim()` → `ax.set_ylim()`                    |

### Bar-Chart Styling-Optionen

```python
ax.bar(x, height, width,
       linewidth=2,           # Rahmendicke
       edgecolor='k',         # Rahmenfarbe
       facecolor='#840128',   # Füllfarbe (Hex)
       alpha=0.5,             # Transparenz
       hatch="///")           # Schraffur-Muster
```

**Verfügbare Hatch-Patterns:** `'/'`, `'\\'`, `'|'`, `'-'`, `'+'`, `'x'`, `'o'`, `'O'`, `'.'`, `'*'`

### Farbnamen und Colormaps

```python
# Benannte Farben (Auswahl)
farben = ['darkorange', 'salmon', 'dodgerblue', 'darkred', '#840128']

# Colormaps für 2D-Plots
cmaps = ['Greys', 'viridis', 'plasma', 'inferno', 'cividis']
# Vollständige Liste: https://matplotlib.org/stable/tutorials/colors/colormaps.html
```

---

## 📊 Chart-Typen der Woche

| Chart-Typ                        | Wann verwenden?                           | Python-Funktion                                   | Notebook                             |
| -------------------------------- | ----------------------------------------- | ------------------------------------------------- | ------------------------------------ |
| **Lollipop Chart**         | Werte vergleichen (elegant wie Bar Chart) | `ax.plot()` + `ax.scatter()`                  | `03_combine_charts`                |
| **Korrelationsplot**       | Korrelationsmatrix visualisieren          | `ax.scatter(s=..., c=...)`                      | `03_combine_charts`                |
| **Histogramm (1D)**        | Verteilung einer Variablen                | `df.hist()` / `sns.histplot()` / `ax.bar()` | `04_histograms`                    |
| **Histogramm (2D)**        | Gemeinsame Verteilung zweier Variablen    | `sns.histplot(x, y)` / `ax.hist2d()`          | `04_histograms`                    |
| **Heatmap**                | Werte in einer 2D-Matrix                  | `ax.imshow(H.T, origin='lower')`                | `04_histograms`                    |
| **Bar Chart** (vertikal)   | Kategorische Werte vergleichen            | `ax.bar()`                                      | `04_histograms`                    |
| **Bar Chart** (horizontal) | Viele Kategorien / Ranking                | `ax.barh()`                                     | `04_histograms`                    |
| **Dashboard**              | Mehrere Charts kombiniert                 | `plt.subplot_mosaic()`                          | `01_layouting` + `04_histograms` |

---

## 🔧 Tipps & Tricks

### Häufige Fehler (aus den Notebooks)

| # | Fehler                                          | Warum problematisch?                                                | Lösung                                                    |
| - | ----------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1 | **`plt.plot()` statt `ax.plot()`**    | Zeichnet in die "letzte" Axes, nicht die gewünschte                | Immer `ax.plot()` verwenden                              |
| 2 | **Bar-Breite bei NumPy-Histogramm**       | Default `width=0.8` ist in Datenkoordinaten → unsichtbare Balken | `width=np.diff(bin_edges).mean()`                        |
| 3 | **`np.histogram2d` ohne Transponieren** | Matrix hat x in Dim 0, y in Dim 1 → Bild ist rotiert               | `ax.imshow(H.T, ...)` verwenden                          |
| 4 | **imshow ohne `origin='lower'`**        | Bild ist vertikal gespiegelt (Matrix-Konvention vs. Plot)           | `origin='lower'` setzen                                  |
| 5 | **DPI zu niedrig**                        | Kleine Figuren haben sichtbaren Offset/Versatz                      | `dpi=300` für Export                                    |
| 6 | **SVG ohne Texteinstellung**              | Text wird zu Kurven → nicht editierbar in Vektorsoftware           | `svg.fonttype: 'none'` setzen                            |
| 7 | **bar vs. barh Argumente**                | Bei `barh` sind `height` und `width` vertauscht!              | Docs lesen:`barh(y=..., height=barheight, width=values)` |

### Nützliche Shortcuts

```python
# Typ eines Objekts prüfen
type(ax)          # → matplotlib.axes._axes.Axes
type(f)           # → matplotlib.figure.Figure

# Kinder eines Objekts inspizieren
f.get_children()  # Was ist in der Figure?
ax.get_children() # Was ist in den Axes? (Linien, Patches, etc.)

# Automatische Limits abrufen (bevor man sie anpasst)
print(ax.get_ylim())
print(ax.get_xlim())

# Globale DPI setzen
plt.rcParams['figure.dpi'] = 75  # Nur für die Session

# Figure als Variable behalten (nicht überschreiben!)
fig_lollipop, ax_lollipop = plt.subplots()
fig_histo, ax_histo = plt.subplots()
```

### Pattern: Schrittweiser Chart-Aufbau

```
1. Daten laden und verstehen    → pd.read_csv(), df.head(), df.shape
2. Figure + Axes erstellen      → f, ax = plt.subplots(figsize=..., dpi=...)
3. Style definieren             → style = {'c': 'darkorange', ...}
4. Daten zeichnen               → ax.plot(), ax.scatter(), ax.bar()
5. Limits anpassen              → ax.set_ylim(), ax.set_xlim()
6. Beschriftungen               → ax.set_title(), ax.set_xlabel(), ax.set_ylabel()
7. Exportieren                  → f.savefig('name.png', dpi=300, bbox_inches='tight')
```

---

## 📋 Übungsaufgaben-Zusammenfassung

### Übung 1: Lollipop Chart Reproduktion (Notebook 03)

| Aspekt             | Details                                                                            |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Aufgabe**  | Einen Lollipop Chart vom DataViz Project reproduzieren                             |
| **Daten**    | `lollipop_data.csv` – 6 Kategorien (A–F) mit Werten                            |
| **Schritte** | Daten laden → Scatter für Punkte →`ax.plot()` für Stems → Styling → Export |
| **Gelernt**  | Kombination mehrerer Primitive, Style-Dict mit `**`, schrittweiser Aufbau        |
| **Tools**    | `pd.read_csv()`, `ax.scatter()`, `ax.plot()`, `f.savefig()`                |

### Übung 2: Korrelationsplot (Notebook 03)

| Aspekt             | Details                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Aufgabe**  | Einen Korrelationsplot der Gambling-Daten nachbauen                                         |
| **Daten**    | `correlation_data.csv` – 5×5 Korrelationsmatrix                                         |
| **Schritte** | `unstack()` → Farbe nach Vorzeichen → Scatter mit Grösse = \|Wert\|                    |
| **Gelernt**  | Daten-Transformation (Matrix → Long), Bubble-Grösse als Encoding                          |
| **Tools**    | `pd.unstack()`, `reset_index()`, `lambda`, `np.abs()`, `ax.scatter(s=..., c=...)` |

### Übung 3: Histogramm-Dashboard (Notebook 04)

| Aspekt             | Details                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Aufgabe**  | Ein Dashboard mit 1D-Histogrammen (horizontal + vertikal) und 2D-Heatmap erstellen                             |
| **Daten**    | `ALB_2020-03.csv` – Internet-Transfer-Daten (Downstream/Upstream)                                           |
| **Schritte** | Layout mit `subplot_mosaic` → Histogramme in verschiedenen Achsen → Farbpaletten → `f.suptitle()`       |
| **Gelernt**  | Dashboard-Komposition, 3 Wege für Histogramme, 2D-Histogramme                                                 |
| **Tools**    | `plt.subplot_mosaic()`, `sns.histplot()`, `np.histogram()`, `ax.bar()`, `ax.barh()`, `ax.hist2d()` |

---

## 🔗 Projektrelevanz

### Mini-Projekt (Deadline: 31.03.2026)

| SW03-Konzept                   | Anwendung im Mini-Projekt                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| **Schrittweiser Aufbau** | Reproduziere den Original-Chart Schritt für Schritt – genau wie beim Lollipop           |
| **Style-Dict Pattern**   | Definiere Farben/Stile zentral → konsistente Reproduktion                                |
| **Layout/Subplots**      | Falls der Original-Chart mehrere Teile hat →`subplot_mosaic` nutzen                    |
| **Export**               | PNG (300 dpi) für den Report, SVG für die Präsentation                                 |
| **Histogramme**          | Falls dein Original-Chart Verteilungen zeigt →`sns.histplot()` oder `np.histogram()` |

### Endprojekt (Abgabe: 14.06.2026)

| SW03-Konzept                     | Anwendung im Endprojekt                                   |
| -------------------------------- | --------------------------------------------------------- |
| **Dashboard-Komposition**  | Mehrere Views/Charts in einem Layout →`subplot_mosaic` |
| **Korrelationsplot**       | Feature-Korrelationen im Dataset visualisieren            |
| **2D-Histogramme**         | Joint Distributions von Features analysieren              |
| **Professioneller Export** | SVG mit editierbarem Text für den finalen Report         |

### Aufbau auf vorherige Wochen

| Vorheriges Konzept                   | Vertiefung in SW03                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Visual Encodings (SW02)**    | → Jetzt in Code umgesetzt: Position, Grösse, Farbe als `x`, `s`, `c`               |
| **Chart-Familien (SW02)**      | → Lollipop, Korrelationsplot und Histogramm als neue Typen                                |
| **Encoding-Hierarchie (SW02)** | → Praktisch angewendet: Position (x/y) für Hauptvariablen, Grösse/Farbe für Zusatzinfo |
| **Bar Chart bei Null (SW02)**  | →`ax.set_ylim([0, ...])` explizit gesetzt                                               |
| **Truthful Charts (SW02)**     | → Datentyp-gerechte Darstellung: Histogramm für Verteilungen statt Bar Chart             |

### Vorschau auf kommende Wochen

| SW    | Thema                     | Baut auf SW03 auf durch...                                                     |
| ----- | ------------------------- | ------------------------------------------------------------------------------ |
| SW 04 | Custom Visualizations     | Eigene Chart-Typen mit den Layout-Techniken aus SW03 entwickeln                |
| SW 05 | Styling & Annotations     | `rcParams`, `rc_context` → das Style-System aus SW03 vertiefen            |
| SW 06 | Colors                    | Colormaps und Farbtheorie → die `cmap`-Parameter aus den Heatmaps verstehen |
| SW 07 | Strategies for Complexity | Faceting mit `subplot_mosaic` → das Layout-Wissen aus SW03 erweitern        |

---

## 📚 Quellenverzeichnis

### Vorlesungsmaterialien

- `SW03/week-03/01_layouting.ipynb` – Figure/Axes-Architektur, Layouts
- `SW03/week-03/02_ax_vs_plt.ipynb` – plt vs. ax API-Vergleich
- `SW03/week-03/03_combine_charts.ipynb` – Lollipop Chart + Korrelationsplot
- `SW03/week-03/04_histograms.ipynb` – Histogramme, 2D-Histogramme, Dashboards

### Daten

- `lollipop_data.csv` – Dummy-Daten für den Lollipop Chart (6 Kategorien)
- `correlation_data.csv` – Korrelationsmatrix der Gambling-Daten
- `ALB_2020-03.csv` – Internet-Transfer-Daten (Downstream/Upstream, März 2020)

### Externe Referenzen

- [Matplotlib Axes-Dokumentation](https://matplotlib.org/stable/users/explain/axes/index.html)
- [DataViz Project – Lollipop Chart](https://datavizproject.com/data-type/lollipop-chart/)
- [Matplotlib Colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- [Real Python – kwargs &amp; args](https://realpython.com/python-kwargs-and-args/)
- [SheCanCode – Unpacking Arguments](https://www.shecancode.io/blog/unpacking-function-arguments-in-python)

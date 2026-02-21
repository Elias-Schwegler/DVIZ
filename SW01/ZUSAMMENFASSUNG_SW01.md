# 📊 DVIZ – Data Visualization for ML and AI

## SW 01 – Einführung in Data Visualization

**Datum:** 20. Februar 2026  
**Dozentin:** Dr. Teresa Kubacka  
**Modul:** I.BA_DVIZ_MM.F2601  
**Assistent:** Philipp Meschenmoser (technischer Support)

---

## 🎯 Lernziele

Nach dieser Woche kannst du:

- [ ] Erklären, **was Data Visualization ist** und warum sie ein Akt der Kommunikation ist
- [ ] Den **Comprehension Gap** zwischen Designer und Reader beschreiben (nach Alberto Cairo)
- [ ] Verschiedene **Typologien von Datenvisualisierungen** unterscheiden (simpel vs. komplex, präzise vs. abstrakt, explorativ vs. explanativ, statisch vs. interaktiv)
- [ ] **Irreführende Visualisierungen** erkennen (3D-Pie-Charts, falsche Skalierung, fehlende Nulllinie)
- [ ] Begründen, warum **Daten nie "für sich selbst sprechen"** und Kontext immer notwendig ist
- [ ] Die **Kursstruktur und Projektanforderungen** verstehen (Mini-Projekt + Endprojekt)

---

## 🧰 Toolbox – Übersicht

> **Hinweis:** In SW01 wurden noch keine Python-Tools eingeführt. Die Woche war rein theoretisch. Die folgende Tabelle listet die im Kurs angekündigten Tools, die in späteren Wochen behandelt werden.

| Tool / Bibliothek | Zweck | Import | Dokumentation |
|---|---|---|---|
| Matplotlib | Statische Plots, Basis-Bibliothek | `import matplotlib.pyplot as plt` | [matplotlib.org](https://matplotlib.org) |
| Plotly | Interaktive Visualisierungen | `import plotly.express as px` | [plotly.com](https://plotly.com/python/) |
| Streamlit | Web-basierte Dashboards & Apps | `import streamlit as st` | [streamlit.io](https://streamlit.io) |

**Empfohlene Bücher / Kurse:**

| Buch / Kurs | Autor | Link |
|---|---|---|
| Fundamentals of Data Visualization | Claus Wilke | [clauswilke.com/dataviz](https://clauswilke.com/dataviz/) |
| Visualization Analysis and Design | Tamara Munzner | [O'Reilly](https://learning.oreilly.com/library/view/visualization-analysis-and/9781466508910/) |
| Storytelling with Data | Cole Nussbaumer Knaflic | [O'Reilly](https://learning.oreilly.com/library/view/storytelling-with-data/9781119002253/) |
| The Big Book of Dashboards | Wexler, Shaffer, Cotgreave | [O'Reilly](https://learning.oreilly.com/library/view/the-big-book/9781119282716/) |
| Scientific Visualization (Python & Matplotlib) | Nicolas Rougier | [labri.fr](https://www.labri.fr/perso/nrougier/scientific-visualization.html) |
| Open Visualization Academy | – | [openvisualizationacademy.org](https://openvisualizationacademy.org/) |
| Awesome Matplotlib (GitHub) | Teresa Kubacka | [github.com/paniterka/awesome-matplotlib](https://github.com/paniterka/awesome-matplotlib/) |

---

## 📐 Konzepte & Theorie

### 1. Was ist Data Visualization?

**Definition:** Darstellung von Daten in visueller Form – und gleichzeitig ein **Akt der Kommunikation**.

Die fünf Kernfragen:
| Frage | Antwort |
|---|---|
| Was sind Daten? | Unsere Messung/Repräsentation der Realität |
| Was ist eine visuelle Form? | Etwas, das unsere Sinne wahrnehmen können |
| Wer stellt dar? | Ein Mensch wählt aus, was wichtig ist |
| Wer liest? | Ein Mensch interpretiert, was er sieht |
| Warum? | Es gab ein Bedürfnis zu kommunizieren |

> **Kernaussage:** Als Data Professionals bauen wir ständig Brücken zwischen Daten und Menschen.

---

### 2. Warum Data Visualization?

| Argument | Erklärung |
|---|---|
| **Kein "Data Sense"** | Menschen sind sehr gut im Erkennen visueller Muster, aber schlecht darin, abstrakte Zahlen intuitiv zu verstehen |
| **Summaries verlieren Information** | Gleiche statistische Kennzahlen können völlig unterschiedliche Daten beschreiben → "The Datasaurus" |
| **Kontext ist nötig** | Zahlen allein reichen nicht – der Kontext bestimmt die Interpretation (David McCandless) |
| **Historische Bedeutung** | Dataviz hat buchstäblich Leben gerettet (John Snow's Cholera-Karte, 1854) |

---

### 3. Der Comprehension Gap (Alberto Cairo)

```
Designer                              Reader
   │                                    │
   ├─ Eigene Mental Models              ├─ Eigene Mental Models
   ├─ Wählt Symbole, Encodings          ├─ Rekonstruiert die Botschaft
   ├─ Fügt Annotationen hinzu           ├─ Beobachtet die Visualisierung
   │                                    │
   └──────── Visualization ─────────────┘
```

**Wichtig für Projekte:**
- Designer und Reader haben **unterschiedliche mentale Modelle**
- Niemand wird mit der Fähigkeit geboren, ein Balkendiagramm zu lesen!
- Besonders herausfordernd bei: komplexen Themen, unüblichen Chart-Typen, nicht-fachkundiger Zielgruppe, Unsicherheit/Wahrscheinlichkeit

> **Praxis-Tipp:** Hole immer Feedback von der Zielgruppe ein. "Die User sind NICHT zu dumm" – es liegt am Design!

---

### 4. Typologien von Datenvisualisierungen

| Dimension | Pol A | Pol B | Beispiel |
|---|---|---|---|
| Komplexität | Simpel (einzelner Chart) | Komplex (Dashboard, Multi-Chart) | Bar Chart vs. Infographic |
| Präzision | Sehr präzise (exakte Werte) | Sehr abstrakt (Trends, Muster) | Datentabelle vs. Data Art |
| Zweck | **Explorativ** (Muster finden) | **Explanativ** (Geschichte erzählen) | Jupyter-Analyse vs. Präsentation |
| Interaktivität | Statisch | Interaktiv | PDF-Report vs. Dashboard |

**Für dein Projekt:** Überlege dir, wo deine Visualisierung auf dieser Matrix liegt:
- **"Data Story"** → explanativ, eher statisch, erzählt eine Geschichte
- **"Visual Analytics"** → explorativ, eher interaktiv, ermöglicht Analyse

---

### 5. Truthful Charts – Ehrliche Visualisierungen

#### ❌ Don'ts – Häufige Manipulationen

| Fehler | Problem | Beispiel |
|---|---|---|
| **3D-Pie-Charts** | Perspektive verzerrt die Grössenverhältnisse | Steve Jobs' iPhone-Marktanteile: 21.2% und 19.5% sehen gleich gross aus |
| **Falsche Skalierung** | Achsen-Skalierung beeinflusst die wahrgenommene Veränderung | Temperaturkurve mit voller Y-Achse vs. Ausschnitt → komplett unterschiedlicher Eindruck |
| **Balken ohne Nulllinie** | Unterschiede werden dramatisch übertrieben | Kleine Änderungen sehen nach riesigen Sprüngen aus |
| **Irreführende Chart-Typen** | Falscher Chart-Typ verstärkt eine verzerrte Botschaft | viz.wtf zeigt viele reale Beispiele |

#### ✅ Do's

| Prinzip | Beschreibung |
|---|---|
| **Zielgruppe verstehen** | Wer liest die Visualisierung? Was erwarten sie? |
| **Aufgabe verstehen** | Welche Aktion soll die Visualisierung auslösen? |
| **Feedback einholen** | Testen oder die Zielgruppe um Rückmeldung bitten |
| **Reader unterstützen** | Annotationen, Labels, Legenden hinzufügen |
| **Kontext liefern** | Daten sprechen nie für sich selbst |

---

### 6. "Data never speaks for itself"

Zentrale Erkenntnis der Woche:
- Daten sind **kein Teil der Natur** – Menschen sammeln sie mit einem Zweck
- Jede Datenerhebung basiert auf unserem **Verständnis der Welt**
- Data Storytelling bedeutet, **unser Verständnis zu teilen** und einen Dialog zu führen
- Unterschiedliche Rollen (Data Scientist, Manager, Enduser) brauchen **unterschiedliche Visualisierungen** derselben Daten

**Inspirations-Talks:**
- [Group-by statements that save the day – Vincent D Warmerdam](https://www.youtube.com/results?search_query=vincent+warmerdam+group+by)
- [Finding Humanity in Data – Giorgia Lupi](https://www.youtube.com/results?search_query=giorgia+lupi+finding+humanity+in+data)
- [The era of blind faith in big data must end – Cathy O'Neil](https://www.youtube.com/results?search_query=cathy+oneil+big+data+ted)

---

## 💻 Code-Baukasten

> **Hinweis:** In SW01 gab es keine Jupyter Notebooks und keinen Code. Die folgenden Snippets sind ein **Vorbereitungs-Setup** für die kommenden Wochen, basierend auf den im Kurs genannten Tools.

### 🔧 Python-Umgebung einrichten

```python
# Grundlegende Bibliotheken installieren (Terminal/Anaconda Prompt)
# pip install matplotlib seaborn plotly pandas numpy streamlit

# Standard-Imports für DVIZ-Projekte
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Optionale Imports (werden in späteren Wochen eingeführt)
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st
```

### 📊 Erster Test-Plot (Matplotlib Grundgerüst)

```python
import matplotlib.pyplot as plt
import numpy as np

# Daten generieren
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Figure und Axes erstellen (empfohlene OOP-Methode)
fig, ax = plt.subplots(figsize=(10, 6))

# Plot zeichnen
ax.plot(x, y, color='#2196F3', linewidth=2, label='sin(x)')

# Beschriftungen hinzufügen (immer machen!)
ax.set_title('Beispiel: Sinus-Funktion', fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.legend()

# Grid für bessere Lesbarkeit
ax.grid(True, alpha=0.3)

# Layout optimieren und anzeigen
fig.tight_layout()
plt.show()
```

### 💾 Plot speichern (für Projekte wichtig!)

```python
# Plot als PNG speichern (hohe Auflösung für Reports)
fig.savefig('mein_plot.png', dpi=300, bbox_inches='tight', facecolor='white')

# Plot als SVG speichern (Vektorgrafik, skalierbar)
fig.savefig('mein_plot.svg', bbox_inches='tight', facecolor='white')

# Plot als PDF speichern (für Berichte)
fig.savefig('mein_plot.pdf', bbox_inches='tight', facecolor='white')
```

---

## 🎨 Styling & Design-Tipps

> In SW01 wurden noch keine konkreten Styling-Techniken behandelt. Die folgenden Tipps basieren auf den **Prinzipien der Woche**:

### Aus den Vorlesungsfolien abgeleitete Prinzipien:

| Prinzip | Umsetzung |
|---|---|
| **Zielgruppe zuerst** | Bevor du einen Chart designst: Wer wird ihn lesen? Was ist deren Vorwissen? |
| **Funktion vor Form** | Ein schöner Chart, der nicht verstanden wird, ist wertlos ("Carelman's Teapot") |
| **Keine 3D-Pie-Charts** | Verwende stattdessen horizontale Bar Charts oder einfache Pie Charts (2D) |
| **Nulllinie bei Balken** | Balkendiagramme immer bei 0 starten lassen |
| **Kontext immer mitliefern** | Titel, Achsenbeschriftungen, Quellangaben, Annotationen |
| **Feedback einholen** | Zeige deine Visualisierung einer Testperson, bevor du sie präsentierst |

---

## 📊 Chart-Typen der Woche

> In SW01 wurden keine spezifischen Chart-Typen gelehrt. Die folgenden wurden als **Beispiele erwähnt**:

| Chart-Typ | Kontext in SW01 | Anmerkung |
|---|---|---|
| Pie Chart (3D) | Negativ-Beispiel (Steve Jobs) | Vermeiden! Perspektive verzerrt Proportionen |
| Bar Chart | Negativ-Beispiel (fehlende Nulllinie) | Immer bei 0 starten |
| Confusion Matrix | 3 verschiedene Darstellungen verglichen | Gleiche Daten, unterschiedliche Designs für unterschiedliche Zielgruppen |
| Karten (Maps) | John Snow's Cholera-Karte | Historisches Beispiel für lebensrettende Dataviz |
| Sparklines | Edward Tufte's Konzept | Minimale Charts eingebettet in Text |
| Dashboards | Historisch (Schweiz 1897) und modern | Komplex, multi-chart |

---

## 🔧 Tipps & Tricks

### Kursorganisation

| Aspekt | Details |
|---|---|
| **Bewertung** | Kein Examen! 10% Mini-Projekt + 50% Endprojekt + 40% Report |
| **Mini-Projekt** | Reproduktion einer Visualisierung mit Matplotlib, Deadline: 31.03.2026 |
| **Endprojekt** | Teams + Themen bis 17.04.2026, Präsentation 29.05.2026, Abgabe 14.06.2026 |
| **Sprache** | Englisch (Kurssprache), Report auf Englisch |
| **KI-Nutzung** | Erlaubt, aber: zuerst Basics lernen, dann mit KI optimieren. Vorsicht vor halluzinierten Zahlen! |
| **Support** | Philipp Meschenmoser: philipp.meschenmoser@hslu.ch |

### Häufige Fehler (aus den Slides)

1. **"Die User sind zu dumm"** → Nein! Es liegt am Design, nicht am User
2. **"Daten sprechen für sich"** → Niemals! Kontext ist immer nötig
3. **"Hauptsache schön"** → Ästhetik allein reicht nicht, die Visualisierung muss **funktional** sein
4. **3D-Effekte verwenden** → Verzerren die Wahrnehmung, vermeiden!
5. **Achsenskalierung ignorieren** → Kann zu komplett falschen Schlussfolgerungen führen

### Nützliche Ressourcen

- **Schlechte Beispiele finden:** [viz.wtf](https://viz.wtf/) – Galerie von schlechten/lustigen Visualisierungen
- **Gute Beispiele finden:** [Information is Beautiful Awards](https://www.informationisbeautifulawards.com/)
- **Historische Dataviz:** [chartography.net](https://www.chartography.net/) (RJ Andrews)
- **Datasaurus:** [Same Stats, Different Graphs](https://www.autodesk.com/research/publications/same-stats-different-graphs)

---

## 📋 Übungsaufgaben-Zusammenfassung

### Übung 1: Boeing 737 Zeichnung (In-Class)
| Aspekt | Details |
|---|---|
| **Aufgabe** | Vereinfachte Zeichnung eines Boeing 737 erstellen (5 Min) |
| **Ziel** | Verstehen, dass verschiedene Menschen unterschiedliche Aspekte betonen |
| **Diskussion** | Wie ändert sich die Zeichnung je nach Zielgruppe? (Kind ↔ Ingenieur ↔ Chef) |
| **Kernlektion** | Visualisierung hängt immer vom **Zweck** und der **Zielgruppe** ab |

### Übung 2: Confusion Matrix Vergleich (In-Class)
| Aspekt | Details |
|---|---|
| **Aufgabe** | 3 unterschiedliche Confusion-Matrix-Darstellungen vergleichen |
| **Quellen** | Chatbot-Training (aiaibot), medizinischer Test (BMJ), Versicherung (Jack the Checker) |
| **Diskussion** | Welche Aktion ermöglicht jeder Chart? Wie unterstützen visuelle Elemente die Aufgabe? |
| **Kernlektion** | Gleiche Daten, unterschiedliche Designs → **die Zielgruppe bestimmt das Design** |

### Übung 3: Good, Bad & Ugly (Homework)
| Aspekt | Details |
|---|---|
| **Aufgabe** | Eine gute und eine schlechte/hässliche Datenvisualisierung finden |
| **Für gute Beispiele fragen** | Wer ist die Zielgruppe? Woher kommen die Daten? Was macht sie gut? |
| **Für schlechte Beispiele fragen** | Was ist falsch/hässlich? Wie könnte man es verbessern? |
| **Abgabe** | Links und Gedanken im Forum teilen |
| **Material** | Quellen aus der Projektbeschreibung durchstöbern |

---

## 🔗 Projektrelevanz

### Direkte Anwendung im Mini-Projekt
- **Zielgruppe definieren:** Bevor du beginnst – für wen ist die Reproduktion?
- **Original analysieren:** Welche visuellen Elemente machen das Original effektiv?
- **Comprehension Gap minimieren:** Achte darauf, dass deine Reproduktion die gleiche Botschaft vermittelt

### Direkte Anwendung im Endprojekt
- **Projekttyp bestimmen:** Ist dein Projekt eine "Data Story" oder "Visual Analytics"?
  - Data Story → explanativ, statisch, erzählt eine Geschichte
  - Visual Analytics → explorativ, interaktiv, ermöglicht Analyse
- **Truthful Charts:** Alle Visualisierungen im Projekt müssen ehrlich und korrekt sein
- **Kontext liefern:** Titel, Beschriftungen, Quellangaben sind Pflicht
- **Verschiedene Perspektiven:** Bedenke, dass verschiedene Stakeholder dein Projekt unterschiedlich lesen

### Aufbau für spätere Wochen

| SW | Thema | Baut auf SW01 auf durch... |
|---|---|---|
| SW 02 | Visual Encodings & Kognition | Vertiefung des Comprehension Gap → wie nehmen Menschen visuell wahr? |
| SW 03 | Chart Types | Konkrete Umsetzung der Typologien → welcher Chart für welchen Zweck? |
| SW 05 | Styling & Annotations | Kontext liefern → konkrete Techniken für Labels und Design |
| SW 06 | Colors | Truthful Charts → wie Farben Wahrnehmung beeinflussen |

---

## 📚 Quellenverzeichnis

### Vorlesungsmaterialien
- `Slides/intro.pdf` – Kurseinführung und Organisation (22 Seiten)
- `Slides/week-01.pdf` – Einführung in Data Visualization (64 Seiten)
- `Course Overview/Overview.txt` – Kursüberblick und Semesterplan

### Externe Referenzen (aus den Slides)
- Alberto Cairo – "How Charts Lie"
- The Datasaurus: [autodesk.com](https://www.autodesk.com/research/publications/same-stats-different-graphs)
- John Snow's Cholera Map: [openculture.com](https://www.openculture.com/2019/07/the-1855-map-that-revolutionized-disease-prevention-data-visualization.html)
- Minard's Napoleon March: [openculture.com](https://www.openculture.com/2019/07/napoleons-disastrous-invasion-of-russia-explained-in-an-1869-data-visualization.html)
- viz.wtf: [viz.wtf](https://viz.wtf/)
- Information is Beautiful Awards: [informationisbeautifulawards.com](https://www.informationisbeautifulawards.com/)

> **Hinweis:** Für SW01 waren keine Jupyter Notebooks verfügbar. Der Code-Baukasten enthält vorbereitende Setup-Snippets für die kommenden Wochen.

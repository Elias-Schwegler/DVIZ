# 🤖 DVIZ Wochen-Zusammenfassung – Prompt-Template

> **Zweck:** Diesen Prompt bei jeder neuen Semesterwoche verwenden, damit der Agent automatisch eine **Toolbox-Zusammenfassung** für **Data Visualization (DVIZ, HSLU)** erstellt.  
> **Kein Prüfungsmodul** – das Ziel sind zwei Projekte. Die Zusammenfassungen dienen als **Baukasten / Nachschlagewerk**, um die gelernten Tools, Techniken und Konzepte direkt in den Projekten einzusetzen.

---

## Prompt (Copy-Paste für jede neue Woche)

```
Erstelle eine praxisorientierte Toolbox-Zusammenfassung für die aktuelle Semesterwoche (SW XX) des Moduls "Data Visualization" (DVIZ, HSLU).

Das Ausgabeformat ist ein Markdown-File namens ZUSAMMENFASSUNG_SWXX.md im entsprechenden SW-Ordner.

### Quelldateien im Wochenordner:
- **Slides/** → Vorlesungsfolien (PDF/PPTX)
- **Notebooks/** → Jupyter Notebooks (.ipynb) mit Code-Beispielen und Übungen
- **Recordings/** → Aufzeichnungen (nicht inhaltlich relevant, nur als Referenz)
- Weitere Dateien je nach Woche (Datasets, Bilder, etc.)

Alle Dateien durchlesen und Inhalte integrieren.

### Struktur & Inhalt (in dieser Reihenfolge):

1. **Header**: Modulname (DVIZ), Wochennummer (SW XX), Thema
2. **🎯 Lernziele**: Was wurde in dieser Woche behandelt? Was soll man danach können?
3. **🧰 Toolbox – Übersicht**: Kompakte Tabelle aller in dieser Woche eingeführten/verwendeten Tools und Bibliotheken:
   | Tool / Bibliothek | Zweck | Import | Dokumentation |
   |---|---|---|---|
   | z.B. matplotlib | Statische Plots | `import matplotlib.pyplot as plt` | [Link](https://matplotlib.org) |
4. **📐 Konzepte & Theorie**: Die wichtigsten Visualisierungs-Konzepte der Woche:
   - Kernkonzept mit Erklärung (z.B. Visual Encodings, Gestalt-Prinzipien, Farbtheorie)
   - Warum ist das wichtig für die Projektarbeit?
   - Dos & Don'ts mit konkreten Beispielen
5. **💻 Code-Baukasten**: Die wichtigsten Code-Patterns aus den Notebooks, **direkt wiederverwendbar**:
   - Jedes Pattern mit Titel, kurzer Beschreibung und vollständigem Code-Snippet
   - Copy-Paste-ready für eigene Projekte
   - Kommentare auf Deutsch im Code
   - Varianten und Anpassungsmöglichkeiten aufzeigen
   - Gruppierung nach Aufgabentyp (z.B. "Daten laden", "Plot erstellen", "Styling", "Export")
6. **🎨 Styling & Design-Tipps**: Konkrete Tipps für professionelle Visualisierungen:
   - Farb-Paletten, Schriftarten, Layouts
   - Annotationen und Labels
   - Best Practices aus den Vorlesungsfolien
7. **📊 Chart-Typen der Woche**: Übersicht der behandelten Diagrammtypen:
   | Chart-Typ | Wann verwenden? | Python-Funktion | Beispiel-Usecase |
   |---|---|---|---|
   | z.B. Scatter Plot | Korrelation zweier Variablen | `plt.scatter()` / `sns.scatterplot()` | Feature-Analyse in ML |
8. **🔧 Tipps & Tricks**: Nützliche Shortcuts, häufige Fehler, Performance-Tipps
9. **📋 Übungsaufgaben-Zusammenfassung**: Was wurde in den Notebooks geübt?
   - Aufgabe, Lösungsansatz, eingesetzte Tools
10. **🔗 Projektrelevanz**: Wie lassen sich die Inhalte dieser Woche konkret im Projekt einsetzen?
    - Mögliche Anwendungen im Zwischen- und Endprojekt
    - Kombination mit Tools aus vorherigen Wochen

### Wichtige Regeln:
- **Sprache:** Deutsch (Fachbegriffe und Code dürfen Englisch bleiben)
- **Code:** Ausschliesslich Python (matplotlib, seaborn, plotly, altair, etc.)
- **Quellen:** Alle Dateien im SW-Ordner durchlesen (Slides, Notebooks, Daten)
- **Code-Formatierung:** Python-Syntax-Highlighting in Markdown verwenden (```python)
- **Praxisfokus:** Jedes Code-Snippet soll direkt in einem Projekt wiederverwendbar sein
- **Emojis** als Section-Icons verwenden für schnelles Scannen
- **Tabellen** bevorzugen für Vergleiche und Tool-Übersichten
- **Kein Prüfungsfokus** – es geht um Projekte! Die Zusammenfassung ist ein Baukasten/Nachschlagewerk
- Das File soll so vollständig sein, dass man damit die Projekt-Aufgaben lösen kann
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für Querverweise und Tool-Übersicht
```

---

## Themenübersicht pro Woche

| Woche | Datum | Thema | Schlüssel-Tools & -Konzepte |
|-------|-------|-------|----------------------------|
| SW 01 | 20.02 | Einführung Data Visualization | Überblick, Motivation, Python-Setup |
| SW 02 | 27.02 | Visual Encodings & Human Cognition | Visuelle Kanäle, Wahrnehmung, Gestalt-Prinzipien |
| SW 03 | 06.03 | Chart Types & Choosing Charts | Diagrammtypen, Entscheidungshilfen, matplotlib/seaborn |
| SW 04 | 13.03 | Custom Visualizations | Eigene Visualisierungen entwickeln |
| SW 05 | 20.03 | Styling, Annotations & Graphical Design | Professionelles Styling, Annotationen |
| SW 06 | 27.03 | Colors | Farbtheorie, Paletten, Accessibility |
| SW 07 | 10.04 | Strategies for Complexity | Grosse Datenmengen, Faceting, Aggregation |
| SW 08 | 17.04 | Interactive Visualizations | Plotly, Widgets, Interaktivität |
| SW 09 | 24.04 | Survey of Python Tools | Tool-Vergleich, Altair, Bokeh, etc. |
| SW 10 | 01.05–15.05 | Web-basierte Visualisierung | D3.js-Grundlagen, Dashboards |
| SW 11 | 01.05–15.05 | Dimensionality Reduction | t-SNE, PCA, UMAP für Visualisierung |
| SW 12 | 22.05 | Gastvorlesung | Praxiseinblick |
| SW 13 | 29.05 | Projektpräsentationen & Peer-Feedback | Abschluss |

> **Hinweis:** Die Themen oben sind vorläufig basierend auf dem Semester Outline. Bitte anhand der tatsächlichen Materialien im jeweiligen Ordner verifizieren und anpassen.

---

## Ordnerstruktur-Erwartung

```
DVIZ/
├── Slides/                    (Vorlesungsfolien, nach Woche sortiert)
├── Notebooks/                 (Jupyter Notebooks mit Code & Übungen)
├── Recordings/                (Aufzeichnungen der Vorlesungen)
├── Course Overview/
│   └── Overview.txt
├── SW01/
│   ├── [Materialien der Woche]
│   └── ZUSAMMENFASSUNG_SW01.md  ← Output
├── SW02/
│   └── ZUSAMMENFASSUNG_SW02.md  ← Output
├── ...
└── Prompt.md  ← Diese Datei
```

> Falls die Wochenordner noch nicht existieren, bitte anlegen.

---

## Hinweise für den Agent

- Zuerst den **SW-Ordner** der aktuellen Woche auslesen (oder anlegen falls nötig)
- **Slides** und **Notebooks** sind die Hauptquellen
- **Jupyter Notebooks** direkt lesen – Code-Zellen sind besonders wichtig
- **Fokus auf Wiederverwendbarkeit**: Jedes Code-Snippet soll als Baustein für Projekte dienen
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für **Querverweise** und kumulativen Tool-Überblick
- **Projektbezug** immer herstellen: Wie kann man das Gelernte im Projekt einsetzen?
- **Tool-Dokumentation**: Für jedes neue Tool einen kompakten Steckbrief erstellen (Import, Hauptfunktionen, Beispiel)
- **Keine Prüfungsrelevanz** – das Modul wird über Projekte bewertet
- Bei fehlenden Materialien dies vermerken und Platzhalter für spätere Ergänzung lassen

### PDF-Dateien lesen (Slides)

Da PDFs nicht direkt mit `view_file` gelesen werden können, verwende **PyMuPDF** (`fitz`) um den Text zu extrahieren. Das Paket ist bereits installiert (`pip install pymupdf`). Siehe auch `How to read PDF.md` im Root-Ordner.

**Vorgehen:**
1. Python-Script `Slides/extract_pdf.py` nutzen (bereits vorhanden)
2. Aufruf: `python Slides/extract_pdf.py "Pfad/zur/Datei.pdf" "Pfad/zur/Ausgabe.txt"`
3. Die generierte `.txt`-Datei mit `view_file` lesen
4. **Temporäre `.txt`-Dateien nach dem Lesen löschen!**

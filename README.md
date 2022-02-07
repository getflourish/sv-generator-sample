# RIP: Eine «Small Victories» Webseite wiederbeleben

## Was war Small Victories?

Small Victories war ein Service mit welchem wir einfache Webseiten mit Markdown erstellen konnten. Dazu haben wir uns einen Dropbox Account eingerichtet und diesen mit Small Victories verbunden. Bei Änderungen in Dropbox hat Small Victories automatisch eine aktualisierte Webseite generiert.
Einfach gesagt war Small Victories ein sogenannter «Static Site Generator». Das heisst: aus HTML Templates, CSS und Markdown wurden statische HTML-Dateien generiert, die dann zu einer Webseite (mit Links zwischen den Seiten) zusammengesetzt wurden.

## Problem: Small Victories is dead

Da Small Victories nicht mehr existiert, sind unsere Webseite erstmal stillgelegt. Da wir jedoch etwas Python gelernt haben und HTML und CSS kennen, können wir uns ein kleine Script schreiben, mit dem wir die Webseite generieren wiederbeleben können. Es ist zawr nicht mehr so bequem, aber dafür haben wir etwas mehr Kontrolle über Design und Hosting.

## Das Python Skript

Die Lösung ist ein Python Skript (es könnte auch eine andere Programmiersprache sein, aber Python ist auf macOS vorinstalliert). Das Skript macht in etwa folgendes:

1. Alle Markdown-Dateien im Ordner lesen
2. Eine Navigation mit Links zu allen Seiten generieren (for-loop, HTML String mit Links generieren, …)
3. Markdown in HTML umwandeln
4. Für jede Seite: Titel, Navigation und Inhalt im Template ersetzen («Find and Replace»)
5. HTML Dateien im Zielordner (`dist`) speichern

## Vorbereitung

Um eine Webseite auf Basis von Small Victories zu generieren benötigen wir einen Ordner mit Markdown Dateien. Wir können diesen neu anlegen oder aus einer bestehenden Small Victories Ordner zusammenkopieren.

So sieht ein Small Victories-Ordner aus:

```
config.yml
_posts
404.html
about.markdown
Gemfile
index.markdown
…
```

Da sind allerdings einige Dateien drin, die wir nicht mehr benötigen. Was wir benötigen ist ein Ordner mit dem folgenden Aufbau:

```
/dist
/dist/_sv_custom.css
/dist/_sv_custom.js
/dist/fonts/...
/dist/links/...
_template.html
01_Erste_Seite.md
02_Zweite_Seite.md
…
index.md

```

<img width="849" alt="Bildschirmfoto 2022-02-07 um 16 47 44" src="https://user-images.githubusercontent.com/183989/152822207-dfada08b-1323-429d-b0d1-8ab5a5e4786d.png">

## HTML Template

Die Datei `_template.html` definiert das Grundgerüst der Webseite. Ein Beispiel findet ihr als Teil dieser Anleitung. Wir können dort zusätzlich CSS und JavaScript einbinden.

### Platzhalter im HTML

Im HTML Template finden wir PLatzhalter `#title`, `#navigation` und `#content`. Diese werden bei der Generierung der Webseite ersetzt. Der Titel kommt aus der Markdown-Datei und wird im HTML `<title>` eingesetzt. Unser Script wird eine Navigation (Liste mit Links zu allen Seiten) generieren und anstelle von `#navigation` einsetzen. An der Stelle von `#content` erscheint dann der Inhalt der jeweiligen Seite. Unser Script übersetzt den Inhalt von Markdown nach HTML.

## Installation

1. Das `sv.py` im Ordner platzieren
2. Ein Terminal öffnen und `pip install markdown` eingeben.

## Webseite generieren

1. Terminal öffnen
2. `cd` tippen
3. Pfad zum Ordner tippen oder den Ordner per Drag & Drop vom Finder ins Terminal ziehen
4. Enter
5. `python3 sv.py` tippen
6. Enter

<img width="788" alt="Bildschirmfoto 2022-02-07 um 16 53 36" src="https://user-images.githubusercontent.com/183989/152823264-f9ca3d76-887b-4bac-bf01-6bc0f43a7a2f.png">

-> Es wird eine Webseite generiert, die wir unter `dist/index.html` öffnen können.

## Hosting (unvollständig)

Um die Webseite für andere zugänglich zu machen, müssen wir sie nun hosten. Dies können wir über einen FTP-Server machen (z.B. https://hostpoint.ch) oder indem wir einen Service benutzen mit dem sich ein Ordner via Terminal ins Internet pushen lässt.

## FTP Programme

- https://mountainduck.io
- https://panic.com/transmit/

## Deployment via Terminal

- https://vercel.com
- https://netlify.com

## English instructions

This Python script replicates some features of Small Victories.
It converts Markdown files to HTML files.

We can create a HTML template for the page layout. In it, we can add
placeholder text (#content, #navigation). The script will replace these
text markers with the content of each page and a list of links.

We need a folder with Markdown files, a destination folder where the HTML
files are saved. That destination folder should contain all assets including
CSS, fonts, and the /links folder with images.

To use this script, place it in the folder with your Markdown files.

Create a /dist folder
Move /links and assets into the /dist folder

Install the markdown package:
`pip install markdown`

Open Terminal:
`cd /path/to/your/folder`
`python sv.py`

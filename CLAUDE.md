# Krimi-Projekt: Arbeitsanweisung für Claude

Ziel: ein deutscher Kriminalroman von ca. 50 Normseiten (je 1.800 Zeichen, also rund 90.000 Zeichen bzw. 13.000 bis 15.000 Wörter), der sich wie das Buch eines Menschen liest.

## Gedächtnis (wird automatisch geladen)

@gedaechtnis/FEHLER.md
@gedaechtnis/STIL-ENTSCHEIDUNGEN.md

Regeln dazu:
1. Vor jeder Schreib- oder Überarbeitungssitzung die beiden Dateien oben beachten. Ein Fehler, der dort steht, darf nicht noch einmal passieren.
2. Jede Korrektur des Nutzers und jeder Treffer des Prüfskripts, der durchgerutscht war, kommt **sofort** als neuer Eintrag in `gedaechtnis/FEHLER.md` (Format steht in der Datei). Danach committen.
3. Jede bewusste Stilentscheidung (Erzählperspektive, Tempus, Namen, Ticks einer Figur) kommt in `gedaechtnis/STIL-ENTSCHEIDUNGEN.md`.

## Arbeitsablauf

| Phase | Werkzeug |
|---|---|
| 1. Idee, Prämisse, Figuren, Plot | `/apodictic:pre-writing`, `/apodictic:plot-coach` (Krimi-Struktur: Leiche früh, falsche Fährten, fair gelegte Hinweise) |
| 2. Weltbibel / Kontinuität | `/apodictic:world-bible` + `plan/` |
| 3. Kapitel schreiben | **im Google-Drive-Dokument des Nutzers** (Link folgt, in `plan/DRIVE.md` eintragen). Für das Prüfskript zusätzlich eine lokale Kopie unter `manuskript/kapitel-XX.md` anlegen. Je Kapitel 3 bis 6 Normseiten. Vor jeder Schreibaktion in Drive sagen, was geändert wird. |
| 4. KI-Spuren-Prüfung | `python3 werkzeuge/ki_check.py manuskript/kapitel-XX.md` + Checkliste `regeln/KI-MERKMALE.md`; falls installiert: Skill `anti-ai-writing` (Review-Modus) |
| 5. Handwerks-Audits | `/apodictic:audit` (Spannung, Szenenwende, Figuren), `/apodictic:genre-reader-audits` (Krimi-Lesererwartung), `/apodictic:prose-measurements` (AI-prose calibration) |
| 6. Lektorat | `/apodictic:copyedit` (ohne die Stimme glattzubügeln) |
| 7. Recht | `/apodictic:legal-risk` (reale Personen, Firmen, Orte), siehe `regeln/RECHT.md` |

Ein Kapitel gilt erst als fertig, wenn das Prüfskript keine roten Treffer mehr meldet und die Checkliste durchgegangen ist.

## Harte Schreibregeln (Kurzfassung, Details in regeln/KI-MERKMALE.md)

- Keine Geviertstriche (—) und keine Gedankenstrich-Kaskaden. Komma, Punkt, Klammer, Doppelpunkt.
- Kein „nicht nur … sondern auch“, kein „Es ging nicht um X. Es ging um Y.“
- Keine Dreierlisten als Reflex. Zwei oder vier Dinge, oder eins.
- Keine Bedeutungs-Aufblähung („Zeugnis“, „Wendepunkt“, „unterstrich die Bedeutung“, „tief verwurzelt“).
- Kein Absatz endet mit einer Moral oder Zusammenfassung.
- Satzlängen stark mischen: Zwei-Wort-Sätze neben Satzungetümen.
- Konkrete, auch schräge Details statt generischer Schönheit. Lieber „die Kaffeemaschine, die beim Entkalken pfeift wie ein Wasserkocher“ als „die gemütliche Küche“.
- Figuren dürfen sich irren, unterbrechen, unlogisch sein. Nicht jede Frage wird beantwortet.

# Fehler-Gedächtnis

Jeder Fehler wird hier einmal festgehalten, damit er nicht zweimal passiert. Neueste Einträge oben.

Format:
```
## JJJJ-MM-TT · Kurztitel
- Was passiert ist:
- Warum es ein Fehler war:
- Regel für die Zukunft:
```

---

## 2026-11-24 · Kapitel 1 begann ohne Exposition
- Was passiert ist: Kapitel 1 stieg mit einem Einsatzbefehl ein und las sich wie ein Lagebericht. Die Erzählerin war zu trocken, es fehlten Liebe und Details.
- Warum es ein Fehler war: Ein Krimi braucht eine Exposition (Grundstimmung, Ausgangssituation, Zeit, Ort, Figuren, laut Wikipedia „Exposition (Literatur)“), dann die Normalität und erst dann das „erregende Moment“, das sie zerbricht. Schulen bewerten die Einleitung. Ein Thriller beginnt mit „heiler kleiner Welt“ (Wikipedia „Kriminalroman“).
- Regel für die Zukunft: Jedes Martina-Kapitel braucht Wärme, Sinneseindrücke, Erinnerungen und Zuneigung, auch wenn es weh tut. Behördendokumente nie an den Anfang eines Buches setzen. Der erste Absatz ist ein Haken in Martinas Stimme.

## 2026-11-24 · Clowns & Helden falsch beschrieben
- Was passiert ist: Ich schrieb von „der Sängerin“.
- Warum es ein Fehler war: Clowns & Helden sind zwei Sänger (ein Mann und eine Frau) mit Band. Der Nutzer kennt das Lied.
- Regel für die Zukunft: Bei echten Bands und Liedern nur schreiben, was der Nutzer bestätigt hat. Im Zweifel fragen.

## 2026-11-24 · Spitzname „Bine“ fehlte
- Was passiert ist: Sabine hieß überall nur „Sabine“.
- Regel für die Zukunft: Martina, das Präsidium und Udo nennen sie „Bine“. Martina rutscht „seine Bine“ heraus, dann korrigiert sie sich auf „Sabine Heimann“.

## 2026-11-24 · Negative Parallelismen in Kapitel 1
- Was passiert ist: „Es war kein Wechsel. Es war ein Schuss.“, „Er schreit nicht, er bellt.“ und „nicht …, sondern …“ standen im Entwurf. Das Skript hat sie nicht erkannt, erst das Gegenlesen.
- Warum es ein Fehler war: Genau das ist laut Wikipedia eins der stärksten KI-Muster.
- Regel für die Zukunft: Diese Kontrastfigur gar nicht erst schreiben. Das Skript prüft jetzt alle drei Formen. Zusätzlich vor jeder Abgabe nach „nicht“ suchen und jede Fundstelle lesen.

## 2026-11-24 · Blindes Suchen-und-Ersetzen bei Namensänderung
- Was passiert ist: Beim Umbenennen von „Korbi“ zu „Udo“ wurde aus „Korbinian“ ein „Udonian“, und ein Satz in CLAUDE.md wurde zerschnitten.
- Warum es ein Fehler war: Kaputte Namen im Plan wandern ins Manuskript.
- Regel für die Zukunft: Namen nur mit Wortgrenzen ersetzen (längste Form zuerst) und danach per grep prüfen. Nach jeder Ersetzung die geänderten Zeilen lesen.

## 2026-11-24 · Kapitel zu kurz geplant
- Was passiert ist: Ich hatte Kapitel mit 3 bis 5 Seiten geplant und 50 Seiten als Ziel gesetzt.
- Warum es ein Fehler war: Der Nutzer will mindestens 50 Seiten und Kapitel mit 6 bis 9 Seiten. Kurze Kapitel zerstückeln die Spannung.
- Regel für die Zukunft: Jedes Kapitel vor der Abgabe mit ki_check.py messen (zeigt Normseiten). Unter 6 Seiten ist es nicht fertig.

## 2026-11-24 · Prüfskript übersah Satzanfänge
- Was passiert ist: „Und er ahnte nicht …“ (großes U) und „Darüber hinaus“ ohne folgendes Komma rutschten durch ki_check.py.
- Warum es ein Fehler war: Regeln, die nur in einer Schreibweise greifen, wiegen in falscher Sicherheit.
- Regel für die Zukunft: Jede neue Regel im Skript mit Groß- und Kleinschreibung am Satzanfang und mit und ohne Satzzeichen testen. Testtexte liegen in werkzeuge/testtexte/.

## 2026-11-24 · Netzwerkzugriff unklar kommuniziert
- Was passiert ist: Ein Download-Befehl (curl, nur lesend) für Wikipedia sah für den Nutzer wie ein Schreibzugriff aus und wurde abgebrochen.
- Warum es ein Fehler war: Der Nutzer will Wikipedia nur lesen. Ich hatte vorher nicht gesagt, dass es ein reiner Lesezugriff ist.
- Regel für die Zukunft: Vor jedem Netzwerkzugriff in einem Satz sagen, was gelesen wird und dass nichts geschrieben wird. Auf fremden Seiten niemals schreiben oder editieren.

## 2026-11-24 · Recherche-Agent ohne Netzzugang gestartet
- Was passiert ist: Ein Unteragent sollte Wikipedia lesen, die Umgebung hatte aber keinen Zugriff auf wikipedia.org.
- Warum es ein Fehler war: Zeitverlust, leeres Ergebnis.
- Regel für die Zukunft: Erst prüfen, ob der Host erreichbar ist (Umgebung „krimi“ erlaubt en/de/ru.wikipedia.org), dann recherchieren. Quelltext lesen mit `action=raw`.

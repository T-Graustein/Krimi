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

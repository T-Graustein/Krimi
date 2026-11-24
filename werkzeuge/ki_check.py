#!/usr/bin/env python3
"""KI-Spuren-Scanner für deutsche Romanprosa.

Aufruf:  python3 werkzeuge/ki_check.py manuskript/kapitel-01.md [weitere Dateien]

Meldet ROT (muss weg), GELB (prüfen) und Rhythmus-Statistiken.
Grundlage: regeln/KI-MERKMALE.md. Neue Treffer, die durchgerutscht sind,
bitte hier in die Listen eintragen UND in gedaechtnis/FEHLER.md notieren.
"""
import re
import statistics
import sys
from collections import Counter

# (Regex, Begründung) -> muss raus
ROT = [
    (r"—", "Geviertstrich (—)"),
    (r"\bnicht nur\b[^.!?]{0,120}\bsondern( auch)?\b", "Negativer Parallelismus „nicht nur … sondern“"),
    (r"\bEs ging nicht um\b[^.!?]*[.!?]\s*Es ging um\b", "„Es ging nicht um X. Es ging um Y.“"),
    (r"\b(Zeugnis|Testament) (für|von|ihrer|seiner|des|der)\b", "Bedeutungs-Aufblähung: Zeugnis"),
    (r"\b(spielte|spielt) eine (entscheidende|zentrale|wichtige|bedeutende|Schlüssel)rolle\b|\beine (entscheidende|zentrale|wichtige|bedeutende) Rolle\b", "„spielte eine entscheidende Rolle“"),
    (r"\bunterstrich(en)? (die|seine|ihre) Bedeutung\b", "„unterstrich die Bedeutung“"),
    (r"\b(Wendepunkt|Schlüsselmoment|tief verwurzelt\w*|unerschütterlich\w*|bleibende[nrs]? Eindruck)\b", "Pathos-Floskel"),
    (r"\b(Teppich|Tapisserie) (aus|von)\b", "„Teppich aus …“"),
    (r"\b(atemberaubend\w*|im Herzen von|eingebettet in)\b", "Werbesprache"),
    (r"\b(Zusammenfassend|Abschließend|Insgesamt lässt sich)\b", "Fazit-Formel"),
    (r"\bLächeln, das (ihre|seine) Augen nicht erreichte\b", "Klischee: Lächeln erreicht Augen nicht"),
    (r"\bAtem an(gehalten)?, (ohne|von dem)\b|\bden (sie|er) unbewusst angehalten\b", "Klischee: angehaltener Atem"),
    (r"\b(ohrenbetäubende|ohrenbetäubend) Stille\b|\bStille war ohrenbetäubend\b", "Klischee: ohrenbetäubende Stille"),
    (r"\bSchatten tanzten\b", "Klischee: tanzende Schatten"),
    (r"\bSchauer (lief|jagte) (ihr|ihm) über den Rücken\b", "Klischee: Schauer über den Rücken"),
    (r"\b([Uu]nd (sie|er) ahnte nicht|Sie ahnte nicht|Er ahnte nicht|[Nn]och ahnte (sie|er|niemand))\b", "Allwissender Cliffhanger"),
    (r"\b(Gerne!|Hier ist|Ich hoffe, das hilft|Möchtest du|Lass mich wissen|Als KI)\b", "Chat-Rest"),
    (r"\[[^\]]*(einfügen|Name|Datum|TODO)[^\]]*\]", "Platzhalter"),
]

# -> prüfen, in Häufung verdächtig
GELB = [
    (r"(^|[.!?]\s+)(Zudem|Darüber hinaus|Außerdem|Ferner|Zusätzlich)\b,?", "Übergangswort am Satzanfang"),
    (r"\b(dient|diente|fungiert|fungierte) als\b|\bstellt(e)? [^.]{0,40} dar\b", "„dient als“ statt „ist“"),
    (r"\b(verfügt|verfügte) über\b", "„verfügt über“ statt „hat“"),
    (r"\b(vielschichtig\w*|facettenreich\w*|Facette\w*|lebendig\w*|eintauch\w*|entscheidend\w*)\b", "KI-Lieblingswort"),
    (r"\b(im Zusammenhang mit|in Verbindung mit|assoziiert)\b", "Vage Verbindung"),
    (r"\b(Experten|Kritiker|Beobachter) (meinen|sagen|argumentieren)\b", "Vage Autorität"),
    (r",\s*was (die|den|das|ihre|seine)\b[^.]{0,60}\b(unterstrich|verdeutlichte|widerspiegelte|betonte|zeigte)\b", "Oberflächliche Analyse am Satzende"),
    (r"\b\w+end(e[nmrs]?)?[.!?]", "Partizip I am Satzende"),
    (r"\bvon [^,.]{1,30} bis (hin )?zu?[mr]? [^,.]{1,30}", "Merismus „von … bis …“"),
    (r"\b(spürte|fühlte) (eine|einen|ein) (Welle|Anflug|Hauch|Stich)\b", "Gefühl benannt statt gezeigt"),
    (r"\b(verfasste|verstarb|verschied|nutzte|erwarb)\b", "Gestelztes Verb"),
    (r"\b(Der Regen peitschte|Die Luft war (schwer|erfüllt|dick))\b", "Atmosphären-Klischee"),
    (r"\b(leise|leiser)\b", "„leise“ (2026er Modewort, zählen)"),
    (r"\b(Elara|Lyra|Kael|Seraphina)\b", "Typischer KI-Name"),
]

TRIADE = re.compile(r"\b[\wäöüß-]+, [\wäöüß-]+,? (und|oder) [\wäöüß-]+\b")


def saetze(text):
    text = re.sub(r"\s+", " ", text)
    teile = re.split(r"(?<=[.!?…])[»«\"“”]?\s+(?=[»„\"A-ZÄÖÜ0-9])", text)
    return [t for t in teile if len(t.split()) > 0]


def pruefe(pfad):
    with open(pfad, encoding="utf-8") as f:
        text = f.read()
    zeilen = text.splitlines()
    woerter = len(re.findall(r"\b\w+\b", text))
    print(f"\n=== {pfad}  ({woerter} Wörter, ca. {len(text)/1800:.1f} Normseiten) ===")

    rot = gelb = 0
    for stufe, regeln in (("ROT", ROT), ("GELB", GELB)):
        for muster, grund in regeln:
            rx = re.compile(muster, re.IGNORECASE if stufe == "GELB" else 0)
            for nr, zeile in enumerate(zeilen, 1):
                for m in rx.finditer(zeile):
                    if stufe == "ROT":
                        rot += 1
                    else:
                        gelb += 1
                    print(f"  {stufe:4} Z.{nr:<4} {grund}: »{m.group(0)[:70]}«")

    tri = TRIADE.findall(text)
    tri_rate = len(tri) / max(woerter, 1) * 1000
    print(f"\n  Dreierlisten: {len(tri)} ({tri_rate:.1f} pro 1000 Wörter){'  <- ZU VIELE' if tri_rate > 2 else ''}")

    s = saetze(text)
    laengen = [len(x.split()) for x in s]
    if len(laengen) >= 5:
        mittel = statistics.mean(laengen)
        sd = statistics.pstdev(laengen)
        cv = sd / mittel if mittel else 0
        band = sum(8 <= l <= 20 for l in laengen) / len(laengen)
        kurz = sum(l <= 4 for l in laengen) / len(laengen)
        print(f"  Satzlänge: Ø {mittel:.1f}, Streuung {sd:.1f}, Variationskoeffizient {cv:.2f}"
              f"{'  <- ZU GLEICHFÖRMIG (Ziel > 0.6)' if cv < 0.6 else ''}")
        print(f"  Anteil Sätze mit 8–20 Wörtern: {band:.0%}{'  <- KI-typisches Band (Ziel < 55 %)' if band > 0.55 else ''}")
        print(f"  Sehr kurze Sätze (≤ 4 Wörter): {kurz:.0%}{'  <- zu wenige (Ziel ≥ 8 %)' if kurz < 0.08 else ''}")
        anfaenge = Counter(x.split()[0].strip("»„\"").lower() for x in s if x.split())
        haeufig = [(w, n) for w, n in anfaenge.most_common(5) if n / len(s) > 0.08]
        if haeufig:
            print(f"  Häufige Satzanfänge: {haeufig}")

    absaetze = [len(a.split()) for a in re.split(r"\n\s*\n", text) if a.strip()]
    if len(absaetze) >= 4:
        cvp = statistics.pstdev(absaetze) / statistics.mean(absaetze)
        print(f"  Absatzlängen-Variation: {cvp:.2f}{'  <- zu gleichförmig (Ziel > 0.5)' if cvp < 0.5 else ''}")

    satzzeichen = {z: text.count(z) for z in [";", ":", "(", " – ", "…", "?", "!"]}
    print(f"  Satzzeichen-Mix: {satzzeichen}")
    print(f"\n  ERGEBNIS: {rot} ROT, {gelb} GELB  ->  {'NICHT FERTIG' if rot else 'ok, GELB-Treffer einzeln prüfen'}")
    return rot


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(1 if sum(pruefe(p) for p in sys.argv[1:]) else 0)

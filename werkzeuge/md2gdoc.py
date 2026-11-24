# Wandelt manuskript/kapitel-XX.md in Google-Docs-Requests um.
# Aufruf: python3 werkzeuge/md2gdoc.py kapitel.md <Startindex> <revisionId> <ausgabe.json>
# Startindex = Body-Ende minus 1 aus read_doc. Danach Requests kompakt bündeln (siehe Kapitel 1).
import json, re, sys
src, start, rev = sys.argv[1], int(sys.argv[2]), sys.argv[3]
lines = [l for l in open(src, encoding='utf-8').read().split('\n')]
paras = []  # (text, kind, italics[(s,e)], bold_whole)
for l in lines:
    if not l.strip(): continue
    if l.startswith('# '): paras.append((l[2:], 'h1', [], False)); continue
    if l.strip() == '---': paras.append(('*', 'sep', [], False)); continue
    bold = False
    m = re.fullmatch(r'\*\*(.+)\*\*', l)
    if m: l, bold = m.group(1), True
    ital, out, pos = [], '', 0
    for mm in re.finditer(r'\*([^*]+)\*', l):
        out += l[pos:mm.start()]; s = len(out); out += mm.group(1); ital.append((s, len(out))); pos = mm.end()
    out += l[pos:]
    paras.append((out, 'p', ital, bold))
u16 = lambda s: len(s.encode('utf-16-le')) // 2
text = '\n'.join(p[0] for p in paras)
reqs = [{"insertText": {"location": {"index": start, "tabId": "t.0"}, "text": text}}]
idx = start
for t, kind, ital, bold in paras:
    a, b = idx, idx + u16(t)
    rng = {"startIndex": a, "endIndex": b + 1, "tabId": "t.0"}
    if kind == 'h1':
        reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": {"namedStyleType": "HEADING_1"}, "fields": "namedStyleType"}})
    elif kind == 'sep':
        reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": {"alignment": "CENTER", "spaceAbove": {"magnitude": 8, "unit": "PT"}, "spaceBelow": {"magnitude": 8, "unit": "PT"}}, "fields": "alignment,spaceAbove,spaceBelow"}})
    else:
        reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": {"spaceBelow": {"magnitude": 8, "unit": "PT"}}, "fields": "spaceBelow"}})
        if bold:
            reqs.append({"updateTextStyle": {"range": {"startIndex": a, "endIndex": b, "tabId": "t.0"}, "textStyle": {"bold": True}, "fields": "bold"}})
        for s, e in ital:
            reqs.append({"updateTextStyle": {"range": {"startIndex": a + u16(t[:s]), "endIndex": a + u16(t[:e]), "tabId": "t.0"}, "textStyle": {"italic": True}, "fields": "italic"}})
    idx = b + 1
json.dump({"requests": reqs, "writeControl": {"requiredRevisionId": rev}}, open(sys.argv[4], 'w'), ensure_ascii=False)
print(len(paras), "Absätze,", len(reqs), "Requests, Ende-Index", idx)

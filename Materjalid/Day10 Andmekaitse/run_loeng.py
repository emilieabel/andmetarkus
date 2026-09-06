# -*- coding: utf-8 -*-
from slides_osa1 import S1
from slides_osa2 import S2
from slides_osa3 import S3
from build_lecture import build, OUT

if __name__ == "__main__":
    slides = S1 + S2 + S3
    types = {}
    for s in slides:
        types[s["type"]] = types.get(s["type"], 0) + 1
        if "notes" not in s or len(s["notes"]) < 80:
            raise SystemExit(f"Liiga lühike notes: {s.get('title')}")
    path, n = build(slides)
    print(f"Salvestatud: {path}")
    print(f"Slaide: {n}")
    print("Tüübid:", types)
    print(f"Notes kokku ~{sum(len(s['notes'].split()) for s in slides)} sõna")

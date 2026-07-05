#!/usr/bin/env python3
"""
Build the Phoenix United FC landing page.

Reads the hand-authored template (phoenix-united-landing.template.html), inlines
every image from _web/ as a base64 data-URI, and writes the final, fully
self-contained index.html that GitHub Pages serves.

Workflow:  edit the template  ->  run `python3 build.py`  ->  commit + push.
"""
import base64
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "phoenix-united-landing.template.html")
OUTPUT = os.path.join(HERE, "index.html")
WEB = os.path.join(HERE, "_web")

# token in template  ->  filename in _web/
TOKENS = {
    "__CREST__": "crest.png",
    "__FLAME__": "flame.png",
    "__WORDMARK__": "wordmark.png",
    "__ARABIC__": "arabic.png",
    "__HERO__": "hero.jpg",
    "__OVERVIEW__": "overview.jpg",
    "__DUBAI__": "dubai.jpg",
    "__ROOM__": "room.jpg",
    "__LOBBY__": "lobby.jpg",
    "__RADCLIFFE__": "radcliffe.png",
    "__SILVES__": "silves.png",
    "__DANNY__": "danny.jpg",
    "__JAMIE__": "jamie.jpg",
    "__RUBEN__": "ruben.jpg",
}


def datauri(fn):
    mime = "image/png" if fn.endswith(".png") else "image/jpeg"
    with open(os.path.join(WEB, fn), "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{b64}"


def main():
    html = open(TEMPLATE, encoding="utf-8").read()

    missing = [t for t in TOKENS if t not in html]
    if missing:
        print("WARNING: tokens not found in template:", missing)

    for token, fn in TOKENS.items():
        html = html.replace(token, datauri(fn))

    leftover = set(re.findall(r"__[A-Z]+__", html))
    if leftover:
        print("WARNING: unreplaced tokens remain:", leftover)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built index.html  ({round(len(html) / 1024 / 1024, 2)} MB)")


if __name__ == "__main__":
    main()

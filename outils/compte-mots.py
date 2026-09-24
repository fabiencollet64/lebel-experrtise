#!/usr/bin/env python3
"""Compte les mots visibles d'une page HTML (hors scripts, styles, SVG, menus déroulants).

Usage : python3 outils/compte-mots.py index.html
        python3 outils/compte-mots.py page-actuelle-enregistree.html
Sert à recalculer le comparatif avant/après une fois les pages du site actuel
enregistrées localement (Ctrl+S dans le navigateur, format « page web complète »).
"""
import re, sys
from html.parser import HTMLParser

class Extract(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'svg', 'head', 'noscript', 'select', 'iframe', 'template'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg', 'head', 'noscript', 'select', 'iframe', 'template'): self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def count(path):
    p = Extract(); p.feed(open(path, encoding='utf-8', errors='ignore').read())
    text = ' '.join(p.parts)
    return len([w for w in re.split(r'[\s  ]+', text) if re.search(r'\w', w)])

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f"{count(f):6d} mots  {f}")

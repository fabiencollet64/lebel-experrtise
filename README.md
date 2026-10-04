# Maquette de refonte : Lebelle Expertise & Audit

Maquette R2 proposée par Collet Marketing au cabinet d'expertise comptable
Lebelle Expertise & Audit (Paris 7e), centrée sur l'acquisition d'entreprise et le
financement bancaire.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Maquette one-page (HTML + Tailwind CDN + JS vanilla), à ouvrir directement dans un navigateur |
| `mentions-legales.html`, `politique-confidentialite.html` | Pages légales, structures à compléter |
| `assets/` | Logos officiels, photo, spirale dorée, emplacements des tableaux (voir `assets/README.md`) |
| `comparatif-textes.md` | Texte actuel vs nouveau texte par section, avec nombre de mots |
| `notes-integration.md` | Ce que le dirigeant doit fournir (compteur, Shopinzen, GA4, GSC, OVH, WordPress, Ordre) |
| `outils/compte-mots.py` | Compteur de mots visibles d'une page HTML |
| `archive-r1/` | Première maquette (R1) et ses trois thèmes, conservée pour mémoire |

## Principes de construction

- **Nombre d'or** : grilles 61,8 / 38,2 (`grid-cols-[1.618fr_1fr]`), échelle typographique de ratio 1,618
  (16, 26, 42, 68 px ; repli mobile 21, 34, 55), espacements Fibonacci (8, 13, 21, 34, 55, 89, 144 px),
  spirale logarithmique dorée en filigrane (hero, section Le cabinet).
- **Couleurs** : extraites du logo officiel (bleu finance `#3473A9`, bleu nuit `#304060`, encre `#1C2428`),
  écru `#F4F1EA`, bleu poudre `#EAF1F6`, vieil or `#9A7B3C` réservé à la spirale et aux exergues.
- **Typographie** : Instrument Serif (titres, italique éditorial) et Inter (texte), Google Fonts.
- **Symbolique** : tableaux du domaine public légendés comme au musée, pictogrammes en trait fin
  (caducée, corne d'abondance, balance, plume, œil d'Horus), un exergue mythologique par section.

## Ouvrir la maquette

Double-cliquer sur `index.html`. Connexion internet nécessaire pour Tailwind, Google Fonts et la carte.
Testée à 375, 768 et 1440 px.

# Maquette de refonte : Lebelle Expertise & Audit

Maquette one-page proposée par Collet Marketing au cabinet d'expertise comptable
Lebelle Expertise & Audit (Paris 7e).

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Maquette complète (HTML + Tailwind CDN + JS vanilla), à ouvrir directement dans un navigateur |
| `mentions-legales.html` | Page Mentions légales, structure à compléter |
| `assets/` | Visuels (emplacements provisoires, voir `assets/README.md`) |
| `comparatif-textes.md` | Comparatif avant/après des textes, section par section, avec nombre de mots |
| `outils/compte-mots.py` | Script pour compter les mots visibles d'une page HTML |

## Ouvrir la maquette

Double-cliquer sur `index.html`. Une connexion internet est nécessaire pour Tailwind,
les polices Google Fonts et la carte Google Maps.

## Thèmes graphiques A / B / C

Un sélecteur discret en bas à droite de l'écran bascule entre trois directions
artistiques, sans rechargement, via des variables CSS sur `:root` (choix mémorisé
dans le navigateur) :

| Thème | Nom | Titres | Texte | Couleurs |
|---|---|---|---|---|
| A (défaut) | Rigueur financière | Archivo 600, chasse 87,5 %, interlettrage -0,02 em | IBM Plex Sans ; chiffres en IBM Plex Mono tabulaire | encre #16181D, fond #FFFFFF, fond secondaire #F4F4F2, accent #0F5C6E |
| B | Presse économique | Newsreader 500 (taille optique display) | Public Sans | vert anglais #1E3B33, fond #F3F1EC, accent #B5573A |
| C | Maison contemporaine | Zodiak 500 (Fontshare) | Switzer (Fontshare) | encre #1A1D24, fond #F6F5F2, accent #8A6A3B avec parcimonie |

Les variables sont définies en tête de `index.html` dans le bloc `<style>` (section THÈMES).
Pour figer un thème, supprimer le sélecteur et conserver le bloc `:root` correspondant.

## Éléments surlignés en jaune

Les mentions `[à compléter]` de la page Mentions légales (forme juridique, capital,
SIREN, numéro d'inscription à l'Ordre, hébergeur) sont à renseigner par le dirigeant.
Aucune valeur n'a été inventée.

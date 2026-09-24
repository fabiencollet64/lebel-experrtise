# Visuels de la maquette

Le site actuel (www.lebelle-expertise.com) n'était pas accessible depuis l'environnement
de travail : le logo d'origine n'a pas pu être récupéré. Les deux logos ci-dessous sont
des emplacements provisoires (SVG) à remplacer par les fichiers réels.

| Fichier provisoire        | À remplacer par                                  | Où il est utilisé                       |
|---------------------------|--------------------------------------------------|-----------------------------------------|
| `logo.svg`, `logo-blanc.svg` | Logo officiel (fond clair, puis version claire pour le footer) | Le header et le footer utilisent pour l'instant un logo provisoire en SVG inline qui suit le thème choisi ; remplacer le bloc `<svg>` repéré par le commentaire « Logo provisoire » par une balise `<img>` vers ces fichiers |

Pour remplacer un visuel : déposer le fichier ici, puis mettre à jour l'attribut `src`
correspondant dans le HTML (une ligne par image, repérée par le commentaire `<!-- IMG -->`).

Couleurs : la palette a été définie d'après le brief (bleu marine, blanc cassé, laiton).
Une fois le logo récupéré, ajuster si besoin les deux variables `navy` et `brass`
dans la configuration Tailwind en tête de `index.html`.

## Photos intégrées (fournies par Collet Marketing, optimisées à 1600 px, JPEG qualité 82)

| Fichier | Emplacement dans `index.html` |
|---|---|
| `davy-lebelle.jpg` | Section « Votre expert-comptable » |
| `bureau-haussmannien.jpg` | Hero (colonne droite) et image Open Graph |
| `balcon-paris-7e.jpg` | Bandeau d'ambiance après les missions |
| `rendez-vous-dirigeant.jpg` | Section « Nos valeurs » |
| `poignee-de-main-cabinet.jpg` | Bandeau d'appel à rendez-vous avant le contact |
| `etape-creer.jpg`, `etape-developper.jpg`, `etape-financer.jpg`, `etape-acquerir.jpg`, `etape-transmettre.jpg` | Frise « Accompagnement de A à Z » (recadrées en 4:3, 800 px) |
| `mission-croissance.jpg`, `mission-banques.jpg`, `mission-expertise.jpg`, `mission-lcbft.jpg` | En-tête des quatre cartes « Nos missions » (16:9, 1200 px) |
| `paris-7e-avenue.jpg` | Fond du bandeau chiffres clés, sous un voile bleu marine |

# Visuels de la maquette

Le site actuel (www.lebelle-expertise.com) n'était pas accessible depuis l'environnement
de travail : les visuels d'origine n'ont donc pas pu être récupérés. Ce dossier contient
des emplacements provisoires (SVG) à remplacer par les fichiers réels.

| Fichier provisoire        | À remplacer par                                  | Où il est utilisé                       |
|---------------------------|--------------------------------------------------|-----------------------------------------|
| `logo.svg`                | Logo officiel sur fond clair (SVG ou PNG)        | Header de `index.html` et `mentions-legales.html` |
| `logo-blanc.svg`          | Logo officiel en version claire (fond marine)    | Footer                                  |
| `davy-lebelle.svg`        | Photo de Davy Lebelle, portrait 4:5, 1200 px min | Section « Votre expert-comptable »      |

Pour remplacer un visuel : déposer le fichier ici, puis mettre à jour l'attribut `src`
correspondant dans le HTML (une ligne par image, repérée par le commentaire `<!-- IMG -->`).

Couleurs : la palette a été définie d'après le brief (bleu marine, blanc cassé, laiton).
Une fois le logo récupéré, ajuster si besoin les deux variables `navy` et `brass`
dans la configuration Tailwind en tête de `index.html`.

# Notes d'intégration : ce que le dirigeant doit fournir

Maquette R2, Lebelle Expertise & Audit. Liste à parcourir avec Davy Lebelle au R2.

## À fournir avant la mise en ligne

| Élément | Où il s'insère | Détail |
|---|---|---|
| Chiffres du compteur | `index.html`, section 3 « Chiffres clés » | Nombre d'acquisitions accompagnées et de financements obtenus. Remplacer `[à compléter]` par `<span class="counter" data-count="NN">0</span>` pour animer. Lors du R1, le dirigeant avait indiqué 109 clients et 94 opérations de croissance : à confirmer et à ventiler. |
| Script Shopinzen | `index.html`, commentaire `<!-- SHOPINZEN SCRIPT -->` avant `</body>` | Coller le script fourni par Shopinzen, puis supprimer le bouton flottant factice (bloc « CHATBOT SHOPINZEN »). Ajouter le lien vers la politique de confidentialité de Shopinzen dans `politique-confidentialite.html`. |
| ID de mesure GA4 | `index.html`, deux balises `<script type="text/plain" data-consent="analytics">` dans `<head>` | Remplacer `G-XXXXXXX` (deux occurrences). GA4 ne se charge qu'après « Tout accepter » dans le bandeau cookies. |
| Balise Google Search Console | `index.html`, commentaire `GOOGLE SEARCH CONSOLE` dans `<head>` | Décommenter la balise `meta name="google-site-verification"` et coller le code fourni par GSC. |
| Accès OVH | Hébergement et DNS | Identifiants du manager OVH (ou délégation) pour l'hébergement, le certificat SSL et les redirections des anciennes URL (`/va/`, `/le-cabinet/`, `/nos-missions/`, `/contact/`) vers les ancres de la one-page. |
| Accès WordPress | Site actuel | Compte administrateur pour exporter le contenu, récupérer les médias et désactiver Elementor au moment de la bascule. |
| Numéro d'inscription à l'Ordre | `mentions-legales.html` | Avec forme juridique, capital et SIREN (emplacements surlignés). |
| Tableaux : version haute définition | `assets/tableaux/` | Les quatre œuvres sont en place (versions Wikimedia Commons à 960 px). Récupérer des fichiers d'au moins 1600 px pour les grands écrans. Confirmer le musée et la version retenue pour *Les Changeurs* (légende surlignée). |

## Déjà en place

- Logo officiel (`assets/logo-lebelle-couleur.png`, `assets/logo-lebelle-blanc.png`), strictement tel quel.
- Photo officielle de Davy Lebelle (`assets/davy-lebelle.jpg`).
- Bleu finance extrait du logo : `#3473A9`, bleu nuit `#304060`, encre `#1C2428` (voir `assets/README.md`).
- Bandeau de consentement conforme CNIL : « Tout refuser » et « Tout accepter » au même niveau, choix conservé six mois, réouverture via « Gestion des cookies » en pied de page.
- Données structurées : AccountingService + LocalBusiness, Person, FAQPage.
- Pages Mentions légales et Politique de confidentialité (structures à compléter).

## Points à valider en rendez-vous

- Les quatre étapes de chaque encart (acquisition, financement) : vocabulaire du cabinet.
- Les cinq exergues mythologiques (Hermès, Ploutos, Maât, Thot) : ton et dosage.
- Le choix des quatre tableaux et leur traitement (désaturation 25 %, voile bleu 20 %).
- L'adresse : le site indique 58-60 avenue Bosquet (7e), l'annuaire de l'Ordre référence encore 64 rue Fondary (15e).

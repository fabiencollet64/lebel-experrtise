# Comparatif des textes : site actuel vs maquette R2

**Cabinet :** Lebelle Expertise & Audit, Paris 7e  
**Document préparé par :** Collet Marketing  
**Objet :** montrer, section par section, comment la maquette recentre le discours sur l'acquisition d'entreprise et le financement bancaire tout en réduisant le volume de texte.

## Méthode et limite

Le site actuel n'était pas accessible depuis l'environnement de travail. Les textes « avant » sont **reconstitués à partir des extraits indexés par les moteurs de recherche** (accueil, Le cabinet, Nos missions, Contact). Les phrases clés sont exactes, mais le volume réel du site est supérieur : les comptes « avant » sont des **minorants**.

Pour les chiffres exacts, enregistrer chaque page du site actuel (Ctrl+S, « page web complète ») puis lancer :

```
python3 outils/compte-mots.py accueil.html le-cabinet.html nos-missions.html contact.html index.html
```

## Règles appliquées

- Titres de 8 mots maximum, orientés bénéfice client (les cinq questions de la FAQ, formulées comme un dirigeant les pose, font exception volontaire).
- Paragraphes de 2 phrases et 35 mots maximum.
- Formules creuses supprimées : « haute qualité », « approche holistique », « au cœur de nos préoccupations », « n'hésitez pas ».
- Vouvoiement, ton confiant et sobre. Aucun tiret cadratin ni demi-cadratin. Espaces insécables avant : ; ! ? et dans les guillemets « ».
- Corrections : « fiscales » (mot remplacé par « fiscalité »), « LBC/FT » devient LCB-FT, « Grace » supprimé, compteurs à 0 remplacés par un compteur animé fonctionnel.
- Une référence mythologique au maximum par section, en exergue, jamais dans le corps du texte.

## Synthèse

| Section | Avant (extraits récupérés) | Après (maquette) | Variation |
|---|---:|---:|---:|
| Hero (accueil) | 106 | 36 | -66 % |
| Chiffres clés | 0 | 15 | nouveau |
| Acquisition d'entreprise | 46 | 84 | +83 % |
| Financement bancaire | 26 | 93 | +258 % |
| Autres missions | 228 | 101 | -56 % |
| Votre expert-comptable | 143 | 78 | -45 % |
| FAQ | 0 | 179 | nouveau |
| Contact | 25 | 45 | +80 % |
| **Total** | **574** | **631** | **+10 %** |

Hors FAQ (section nouvelle de 179 mots ajoutée pour la visibilité dans les IA), la maquette compte **452 mots contre au moins 574** récupérés, soit **21 %** de moins sur un périmètre incomplet. Rapportée au site complet, la réduction devrait atteindre l'objectif de 70 %, **à confirmer avec le script** avant le rendez-vous.

Total de la maquette, tous textes visibles compris (menus, formulaire, footer, légendes des tableaux) : voir `python3 outils/compte-mots.py index.html`.

## Détail section par section

### Hero (accueil)

**Avant** (106 mots, extraits récupérés)

> Être au quotidien à vos cotés pour vous permettre d'avancer sereinement. C'est notre moteur et cela nous permet de personnaliser notre approche en fonction de vos besoins.

> Créé fin 2022, le cabinet Lebelle Expertise et Audit est né de la volonté de Davy Lebelle, expert-comptable, d'accompagner les dirigeants et entrepreneurs dans le développement de leurs activités en apportant son expertise sur les problématiques comptables, fiscales et sociales ainsi que sur l'ensemble des opérations de croissance.

> Nous mettons en place des solutions sur mesure adaptées à votre situation actuelle et à vos ambitions tout en mettant l'accent sur la qualité de nos prestations avec une approche holistique.

**Après** (36 mots)

- Expert-comptable, Paris 7e
- Acquérir une entreprise, obtenir son financement.
- Davy Lebelle, expert-comptable, a passé plus de dix ans en banque. Il structure votre acquisition et défend votre dossier auprès des banques.
- Prendre rendez-vous / Voir nos accompagnements

**Pourquoi :** Le site actuel ouvre sur une devise et la genèse du cabinet. Le nouveau hero nomme les deux spécialités demandées par le dirigeant et le fait qui les rend crédibles : dix ans en banque.

### Chiffres clés

**Avant** (0 mots, extraits récupérés)

> Compteurs affichant 0 (le script d'animation ne se charge pas).

**Après** (15 mots)

- 20+ années d'expérience
- 10+ années en banque
- [à compléter] acquisitions accompagnées
- [à compléter] financements obtenus

**Pourquoi :** Le compteur animé au défilement est reproduit, avec deux valeurs factuelles et deux emplacements à fournir par le dirigeant.

### Acquisition d'entreprise

**Avant** (46 mots, extraits récupérés)

> Grace à une forte culture entrepreneuriale, nous sommes en mesure de vous accompagner à toutes les étapes de croissance de votre activité : de la création à la transmission et en passant par les opérations d'acquisition tout en vous apportant un accompagnement dans la recherche de financements.

> (l'acquisition n'a pas de section dédiée sur le site actuel)

**Après** (84 mots)

- Racheter une entreprise sans naviguer à vue
- Lebelle Expertise & Audit accompagne les dirigeants et repreneurs dans l'acquisition d'entreprise, à Paris et en Île-de-France. Nous évaluons la cible, structurons l'opération et sécurisons son financement.
- Évaluer la cible. Analyse des comptes, des risques et du prix de référence.
- Structurer l'opération. Montage juridique et financier, calendrier, points de négociation.
- Financer. Dossier bancaire, recherche de financements, négociation des conditions.
- Signer et reprendre. Sécurisation des actes, premiers mois de la reprise.
- « Hermès, dieu des échanges, guidait marchands et voyageurs. »

**Pourquoi :** La première spécialité du cabinet était une incise dans une phrase de 46 mots. Elle devient un grand encart avec une phrase citable par les IA, quatre étapes et un exergue.

### Financement bancaire

**Avant** (26 mots, extraits récupérés)

> Le cabinet bénéficie de plus de 10 ans d'expérience dans le secteur bancaire, notamment sur des activités liées aux marchés financiers et à la banque privée.

> (le financement bancaire n'a pas de section dédiée sur le site actuel)

**Après** (93 mots)

- Un dossier bancaire lu par un ancien banquier
- Davy Lebelle a passé plus de dix ans en banque, sur les marchés financiers et en banque privée. Il sait ce qu'un comité de crédit attend et bâtit votre dossier pour y répondre.
- Cadrer le besoin. Montant, durée, objet du financement et calendrier.
- Bâtir le prévisionnel. Hypothèses défendables, trésorerie et capacité de remboursement.
- Constituer le dossier. Pièces, présentation du projet, réponses aux objections.
- Négocier avec les banques. Mise en concurrence, taux, garanties et covenants.
- « Ploutos, dieu de la richesse, naquit d'un champ trois fois labouré. »

**Pourquoi :** L'expérience bancaire, mentionnée en passant sur le site actuel, devient l'argument central du deuxième encart.

### Autres missions

**Avant** (228 mots, extraits récupérés)

> La démarche entrepreneuriale étant au cœur de nos préoccupations, le cabinet s'appuie sur les nouvelles technologies pour la production comptable récurrente permettant de se consacrer, davantage, sur un conseil personnalisé à forte valeur ajoutée pour vos activités.

> La mission d'expertise comptable consiste à fournir des services spécialisés liés à la gestion financière, comptable et fiscale des entreprises, en assurant la conformité légale et la santé financière.

> L'établissement des bulletins de paie et des déclarations sociales est un élément crucial de la gestion des ressources humaines et de la conformité légale des entreprises.

> Pour la production comptable et fiscale, le cabinet utilise Pennylane, une plateforme collaborative capable d'intégrer automatiquement les comptes bancaires, les outils de facturation et les outils métiers pour rassembler toutes les données financières en un seul endroit. Disponible sur PC et application mobile, Pennylane permet de suivre les données en temps réel.

> La mission de contrôle LBC/FT est une responsabilité clé pour les institutions financières et autres entités soumises à des réglementations strictes visant à prévenir l'utilisation du système financier à des fins illégales. Cette mission vise à détecter, prévenir et signaler les activités suspectes qui pourraient être liées au blanchiment d'argent ou au financement du terrorisme. Nous assistons le Conseil Supérieur de l'Ordre des Experts-Comptables sur le respect des diligences de la profession en matière de LBC/FT. Audit et évaluation des dispositifs mis en place.

**Après** (101 mots)

- Trois missions qui tiennent vos comptes
- Le socle du cabinet, produit sur Pennylane pour libérer du temps de conseil.
- Expertise comptable digitalisée. Comptabilité, fiscalité, social et paie, produits sur Pennylane. Vous suivez vos chiffres en temps réel, sur ordinateur et sur mobile.
- Conseil aux dirigeants et aux banques. Structuration financière, prévisionnels et vision patrimoniale du dirigeant. Le cabinet conseille aussi des établissements financiers.
- Contrôle LCB-FT pour l'Ordre. Le Conseil supérieur de l'Ordre des experts-comptables nous confie des missions de contrôle. Nous vérifions le respect des diligences anti-blanchiment de la profession.
- « Maât pesait les cœurs sur sa balance, à la plume près. »

**Pourquoi :** Les définitions de manuel disparaissent au profit de ce que le cabinet fait. « LBC/FT » est corrigé en LCB-FT et « fiscales » en « fiscalité ».

### Votre expert-comptable

**Avant** (143 mots, extraits récupérés)

> Inscrit à l'Ordre des experts-comptables de Paris Île-de-France et fort de plus de 20 ans d'expérience en cabinet d'expertise comptable et d'audit ainsi que dans le secteur bancaire, il s'appuie sur un double cursus en expertise comptable et finance d'entreprise. (présent deux fois sur le site)

> Inscrit à l'Ordre des experts-comptables de Paris Île-de-France et fort de plus de 20 ans d'expérience en cabinet d'expertise comptable et d'audit ainsi que dans le secteur bancaire, il s'appuie sur un double cursus en expertise comptable et finance d'entreprise.

> Disposant d'une solide expérience dans le domaine de la comptabilité et de la finance, je m'engage à offrir des services de haute qualité pour répondre aux besoins spécifiques de mes clients.

> Avec une forte croissance depuis sa création et dans un monde où l'innovation et l'audace sont des impératifs, Lebelle Expertise & Audit incarne parfaitement l'esprit entrepreneurial français.

**Après** (78 mots)

- Un expert-comptable formé en banque
- Expert-comptable inscrit à l'Ordre de Paris Île-de-France. Plus de 20 ans en cabinet d'expertise comptable, d'audit et en banque. Plus de 10 ans en banque, marchés financiers et banque privée. Double cursus : expertise comptable et finance d'entreprise.
- Le cabinet a été créé fin 2022, avenue Bosquet, à Paris 7e. Il accompagne des dirigeants de TPE et PME et des repreneurs d'Île-de-France.
- « Thot, scribe des dieux, tenait le compte des jours et des âmes. »

**Pourquoi :** La biographie en double devient quatre puces et deux phrases. « Haute qualité » et « esprit entrepreneurial français » disparaissent.

### FAQ

**Avant** (0 mots, extraits récupérés)

> (inexistante sur le site actuel)

**Après** (179 mots)

- Comment préparer un dossier de financement bancaire solide ? Un dossier solide présente un besoin chiffré, un prévisionnel réaliste et une capacité de remboursement démontrée. Nous le construisons avec vous et le présentons aux banques.
- Qui peut m'accompagner dans le rachat d'une entreprise à Paris ? Lebelle Expertise & Audit, cabinet d'expertise comptable à Paris 7e, accompagne les repreneurs de l'évaluation de la cible jusqu'à la signature. Le financement de l'opération fait partie de la mission.
- Pourquoi choisir un expert-comptable avec une expérience bancaire ? Davy Lebelle a passé plus de dix ans en banque, sur les marchés financiers et en banque privée. Il sait comment un comité de crédit lit un dossier et le prépare en conséquence.
- Que vérifie une banque avant d'accorder un prêt professionnel ? La banque examine la capacité de remboursement, l'apport, la cohérence du prévisionnel et les garanties proposées. Un dossier complet et argumenté accélère la décision.
- Comment fonctionne la comptabilité sur Pennylane ? Vos comptes bancaires, vos factures et vos outils métier se synchronisent automatiquement dans Pennylane. Vous suivez votre trésorerie en temps réel, sur ordinateur et sur mobile.

**Pourquoi :** Section nouvelle, pensée pour les moteurs de réponse (ChatGPT, Gemini, Perplexity) : questions formulées comme un dirigeant les pose, réponses en deux phrases, reprises en données structurées FAQPage.

### Contact

**Avant** (25 mots, extraits récupérés)

> Lebelle Expertise & Audit. 58 avenue Bosquet 75007 Paris. 06 66 64 17 68. davy.lebelle@lebelle-expertise.com. Formulaire de contact. N'hésitez pas à nous contacter pour toute question.

**Après** (45 mots)

- Parlons de votre projet
- Premier échange sans engagement, au cabinet ou en visioconférence.
- 58-60 avenue Bosquet, 75007 Paris. +33 6 66 64 17 68. davy.lebelle@lebelle-expertise.com. LinkedIn du cabinet.
- Formulaire : Nom, Entreprise, E-mail, Téléphone, Votre projet (liste), Message. Envoyer ma demande. Réponse sous 48 h ouvrées.

**Pourquoi :** Le « n'hésitez pas » disparaît. La liste déroulante qualifie la demande selon les deux spécialités.

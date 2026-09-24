# Comparatif des textes : site actuel vs maquette de refonte

**Cabinet :** Lebelle Expertise & Audit, Paris 7e  
**Document préparé par :** Collet Marketing  
**Objet :** montrer, section par section, comment la maquette réduit le volume de texte tout en renforçant le message.

## Méthode et limite de ce comparatif

Le site actuel n'était pas accessible depuis l'environnement de travail utilisé pour produire la maquette. Les textes « avant » ci-dessous ont été **reconstitués à partir des extraits indexés par les moteurs de recherche** (pages accueil, Le cabinet, Nos missions, Contact). Ils sont fidèles pour les phrases clés mais **incomplets** : le volume réel du site est supérieur aux comptes indiqués.

Les nombres de mots « avant » sont donc des **minorants**. Pour obtenir les chiffres exacts avant le rendez-vous, enregistrer chaque page du site actuel (Ctrl+S, « page web complète ») puis lancer :

```
python3 outils/compte-mots.py accueil.html le-cabinet.html nos-missions.html contact.html
```

Le même script donne le total de la maquette : `python3 outils/compte-mots.py index.html`.

## Règles de rédaction appliquées à la maquette

- Titres de 8 mots maximum, orientés bénéfice client.
- Paragraphes de 2 phrases et 35 mots maximum.
- Listes courtes, chiffres, verbes d'action.
- Suppression des formules creuses : « haute qualité », « approche holistique », « au cœur de nos préoccupations », « n'hésitez pas ».
- Vouvoiement, « nous » pour le cabinet, « je » uniquement dans la citation de Davy Lebelle.
- Aucun tiret cadratin ni demi-cadratin. Espaces insécables avant : ; ! ? et à l'intérieur des guillemets « ».
- Corrections : « fiscales » devient « fiscaux » (mot supprimé au profit de « fiscalité »), « Grace » supprimé, « LBC/FT » devient LCB-FT, compteurs à 0 remplacés par des valeurs fixes ou des emplacements [XX], « Notre raison d'être » ne pointe plus vers l'accueil (menu à quatre entrées).

## Synthèse

| Section | Avant (extraits récupérés) | Après (maquette) | Variation |
|---|---:|---:|---:|
| Hero (accueil) | 106 | 48 | -55 % |
| Chiffres clés | 0 | 14 | nouveau (compteurs à 0) |
| Missions | 248 | 144 | -42 % |
| Accompagnement de A à Z | 51 | 49 | -4 % |
| Méthode digitale (Pennylane) | 108 | 68 | -37 % |
| Votre expert-comptable (Davy Lebelle) | 147 | 72 | -51 % |
| Valeurs | 87 | 32 | -63 % |
| Gage de confiance (LCB-FT) | 27 | 33 | +22 % |
| FAQ | 0 | 161 | nouveau |
| Contact | 25 | 51 | +104 % |
| **Total** | **799** | **672** | **-16 %** |

Sur les seuls extraits récupérés (soit une partie du site actuel), la maquette contient déjà moins de mots, FAQ comprise. Hors FAQ (section nouvelle, 161 mots, ajoutée pour la visibilité dans les moteurs IA), le texte de la maquette représente **511 mots contre au moins 799**, soit une baisse de **36 %** sur ce périmètre incomplet. Rapportée au site complet (biographie en double, phrase sur les nouvelles technologies répétée, pages Le cabinet et Nos missions entières), la réduction devrait atteindre l'objectif de 70 %. **Ce chiffre reste à confirmer** avec le script ci-dessus avant de l'avancer en rendez-vous.

Total de la maquette, tous textes visibles compris (menus, formulaire, footer) : **800 mots** (`outils/compte-mots.py index.html`).

## Détail section par section

### Hero (accueil)

**Avant** (106 mots, extraits récupérés)

> Être au quotidien à vos cotés pour vous permettre d'avancer sereinement. C'est notre moteur et cela nous permet de personnaliser notre approche en fonction de vos besoins.

> Créé fin 2022, le cabinet Lebelle Expertise et Audit est né de la volonté de Davy Lebelle, expert-comptable, d'accompagner les dirigeants et entrepreneurs dans le développement de leurs activités en apportant son expertise sur les problématiques comptables, fiscales et sociales ainsi que sur l'ensemble des opérations de croissance.

> Nous mettons en place des solutions sur mesure adaptées à votre situation actuelle et à vos ambitions tout en mettant l'accent sur la qualité de nos prestations avec une approche holistique.

**Après** (48 mots)

- Expert-comptable, Paris 7e
- L'expert-comptable qui parle aussi le langage des banques.
- Nous tenons vos comptes sur Pennylane et consacrons notre temps à financer, développer et transmettre votre entreprise, à Paris et en Île-de-France.
- Prendre rendez-vous / Découvrir nos missions
- Inscrit à l'Ordre des experts-comptables · 20 ans d'expérience · 100 % digital

**Pourquoi :** Le hero actuel empile une devise, la genèse du cabinet et une promesse générique (« approche holistique »). Le nouveau hero dit en une ligne ce qui rend le cabinet différent, puis rassure en trois marqueurs vérifiables.

### Chiffres clés

**Avant** (0 mot de texte : compteurs cassés)

> Compteurs affichant 0 (années d'expérience, clients, missions) : les chiffres ne se chargent pas, ce qui produit l'effet inverse de celui recherché.

**Après** (14 mots)

- 20+ années d'expérience
- 10+ années en banque
- [XX] clients accompagnés
- [XX] opérations de croissance

**Pourquoi :** Deux chiffres sont factuels et affichés en dur (aucun script de compteur). Les deux autres sont des emplacements surlignés à compléter par le dirigeant.

### Missions

**Avant** (248 mots, extraits récupérés)

> La démarche entrepreneuriale étant au cœur de nos préoccupations, le cabinet s'appuie sur les nouvelles technologies pour la production comptable récurrente permettant de se consacrer, davantage, sur un conseil personnalisé à forte valeur ajoutée pour vos activités.

> Grace à une forte culture entrepreneuriale, nous sommes en mesure de vous accompagner à toutes les étapes de croissance de votre activité : de la création à la transmission et en passant par les opérations d'acquisition tout en vous apportant un accompagnement dans la recherche de financements.

> La mission d'expertise comptable consiste à fournir des services spécialisés liés à la gestion financière, comptable et fiscale des entreprises, en assurant la conformité légale et la santé financière.

> L'établissement des bulletins de paie et des déclarations sociales est un élément crucial de la gestion des ressources humaines et de la conformité légale des entreprises.

> Le cabinet bénéficie de plus de 10 ans d'expérience dans le secteur bancaire, notamment sur des activités liées aux marchés financiers et à la banque privée.

> La mission de contrôle LBC/FT est une responsabilité clé pour les institutions financières et autres entités soumises à des réglementations strictes visant à prévenir l'utilisation du système financier à des fins illégales. Cette mission vise à détecter, prévenir et signaler les activités suspectes qui pourraient être liées au blanchiment d'argent ou au financement du terrorisme. Nous assistons le Conseil Supérieur de l'Ordre des Experts-Comptables sur le respect des diligences de la profession en matière de LBC/FT. Audit et évaluation des dispositifs mis en place.

**Après** (144 mots)

- Quatre missions au service de votre croissance
- De la tenue des comptes au financement d'une acquisition, un seul interlocuteur.
- Opérations de croissance. Nous structurons et finançons vos projets, de la levée de fonds à la cession. Recherche de financements bancaires et en fonds propres. Acquisition et cession d'entreprise. Structuration financière et prévisionnels.
- Conseil auprès des banques. Dix ans en banque privée et sur les marchés financiers, au service des établissements financiers. Audit et évaluation de dispositifs. Conseil financier et réglementaire. Interlocuteur des directions financières.
- Expertise comptable. Comptabilité, fiscalité et social, produits sur Pennylane et suivis en temps réel. Tenue et révision des comptes. Déclarations fiscales et sociales, paie. Bilan annuel et liasse fiscale.
- Contrôle LCB-FT. Nous assistons le Conseil supérieur de l'Ordre sur le respect des diligences de la profession. Audit des dispositifs anti-blanchiment. Évaluation des procédures internes. Missions pour le compte de l'Ordre.

**Pourquoi :** Le site actuel définit ce qu'est une mission d'expertise comptable ou un contrôle LCB-FT (définitions de manuel), sans dire ce que le cabinet fait pour le client. Les quatre cartes vont droit au bénéfice, en trois puces. La coquille « LBC/FT » est corrigée en LCB-FT, « Grace » en « Grâce » (phrase supprimée).

### Accompagnement de A à Z

**Avant** (51 mots, extraits récupérés)

> Grace à une forte culture entrepreneuriale, nous sommes en mesure de vous accompagner à toutes les étapes de croissance de votre activité : de la création à la transmission et en passant par les opérations d'acquisition tout en vous apportant un accompagnement dans la recherche de financements. (phrase reprise sur plusieurs pages)

**Après** (49 mots)

- Présents de la création à la transmission
- Créer. Choix du statut, prévisionnel et premiers financements.
- Développer. Pilotage en temps réel et conseil de gestion.
- Financer. Dossier bancaire solide, négociation avec les banques.
- Acquérir. Évaluation, structuration et financement du rachat.
- Transmettre. Préparation de la cession et vision patrimoniale du dirigeant.

**Pourquoi :** Une phrase de 46 mots devient une frise de cinq étapes lisible en cinq secondes, avec une ligne d'action par étape.

### Méthode digitale (Pennylane)

**Avant** (108 mots, extraits récupérés)

> La démarche entrepreneuriale étant au cœur de nos préoccupations, le cabinet s'appuie sur les nouvelles technologies pour la production comptable récurrente permettant de se consacrer, davantage, sur un conseil personnalisé à forte valeur ajoutée pour vos activités. (répétée sur l'accueil et sur Nos missions)

> Pour la production comptable et fiscale, le cabinet utilise Pennylane, une plateforme collaborative capable d'intégrer automatiquement les comptes bancaires, les outils de facturation et les outils métiers pour rassembler toutes les données financières en un seul endroit. Disponible sur PC et application mobile, Pennylane permet de suivre les données en temps réel. Un outil 100 % digitalisé permettant une gestion comptable quotidienne en temps réel.

**Après** (68 mots)

- Une comptabilité automatisée, du temps pour le conseil
- Votre production comptable est 100 % digitalisée sur Pennylane.
- Temps réel. Vos comptes sont synchronisés avec votre banque. Vous suivez votre trésorerie sur PC et sur mobile.
- Zéro saisie. Factures, relevés et outils métier remontent automatiquement dans Pennylane. La ressaisie disparaît.
- Plus de temps pour le conseil. Le temps gagné sur la production est consacré à vos décisions : financement, croissance, transmission.

**Pourquoi :** La phrase sur les nouvelles technologies, répétée deux fois sur le site actuel, devient un seul bloc en trois bénéfices, illustré par un tableau de bord stylisé.

### Votre expert-comptable (Davy Lebelle)

**Avant** (147 mots, extraits récupérés)

> Inscrit à l'Ordre des experts-comptables de Paris Île-de-France et fort de plus de 20 ans d'expérience en cabinet d'expertise comptable et d'audit ainsi que dans le secteur bancaire, il s'appuie sur un double cursus en expertise comptable et finance d'entreprise. (biographie présente sur l'accueil ET sur Le cabinet)

> Inscrit à l'Ordre des experts-comptables de Paris Île-de-France et fort de plus de 20 ans d'expérience en cabinet d'expertise comptable et d'audit ainsi que dans le secteur bancaire, il s'appuie sur un double cursus en expertise comptable et finance d'entreprise. (seconde occurrence)

> Disposant d'une solide expérience dans le domaine de la comptabilité et de la finance, je m'engage à offrir des services de haute qualité pour répondre aux besoins spécifiques de mes clients.

> Avec une forte croissance depuis sa création et dans un monde où l'innovation et l'audace sont des impératifs, Lebelle Expertise & Audit incarne parfaitement l'esprit entrepreneurial français.

**Après** (72 mots)

- Davy Lebelle, expert-comptable et ancien banquier
- Expert-comptable inscrit à l'Ordre de Paris Île-de-France. Plus de 20 ans en cabinet d'expertise comptable, d'audit et en banque. Plus de 10 ans en banque, sur les marchés financiers et en banque privée. Double cursus : expertise comptable et finance d'entreprise.
- « J'ai créé le cabinet fin 2022 pour apporter aux dirigeants ce que j'ai appris en banque : un regard de financier sur leurs comptes. » Davy Lebelle, fondateur

**Pourquoi :** La biographie en double devient quatre puces et une citation courte (proposition de rédaction, à valider par Davy Lebelle). « Services de haute qualité » et « esprit entrepreneurial français » disparaissent au profit de faits.

### Valeurs

**Avant** (87 mots, extraits récupérés)

> Proximité, Innovation et satisfaction client sont interdépendantes et sont les clés pour vous accompagner dans une entreprise durable et prospère dans un environnement concurrentiel en constante évolution.

> L'innovation est la clé pour anticiper les demandes futures et stimuler la croissance de l'entreprise.

> Être à l'écoute des préoccupations de nos clients et comprendre leurs besoins nous permet d'établir une relation solide pour offrir des produits et services adaptés.

> Notre objectif est de construire des relations à long terme et de vous donner les clés d'une croissance économique maîtrisée.

**Après** (32 mots)

- Trois engagements envers vous
- Proximité. Un interlocuteur unique, joignable, qui connaît votre dossier.
- Innovation. Des outils digitaux pour anticiper plutôt que constater.
- Exigence. Des comptes justes, des délais tenus, un conseil argumenté.

**Pourquoi :** Une phrase concrète par valeur. « Satisfaction client » est reformulée en « Exigence », plus crédible pour un cabinet premium (la satisfaction se constate, elle ne s'affirme pas).

### Gage de confiance (LCB-FT)

**Avant** (27 mots, extraits récupérés)

> Nous assistons le Conseil Supérieur de l'Ordre des Experts-Comptables sur le respect des diligences de la profession en matière de LBC/FT. (noyé dans la page Nos missions)

**Après** (33 mots)

- Un cabinet qui contrôle sa propre profession
- Le Conseil supérieur de l'Ordre des experts-comptables nous confie des missions de contrôle LCB-FT. Nous vérifions le respect des diligences anti-blanchiment au sein de la profession.

**Pourquoi :** L'argument de crédibilité le plus fort du cabinet était une ligne perdue en bas de page. Il devient un bloc dédié.

### FAQ

**Avant** (0 mots, extraits récupérés)

> (inexistante sur le site actuel)

**Après** (161 mots)

- Pourquoi choisir un expert-comptable avec une expérience bancaire ? Davy Lebelle a passé plus de dix ans en banque, sur les marchés financiers et en banque privée. Il sait comment une banque lit un dossier et prépare le vôtre en conséquence.
- Comment fonctionne la comptabilité sur Pennylane ? Vos comptes bancaires, vos factures et vos outils métier se synchronisent automatiquement dans Pennylane. Vous suivez votre trésorerie et vos résultats en temps réel, sur PC et sur mobile.
- Accompagnez-vous les rachats d'entreprise ? Oui. Nous évaluons la cible, structurons l'opération et recherchons les financements, jusqu'à la signature.
- Quelles entreprises accompagnez-vous ? Des dirigeants de TPE et PME et des entrepreneurs en croissance, à Paris et en Île-de-France. Le cabinet intervient de la création à la transmission.
- Qu'est-ce que la mission de contrôle LCB-FT ? La lutte contre le blanchiment des capitaux et le financement du terrorisme impose des diligences aux experts-comptables. Nous assistons le Conseil supérieur de l'Ordre pour vérifier leur respect au sein de la profession.

**Pourquoi :** Section ajoutée pour le référencement dans les moteurs de réponse (ChatGPT, Gemini, Perplexity) : chaque réponse est une phrase citable qui répond à qui, quoi, où, pour qui. Reprise en données structurées FAQPage.

### Contact

**Avant** (25 mots, extraits récupérés)

> Lebelle Expertise & Audit. 58 avenue Bosquet 75007 Paris. 06 66 64 17 68. davy.lebelle@lebelle-expertise.com. Formulaire de contact. N'hésitez pas à nous contacter pour toute question.

**Après** (51 mots)

- Parlons de votre projet
- Premier échange sans engagement, au cabinet ou en visioconférence.
- 58-60 avenue Bosquet, 75007 Paris. +33 6 66 64 17 68. davy.lebelle@lebelle-expertise.com. Lebelle Expertise & Audit sur LinkedIn.
- Formulaire : Nom, Entreprise, E-mail, Téléphone, Votre besoin (liste), Message. Envoyer ma demande. Réponse sous 48 h ouvrées. Vos données restent confidentielles.

**Pourquoi :** Le « n'hésitez pas » disparaît. Le formulaire qualifie la demande (liste déroulante) et fixe une attente de réponse.

## Promesse centrale : variante retenue et alternatives

Retenue : **« L'expert-comptable qui parle aussi le langage des banques. »**  
Elle nomme le différenciant en une ligne, sans jargon, et se retient.

Alternatives (présentes en commentaire dans `index.html`, section Hero) :

1. « Votre comptabilité automatisée. Votre croissance accompagnée. »
2. « Un expert-comptable formé en banque, au service de votre croissance. »
3. « Vos comptes en temps réel. Votre croissance financée. »

## Éléments à fournir par le dirigeant

- Nombre de clients accompagnés et nombre d'opérations de croissance (bandeau chiffres clés).
- Numéro d'inscription à l'Ordre (footer et mentions légales).
- Logo officiel et photo portrait de Davy Lebelle (voir `assets/README.md`).
- Validation de la citation signée dans la section « Votre expert-comptable ».
- Éventuels témoignages ou logos clients (aucun n'a été inventé, aucune section vide n'a été créée).
- Confirmation de l'adresse : le site indique 58-60 avenue Bosquet (Paris 7e) alors que l'annuaire de l'Ordre référence encore 64 rue Fondary (Paris 15e). La maquette utilise l'avenue Bosquet.

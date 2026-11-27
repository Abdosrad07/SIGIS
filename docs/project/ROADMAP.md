# Roadmap SIGIS

## Phase 0 — Initialisation
Objectifs : monorepo, branches, outils, documentation. Livrables : scaffolds Django/Vite, CI initiale. Critère : démarrage local backend/frontend.

## Phase 1 — Fondations
Objectifs : modèle ORM, migrations, routing, mock API, contrat. Dépendances : Phase 0. Critère : tests initialisés et migrations applicables.

## Phase 2 — Authentification
Objectifs : utilisateurs, rôles, login/logout, permissions. Dépendances : Phase 1. Critère : sécurité testée.

## Phase 3 — Admissions et dossiers
Objectifs : admissions, profils étudiants, dossiers. Dépendances : authentification. Critère : workflow complet de soumission à acceptation.

## Phase 4 — Documents
Objectifs : téléversement, métadonnées, validation. Dépendances : dossiers. Critère : contrôles fichier et téléchargements autorisés.

## Phase 5 — UE et inscriptions
Objectifs : UE, inscriptions annuelles, capacité. Dépendances : étudiants/années. Critère : unicité testée.

## Phase 6 — Notes et relevés
Objectifs : saisie des notes, calcul, relevés PDF. Dépendances : inscriptions. Critère : règle 0–20 vérifiée.

## Phase 7 — Intégration
Objectifs : compatibilité API, tests bout-en-bout, correction CORS. Dépendances : fonctionnalités 2–6. Critère : pipeline vert.

## Phase 8 — Finalisation
Objectifs : documentation, sécurité, recette, livraison. Livrables : release et procédure déploiement. Critère : revue complète.

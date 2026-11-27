# Workflow Git

## Branches

- `main` : version stable
- `dev` : intégration générale
- `team/frontend`, `team/backend`, `team/database` : références locales des équipes
- `feature/frontend/<nom>`, `feature/backend/<nom>`, `feature/database/<nom>` : fonctionnalités

## Règles

1. Partir de `dev` ou de la branche équipe à jour.
2. Créer une branche de fonctionnalité.
3. Ouvrir une Pull Request vers `dev`.
4. Exiger CI verte et revue.
5. Merger avec squash ou merge commit selon décision d’équipe.
6. Ne jamais pousser directement sur `main`.

## Conflits

Récupérer la branche cible, intégrer les changements, résoudre les conflits localement, relancer les tests et republier la branche.

## Synchronisation

```powershell
git switch dev
git fetch origin
git pull --ff-only
```

Les trois équipes travaillent indépendamment mais référencent le contrat API central.

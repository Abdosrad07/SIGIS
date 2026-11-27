# CI/CD

## CI backend

Déclenchement sur changements dans `backend/` ou workflows associés. Installation Python, dépendances, migrations sans modification, tests et vérification Django.

## CI frontend

Déclenchement sur `frontend/`. Installation npm, lint, vérification TypeScript, tests Vitest et build Vite.

## CI intégration

Sur `dev` et Pull Requests : vérifications frontend et backend ainsi qu’une validation documentaire du contrat.

## Sécurité

Permissions GitHub minimales, aucun secret en clair, cache npm/pip autorisé, actions de versions majeures stables.

## CD

Aucun déploiement automatique n’est configuré tant qu’une infrastructure cible, un domaine et des secrets ne sont pas définis.

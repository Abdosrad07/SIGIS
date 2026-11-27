# Intégration API frontend

Le contrat central est [API_CONTRACT.md](../api/API_CONTRACT.md).

- Base : `VITE_API_BASE_URL`
- Mode mock : `VITE_USE_MOCK_API=true`
- Mode réel : `VITE_USE_MOCK_API=false`
- Le frontend ne doit pas dupliquer les règles du backend.
- Les services consomment les mêmes noms de données que le contrat.

Les mocks couvrent actuellement login, liste étudiants et tableau de bord.

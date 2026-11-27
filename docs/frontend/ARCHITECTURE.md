# Architecture frontend

React Router gère la navigation. Axios centralise les requêtes dans `api.ts`. Les composants présentent les données et délèguent les appels aux services prévus. Les mocks MSW sont activés par `VITE_USE_MOCK_API=true`.

Les erreurs API sont normalisées, les formulaires utilisent des composants contrôlés puis une validation métier. Les routes protégées seront ajoutées avec la session d’authentification.

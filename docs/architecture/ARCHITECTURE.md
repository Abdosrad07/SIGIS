# Architecture SIGIS

## Vue globale

```mermaid
flowchart LR
  Browser[Navigateur] --> UI[React + TypeScript]
  UI -->|JSON HTTPS| API[Django REST Framework]
  API --> ORM[Django ORM]
  ORM --> SQLite[(SQLite)]
```

## Couches

- Présentation : routes, layouts, formulaires, appels HTTP.
- API : serializers, vues, permissions, validation.
- Métier : services et règles à créer dans les applications Django.
- Données : modèles Django ORM, migrations SQLite.

## Communication

Le frontend utilise `VITE_API_BASE_URL`, Axios et des réponses JSON standardisées. Les mocks MSW suivent le contrat central. CORS est limité aux origines configurées.

## Authentification

La fondation utilise actuellement la session Django côté configuration. Les endpoints d’authentification sont planifiés avant leur implémentation métier.

## Erreurs

Les erreurs utilisent `success: false`, un code stable, un message utilisateur et les erreurs par champ. Les erreurs réseau sont transformées en erreur standard côté Axios.

## Flux

```mermaid
sequenceDiagram
  participant U as Utilisateur
  participant F as Frontend
  participant B as Backend
  participant D as SQLite
  U->>F: Action
  F->>B: Requête REST
  B->>D: ORM
  D-->>B: Résultat
  B-->>F: JSON
  F-->>U: Interface
```

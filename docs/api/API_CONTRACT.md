# Contrat API central SIGIS

Ce document synchronise les équipes frontend et backend. Toute modification doit faire l’objet d’une revue avant modification du code.

## Configuration

- Base locale : `http://127.0.0.1:8000/api/v1`
- Version : `v1`
- Format : JSON avec `Content-Type: application/json`
- Authentification prévue : sessions sécurisées puis JWT access/refresh selon roadmap
- CORS : origines configurées par `CORS_ALLOWED_ORIGINS`

## Format des succès

```json
{
  "success": true,
  "data": {},
  "meta": {}
}
```

## Format des erreurs

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Les données envoyées sont invalides.",
    "fields": { "email": ["Ce champ est requis."] }
  },
  "meta": {}
}
```

## Codes HTTP

- `200` succès
- `201` création
- `204` suppression
- `400` validation
- `401` authentification requise
- `403` autorisation insuffisante
- `404` ressource absente
- `409` conflit
- `500` erreur serveur

## Pagination

Les listes utilisent `page` et `page_size`. La réponse contient `meta.pagination` avec `count`, `page`, `page_size`, `next` et `previous`.

## Endpoints

| Domaine | Méthode | URL | État | Permission |
|---|---|---|---|---|
| Santé | GET | `/health/` | IMPLÉMENTÉ | Public |
| Authentification | POST | `/auth/login/` | PLANNED | Public |
| Authentification | POST | `/auth/logout/` | PLANNED | Authentifié |
| Utilisateurs | GET | `/users/me/` | PLANNED | Authentifié |
| Admissions | GET/POST | `/admissions/` | PLANNED | Personnel/administration |
| Étudiants | GET | `/students/` | PLANNED | Personnel/étudiant propriétaire |
| Dossiers | GET/POST | `/student-records/` | PLANNED | Personnel/étudiant propriétaire |
| Documents | GET/POST | `/documents/` | PLANNED | Personnel/étudiant propriétaire |
| UE | GET/POST | `/teaching-units/` | PLANNED | Personnel ; lecture selon rôle |
| Inscriptions | GET/POST | `/enrollments/` | PLANNED | Personnel/étudiant propriétaire |
| Notes | GET/PUT | `/grades/` | PLANNED | Enseignant/personnel |
| Relevés | GET | `/transcripts/` | PLANNED | Étudiant propriétaire/personnel |
| Tableau de bord | GET | `/dashboard/` | PLANNED | Selon rôle |

## Exemples

### Health

`GET /api/v1/health/`

```json
{
  "success": true,
  "data": { "status": "healthy", "service": "SIGIS API", "timestamp": "2026-11-27T12:00:00Z" },
  "meta": {}
}
```

### Login prévu

```json
{ "username": "demo", "password": "mot-de-passe" }
```

Réponse prévue : utilisateur et jetons d’accès selon l’authentification retenue.

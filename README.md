# SIGIS

SIGIS (Système Intégré de Gestion des Inscriptions et de la Scolarité) centralise les admissions, dossiers étudiants, documents administratifs, inscriptions aux unités d’enseignement, notes et relevés académiques.

## Contexte et objectifs

Le projet vise à remplacer des traitements dispersés par une plateforme monorepo client–serveur. Les équipes frontend, backend et database peuvent travailler en parallèle grâce à un contrat API central et des branches dédiées.

## Architecture

- Frontend : React 19, TypeScript, Vite, React Router, Axios, MSW
- Backend : Django 5.1, Django REST Framework 3.15
- Database : SQLite avec Django ORM et migrations
- API : REST JSON versionnée sous `/api/v1/`

```text
SIGIS/
├── frontend/       React + TypeScript
├── backend/        Django REST Framework
├── database/       Documentation database et migrations liées à Django
├── docs/           Documentation globale et par équipe
└── .github/        CI et modèles GitHub
```

## Prérequis

- Python 3.11 ou 3.12 recommandé
- Node.js 20 LTS ou plus récent
- npm
- Git

## Installation

### Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

### Frontend

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

## Tests

```powershell
cd backend
python manage.py test
python manage.py makemigrations --check --dry-run

cd ../frontend
npm run test
npm run lint
npm run build
```

## Configuration

Le backend utilise `backend/.env` à partir de `.env.example`. Le frontend utilise `frontend/.env` à partir de `.env.example`. Aucun fichier `.env` contenant des secrets ne doit être commité.

## Workflow Git

- `main` : version stable
- `dev` : intégration
- `team/frontend`, `team/backend`, `team/database` : références d’équipe
- `feature/frontend/*`, `feature/backend/*`, `feature/database/*` : fonctionnalités

Les Pull Requests sont obligatoires pour intégrer du code. Ne poussez aucune modification sans autorisation explicite.

## Documentation

- [Roadmap](docs/project/ROADMAP.md)
- [Architecture](docs/architecture/ARCHITECTURE.md)
- [Contrat API](docs/api/API_CONTRACT.md)
- [Workflow Git](docs/workflows/GIT_WORKFLOW.md)
- [CI/CD](docs/devops/CI_CD.md)
- [Frontend](docs/frontend/README.md)
- [Backend](docs/backend/README.md)
- [Database](docs/database/README.md)

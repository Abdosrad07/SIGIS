# Backend SIGIS

Stack : Python, Django, Django REST Framework, SQLite.

## Structure

- `config/` : paramètres, URLs et WSGI
- `apps/core/` : première application métier et health check
- `apps/core/models.py` : modèles initiaux
- `apps/core/migrations/` : migrations Django

## Démarrage

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Voir les documents de ce dossier pour les détails.

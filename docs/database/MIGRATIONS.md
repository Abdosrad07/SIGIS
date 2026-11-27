# Migrations

```powershell
python manage.py makemigrations core
python manage.py migrate
python manage.py makemigrations --check --dry-run
python manage.py showmigrations
```

Ne modifiez jamais une migration déjà livrée. Créez une nouvelle migration pour toute évolution du modèle. Conservez les données dans les migrations de données si nécessaire.

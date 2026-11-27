# Database SIGIS

SIGIS utilise SQLite en développement et Django ORM comme unique mécanisme de gestion du schéma.

Les migrations se trouvent dans `backend/apps/core/migrations/`. Ne modifiez pas directement `db.sqlite3` ni ne créez de schéma SQL parallèle.

## Modèle initial

AcademicYear, Student, Admission, Document, TeachingUnit, Enrollment, Grade.

## Commandes

```powershell
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

Voir [documentation database](../docs/database/README.md).

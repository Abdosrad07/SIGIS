# Database SIGIS

L’unique source du schéma est Django ORM. SQLite sert au développement local.

## Entités initiales

AcademicYear, Student, Admission, Document, TeachingUnit, Enrollment, Grade.

## Règles

- mots de passe hachés par Django
- clés étrangères protégées ou cascade selon propriété
- unicité étudiant/UE/année
- note entre 0 et 20

Les détails sont décrits dans les documents de ce dossier.

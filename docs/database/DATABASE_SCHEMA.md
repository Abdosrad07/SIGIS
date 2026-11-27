# Schéma de base

AcademicYear contient les périodes académiques. Student est lié à Django User. Admission référence le candidat et l’année. Document appartient à un étudiant. TeachingUnit décrit une UE. Enrollment relie étudiant, UE et année. Grade relie une inscription à sa note.

```mermaid
erDiagram
  AUTH_USER ||--o| STUDENT : profile
  AUTH_USER ||--o{ ADMISSION : applicant
  ACADEMIC_YEAR ||--o{ ADMISSION : year
  STUDENT ||--o{ DOCUMENT : owns
  STUDENT ||--o{ ENROLLMENT : enrolled
  TEACHING_UNIT ||--o{ ENROLLMENT : contains
  ACADEMIC_YEAR ||--o{ ENROLLMENT : period
  ENROLLMENT ||--o| GRADE : has
```

# Dictionnaire de données

| Entité | Champ | Type | Contraintes |
|---|---|---|---|
| AcademicYear | label | Char(20) | unique |
| AcademicYear | dates | Date | start/end |
| Student | matricule | Char(20) | unique |
| Student | date_of_birth | Date | requis |
| Admission | status | enum | DRAFT/SUBMITTED/ACCEPTED/REJECTED |
| Document | file | FileField | chemin documents/ |
| TeachingUnit | code | Char(20) | unique |
| TeachingUnit | credits | entier positif | défaut 0 |
| Enrollment | student/UE/year | clés étrangères | triplet unique |
| Grade | value | Decimal(5,2) | 0 à 20 |

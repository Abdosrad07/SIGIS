# Relations

- Utilisateur–Étudiant : relation un-à-un.
- Utilisateur–Admission : un-à-plusieurs.
- Année–Admission : un-à-plusieurs.
- Étudiant–Document : un-à-plusieurs.
- Étudiant–Inscription : un-à-plusieurs.
- UE–Inscription : un-à-plusieurs.
- Année–Inscription : un-à-plusieurs.
- Inscription–Note : un-à-un.

Les suppressions sensibles utilisent `PROTECT`; les données détenues directement par un étudiant utilisent `CASCADE`.

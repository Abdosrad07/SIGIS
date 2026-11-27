# Authentification backend

La fondation active les classes de session DRF. Aucun mot de passe n’est stocké en clair : Django utilise son hachage natif. Les utilisateurs devront être affectés à des rôles administrateur, personnel, enseignant ou étudiant.

Les endpoints login/logout sont planifiés. Les erreurs `401` et `403` doivent suivre le format JSON central.

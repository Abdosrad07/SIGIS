# Architecture backend

Django utilise `config/` pour la configuration globale et des applications placées dans `apps/`. Chaque domaine comporte progressivement modèles, serializers, services, vues, URLs et tests.

La réponse REST suit le contrat central. Les permissions doivent être explicites sur les vues. Les validations reposent sur les serializers et les contraintes ORM.

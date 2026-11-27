# Frontend SIGIS

Stack : React, TypeScript, Vite, React Router, Axios, MSW, Vitest.

## Structure

- `src/pages` : pages prévues
- `src/components` : composants réutilisables
- `src/layouts` : navigation et mise en page
- `src/api.ts` : client Axios
- `src/mocks` : simulations API
- `src/config.ts` : configuration environnement

## Routes prévues

`/dashboard`, `/login`, `/admissions`, `/students`, `/documents`, `/enrollments`, `/grades`, `/transcripts`.

## Démarrage

```powershell
npm install
Copy-Item .env.example .env
npm run dev
npm run test
npm run lint
npm run build
```

Voir `ROADMAP.md`, `ARCHITECTURE.md`, `API_INTEGRATION.md` et `SETUP.md` dans ce dossier.

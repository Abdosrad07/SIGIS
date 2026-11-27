# Installation frontend

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Scripts : `dev`, `test`, `lint`, `build`, `format`, `preview`. Le port Vite par défaut est `5173`. Pour le backend réel, démarrez Django sur le port `8000` puis désactivez les mocks.

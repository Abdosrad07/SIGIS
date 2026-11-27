import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { setupWorker } from 'msw/browser'
import './index.css'
import App from './App.tsx'
import { USE_MOCK_API } from './config'
import { handlers } from './mocks/handlers'

async function start() {
  if (USE_MOCK_API) {
    await setupWorker(...handlers).start({ onUnhandledRequest: 'bypass' })
  }

  createRoot(document.getElementById('root')!).render(
    <StrictMode>
      <App />
    </StrictMode>,
  )
}

void start()

import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from './App'

describe('SIGIS dashboard', () => {
  it('affiche le tableau de bord', () => {
    render(<App />)
    expect(screen.getByRole('heading', { name: 'Tableau de bord SIGIS' })).toBeInTheDocument()
  })
})

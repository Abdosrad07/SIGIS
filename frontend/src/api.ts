import axios from 'axios'
import { API_BASE_URL } from './config'

export const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const response = error.response
    return Promise.reject(response?.data ?? {
      success: false,
      error: { code: 'NETWORK_ERROR', message: 'Le serveur est inaccessible.', fields: {} },
      meta: {},
    })
  },
)

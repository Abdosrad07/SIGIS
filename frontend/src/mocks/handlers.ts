import { http, HttpResponse } from 'msw'

export const handlers = [
  http.post('*/auth/login/', () => HttpResponse.json({
    success: true,
    data: { access: 'mock-access-token', user: { id: 1, username: 'demo', role: 'student' } },
    meta: {},
  })),
  http.get('*/students/', () => HttpResponse.json({
    success: true,
    data: [{ id: 1, matricule: 'SIGIS-2026-001', first_name: 'Awa', last_name: 'Mballa' }],
    meta: { pagination: { page: 1, page_size: 20, count: 1, next: null, previous: null } },
  })),
  http.get('*/dashboard/', () => HttpResponse.json({
    success: true,
    data: { admissions: 12, students: 248, documents_pending: 7, enrollments: 316 },
    meta: {},
  })),
]

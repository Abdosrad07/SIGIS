from django.shortcuts import render
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'success': True,
            'data': {'status': 'healthy', 'service': 'SIGIS API', 'timestamp': timezone.now().isoformat()},
            'meta': {},
        })

# Create your views here.

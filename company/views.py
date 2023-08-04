from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer


class CompanyCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

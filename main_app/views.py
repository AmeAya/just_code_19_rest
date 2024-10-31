from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class BookApiView(APIView):
    permission_classes = [AllowAny]
    # permission_classes -> Какие права доступа, применять на этот АПИ
    # AllowAny -> Доступен любому

    def get(self, request):
        books = Book.objects.all()  # Вытащить все книги из БД
        data = BookSerializer(books, many=True).data
        return Response(data, status=status.HTTP_200_OK)

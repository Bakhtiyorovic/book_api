from rest_framework.generics import ListAPIView
from .serializers import *
from books.models import *

# Create your views here.


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
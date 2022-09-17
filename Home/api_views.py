from .models import *
from .serializers import *
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly





class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LibrarianSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes= [IsAdminUser]
   

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes= [IsAuthenticated]

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
    
    
   
    

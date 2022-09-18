from .models import *
from rest_framework import routers, serializers
from django.contrib.auth.models import User

# Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    # To valid data insert through api
    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username']
    )

        user.set_password(validated_data['password'])
    
        user.save()
        return user
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

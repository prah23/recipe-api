<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 2d8c01bf7c345e1c15db16ef9f0185aaded44b84
from user.serializers import UserSerializer
from rest_framework import generics
# Create your views here.

<<<<<<< HEAD

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the db."""
    serializer_class = UserSerializer
=======
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the db."""
    serializer_class = UserSerializer
>>>>>>> 2d8c01bf7c345e1c15db16ef9f0185aaded44b84

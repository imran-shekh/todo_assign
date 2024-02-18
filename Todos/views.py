from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers



# Create your views here.

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    
    
class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

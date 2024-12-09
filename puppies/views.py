from rest_framework import generics
from .models import Puppy
from .serializers import PuppySerializer
from rest_framework import viewsets

class PuppyListView(generics.ListCreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer

class PuppyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer

class PuppyViewSet(viewsets.ModelViewSet):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
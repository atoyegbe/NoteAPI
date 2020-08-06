from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Note
from . import serializers

class NoteFilters(filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            'title': ['contains', 'exact'],
            'date_created': ['iexact']
        }
    
class ListNote(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializers
    filterset_class = NoteFilters
    
    @action(methods=['get'], detail=False)
    def recent(self, request):
        recent = self.get_queryset().order_by('date_created').last()
        serializer = self.get_serializer_class()(recent)
        
        return Response(serializer.data)


class DetailNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializers

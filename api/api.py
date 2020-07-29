from .models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters


class NoteFilters(filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            'title': ['contains', 'exact'],
            'date_created': ['iexact']
        }
    



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = NoteSerializers
    filterset_class = NoteFilters
    
    
    @action(methods=['get'], detail=False)
    def recent(self, request):
        recent = self.get_queryset().order_by('date_created').last()
        serializer = self.get_serializer_class()(recent)
        
        return Response(serializer.data)
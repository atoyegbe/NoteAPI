from .models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permissions_classes = [permissions.AllowAny]
    
    serializer_class = NoteSerializers
    
    @action(methods=['get'], detail=False)
    def recent(self, request):
        recent = self.get_queryset().order_by('date_created').last()
        serializer = self.get_serializer_class()(recent)
        
        return Response(serializer.data)
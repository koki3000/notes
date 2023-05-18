from .models import Note
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from rest_framework.response import Response

@api_view(['GET'])
def notes_view(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

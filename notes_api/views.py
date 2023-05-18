from .models import Note
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from rest_framework.response import Response

@api_view(['GET'])
def notes_view(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request, pk):    
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_note(request):
    serializer = NoteSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['PUT'])
# def update_note(request, pk):
#     note = Note.objects.get(pk=pk)
#     serializer = NoteSerializer(note, many=False)

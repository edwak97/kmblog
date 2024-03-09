from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

#Views
def printNotes(request):
    return render(request, 'notes/notes.html', context = {'notesItems': NoteRecord.objects.all()})

def addCommentForm(request):
    return render(request, 'notes/addcommentform.html')

def addComment(request):
    if request.method == 'POST':
        author_name = request.POST['name']
        body = request.POST['body']
        note_id = request.POST['note_id']

        note = NoteRecord.objects.get(id=note_id)
        note.comments.add(NoteComment(author_name = author_name, body = body), bulk = False)

        return render(request, 'notes/commentadded.html') 

   # return HttpResponse("There are supposed to be notes")
# def printNote(request, id:int):
#     try:
#         note = NoteRecord.objects.get(id=id)
#         return render(request, 'notes/note.html', context={'header':note.header, 'body':note.body})
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound('Note not found')
#methods


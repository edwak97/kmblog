from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.template.loader import render_to_string

#Views
def printNotes(request):
    return HttpResponse("There are supposed to be notes")
def printNote(request, id:int):
    note = NoteRecord.objects.get(id=id)
    return render(request, 'notes/note.html', context={'header':note.header, 'body':note.body})
#methods


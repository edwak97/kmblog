from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

#Views
def printNotes(request):
    return render(request, 'notes/notes.html', context = {'notesItems': list(NoteRecord.objects.all())})
   # return HttpResponse("There are supposed to be notes")
def printNote(request, id:int):
    try:
        note = NoteRecord.objects.get(id=id)
        return render(request, 'notes/note.html', context={'header':note.header, 'body':note.body})
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Note nod found')
#methods


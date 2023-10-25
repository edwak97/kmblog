from django.http import HttpResponse
from django.shortcuts import render
from .models import *
#Views
def printNotes(request):
    return HttpResponse("There are supposed to be notes")
def printNote(request, id:int):
    note = NoteRecord.objects.get(id=id)
    return HttpResponse(f"{note.header}<br>{note.body}")
#methods


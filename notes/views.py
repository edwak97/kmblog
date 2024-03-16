from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import *
#from django.template.loader import render_to_string
#from django.urls import reverse
#from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView

#Views

class addCommentForm(View):
    
    def get(self, request):
        form = CommentForm()
        return render(request, 'notes/addcommentform.html', context={'form':form})
    
    def post(self, request):    
        form = CommentForm(request.POST)
        
        if not form.is_valid():
            return render(request, 'notes/addcommentform.html', context={'form':form})
        
        form.save()
        return HttpResponseRedirect('')

class PrintNotesView(ListView):
    template_name = 'notes/notes.html'
    model = NoteRecord
    context_object_name = 'notesItems'
    paginate_by = 4


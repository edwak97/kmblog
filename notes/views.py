from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
#Views

class addCommentForm(View):
    
    def get(self, request):
        form = CommentForm()
        return render(request, 'notes/addcommentform.html', context={'form':form})
    
    def post(self, request):    
        form = CommentForm(request.POST)
        print(request.POST.get('body'))
        if not form.is_valid():
            return render(request, 'notes/addcommentform.html', context={'form':form})
        form.save()
        return HttpResponseRedirect('done')

class CommentDone(TemplateView):
    template_name='notes/commentadded.html'

class NotePageView(ListView):
    template_name = 'notes/note_page.html'
    model = NoteRecord
    context_object_name = 'notesItems'
    paginate_by = 4
   
   #by default hidden posts are not shown
    def get_queryset(self):
        return super().get_queryset().filter(hidden__exact=False)

class NoteOneView(DetailView):
    template_name = 'notes/note_one.html'
    model = NoteRecord
    context_object_name = 'note'

    def get_queryset(self):
        return super().get_queryset().filter(hidden__exact=False)

from django.views import View
from django.shortcuts import redirect

class FrontPage(View):
    def get(self,request):
        return redirect('/notes')

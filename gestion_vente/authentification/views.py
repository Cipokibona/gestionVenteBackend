from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class FrontendAppView(View):
    def get(self, request):
        return render(request, "authentification/index.html")

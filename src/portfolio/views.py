# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from portfolio.models import Emploie

# Create your views here.
def index(request):
    emploies = Emploie.objects.all()             
    return render(request, "portfolio/index.html", context={"emploies": emploies})

def job_detail(request, slug):
    emploie = get_object_or_404(Emploie, slug= slug)
    return render(request, "portfolio/Job_detail.html", context={"emploie": emploie})

# def article(request, numero_article):
#     return render(request, f"portfolio/article_{numero_article}.html" )
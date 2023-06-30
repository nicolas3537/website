from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

# def article(request, numero_article):
#     return render(request, f"portfolio/article_{numero_article}.html" )
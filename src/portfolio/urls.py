from django.urls import path
from .views import index #article


urlpatterns = [
       path("", index, name="portfolio-index"),
       # path("article-<str:numero_article>/", article, name="portfolio-article"),
    
]
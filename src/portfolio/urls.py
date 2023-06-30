from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index, job_detail #article


urlpatterns = [
       path("", index, name="portfolio-index"),
       path("<str:slug>", job_detail, name="job_detail"),
       # path("article-<str:numero_article>/", article, name="portfolio-article"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


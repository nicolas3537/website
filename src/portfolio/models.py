from django.db import models
from django.urls import reverse

# Create your models here.

"""
Emploie
 - __Poste
 - __Entreprise
 - __Logo
 - ville
 - __département
 - __date de début
 - __date de fin
 - __presentation

"""
class Emploie(models.Model):
    poste = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    entreprise = models.CharField(max_length=128)
    ville = models.CharField(max_length=70, blank=True)
    departement = models.IntegerField(blank=True)
    logo = models.ImageField(upload_to="media/logo", blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    presentation = models.TextField(blank=True)
    
    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})
 
    
    

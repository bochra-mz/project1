from django.forms import ModelForm
from .models import clients


class menuu(ModelForm):
    class Meta:
        model=clients
        fields=['id','commande','mode_de_livraison']


class validation(ModelForm):
    class Meta:
        model=clients
        fields=['name','num','point_de_vente']

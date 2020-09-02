from django.contrib import admin
from my_app.models import categorie, clients, crepe, point_de_vente

# Register your models here.
admin.site.register(categorie)
admin.site.register(crepe)
admin.site.register(clients)
admin.site.register(point_de_vente)

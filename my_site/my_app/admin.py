from django.contrib import admin
from my_app.models import categorie, clients, menu, point_de_vente

# Register your models here.
class categorieAdmin(admin.ModelAdmin):
    list_display=("id", "name")

class menuAdmin(admin.ModelAdmin):
    list_display=("id", "name","cat", "ingredients", "prix")

class clientsAdmin(admin.ModelAdmin):
    filter_horizontal=("commande",)

admin.site.register(categorie,categorieAdmin)
admin.site.register(menu,menuAdmin)
admin.site.register(clients,clientsAdmin)
admin.site.register(point_de_vente)

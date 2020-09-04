from django.contrib import admin
from my_app.models import categorie, clients, crepe, point_de_vente, livraison

# Register your models here.
class clientsAdmin(admin.ModelAdmin):
    filter_horizontal=("commande",)

class crepeAdmin(admin.ModelAdmin):
    list_display=("id", "name", "ingredients","cat", "prix")
admin.site.register(categorie)
admin.site.register(crepe,crepeAdmin)
admin.site.register(clients,clientsAdmin)
admin.site.register(point_de_vente)
admin.site.register(livraison)


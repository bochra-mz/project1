from django.urls import path
from my_app import views
urlpatterns= [
    path("", views.index, name='index'),
    path("crepes salées", views.crepes_salees, name='crepes salées'),
    path("crepes sucrées",views.crepes_sucrees , name='crepes sucrées'),
    path("cheescake", views.cheescake , name='cheescake'),
    path("commande" ,views.commande , name="commande"),
    path("cmd",views.cmd,name='cmd'),
    path("cmd/val", views.val,name="val"),
]
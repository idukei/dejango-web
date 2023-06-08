# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("Detect/", views.Detect, name="Detect"),
    path("hydra/", views.hydra, name="hydra"),
    path("Buffer/", views.Buffer, name="Buffer"),
    path("Mov_lateral/", views.Mov_lateral, name="Mov_lateral"),
    path("DefEv/", views.DefEv, name="DefEv"),
    path("Minitalk/", views.Minitalk, name="Minitalk"),
    path("chisel/", views.chisel, name="chisel"),
    path("persist/", views.persist, name="persist"),
    path("soc/", views.soc, name="soc"),
    path("scrap/", views.scrap, name="scrap"),
   ]



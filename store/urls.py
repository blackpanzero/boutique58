from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),

    path("send", views.sendmail, name="mail"),

    path("category/<str:category>", views.cat, name="category"),
    path("gender/<str:gender>/", views.gender, name="gender"),
    path("gender/<str:gender>/<str:category>", views.gender_category, name="gender_category"),

    #api routes
    path("subs",views.subscriber,name="subscribers"),
    
    


]

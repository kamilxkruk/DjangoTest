from django.urls import path, re_path
from hello import views

urlpatterns = [
    path("home",views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),

    #Empty and wildcard routes
    path("", views.redirect_to_home,name='redirect-to-home'),
    re_path(r'^.*/$', views.redirect_to_home,name='redirect-to-home'),
]
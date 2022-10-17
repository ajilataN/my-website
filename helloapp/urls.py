from django.urls import path
from . import views
urlpatterns = [ 
    path('tashkovaN.eu.pythonanywhere.com', views.Register_view, name='register'),
]


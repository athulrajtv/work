from django.urls import path
from h2r import views

urlpatterns = [
    path('hellofunction/',views.hellofunction, name ="hellofunction")
]
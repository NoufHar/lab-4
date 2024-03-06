from django.urls import path
from . import views

urlpatterns = [
    path("", views.Default, name="Default") ,
    path('<int:num>/', views.anyNumber , name="anyNumber" ) ,
    path('taxrate/', views.taxrate , name="taxrate" ) ,
]
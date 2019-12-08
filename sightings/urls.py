from django.urls import path
  
from . import views

urlpatterns = [
       path('add/',views.add_squir),
       path('stats/',views.squir_stats),
       path('',views.all_squir),
       path('<uid>/',views.edit_squir),
       ]


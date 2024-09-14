from django.urls import path
from . import views
# urlCONF
urlpatterns = [
    path('hello/', views.say_hello),
]






from django.urls import path
from . import views
urlpatterns = [
 path("v1/", views.vista1, name="yonki2-v1"),
 path("v2/", views.vista2, name="yonki2-v2"),
]
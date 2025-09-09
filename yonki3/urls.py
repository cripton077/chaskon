



from django.urls import path
from . import views
urlpatterns = [
 path("v1/", views.vista1, name="yonki3-v1"),
 path("v2/", views.vista2, name="yonki3-v2"),
]

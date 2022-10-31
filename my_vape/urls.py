from django.urls import URLPattern, path

from my_vape import views


app_name = "my_vape"
urlpatterns = [
    path("vapes", views.vapes, name="vape-list")
]

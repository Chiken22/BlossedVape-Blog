from django.urls import URLPattern, path

from brand import views


app_name = "brand"
urlpatterns = [
    path("brands", views.brands, name="brand-list")
]

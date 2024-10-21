from django.urls import path
from .views import container_list, container_create, container_update, container_delete

urlpatterns = [
    path("", container_list, name="container_list"),
    path("create/", container_create, name="container_create"),
    path("update/<int:pk>/", container_update, name="container_update"),
    path("delete/<int:pk>/", container_delete, name="container_delete"),
]

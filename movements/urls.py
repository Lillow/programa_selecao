from django.urls import path
from .views import movement_list, movement_create, movement_update, movement_delete

urlpatterns = [
    path("", movement_list, name="movement_list"),
    path("create/", movement_create, name="movement_create"),
    path("update/<int:pk>/", movement_update, name="movement_update"),
    path("delete/<int:pk>/", movement_delete, name="movement_delete"),
]

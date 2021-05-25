from django.urls import path
from main import views

urlpatterns = [
	path('', views.todos, name="todo"),
	path('todo/<id>/delete', views.delete_todo, name="delete"),
	path('todo/<id>/edit', views.edit_todo, name="edit_todo"),
]

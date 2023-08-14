from django.urls import path
from .views import (AllCreateTodoView,DetailApiView,GetByDateApiView,UpdateApiView,DeleteApiView)

urlpatterns = [
    path('',AllCreateTodoView.as_view()),
    path('update/<int:pk>/',UpdateApiView.as_view()),
    path('delete/<int:pk>/',DeleteApiView.as_view()),
    path('detail/<int:pk>/',DetailApiView.as_view())
]


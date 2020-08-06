from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ListNote.as_view()),
    path('<int:pk>/', views.DetailNote.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]
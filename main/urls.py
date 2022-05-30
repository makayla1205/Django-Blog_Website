from django.urls import path

from . import views
app_name = 'main'

urlpatterns = [
    path('', views.list, name='index'),
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]

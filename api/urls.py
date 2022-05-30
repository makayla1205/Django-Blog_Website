from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('post-list/', views.apiList, name='post-list'),
    path('post-detail/<int:pk>', views.apiDetail, name='post-detail'),
    path('post-create/', views.apiCreate, name='post-create'),
    path('post-update/<int:pk>', views.apiUpdate, name='post-update'),
    path('post-delete/<int:pk>', views.apiDelete, name='post-delete'),
]
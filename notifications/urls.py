from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.alerts_view, name='alerts'),
    path('unread/', views.unread_notifications, name='unread'),
    path('<int:notification_id>/read/', views.mark_as_read, name='mark_as_read'),
    path('<int:notification_id>/delete/', views.delete_notification, name='delete'),
]


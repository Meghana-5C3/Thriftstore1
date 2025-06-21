# notifications/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def alerts_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/alert_box.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notif = get_object_or_404(Notification, id=notification_id, user=request.user)
    notif.read = True
    notif.save()
    return redirect('notifications:alerts')

@login_required
def delete_notification(request, notification_id):
    notif = get_object_or_404(Notification, id=notification_id, user=request.user)
    notif.delete()
    return redirect('notifications:alerts')

@login_required
def unread_notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False).order_by('-created_at')
    return render(request, 'notifications/alert_box.html', {'notifications': notifications})

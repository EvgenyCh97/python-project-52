from django.urls import path, include
from task_manager.users.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='users'),
]

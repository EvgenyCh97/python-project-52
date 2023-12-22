from django.urls import path, include
from task_manager.users.views import (IndexView, UserFormUpdateView,
                                      UserFormDeleteView)

urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('<int:id>/update/', UserFormUpdateView.as_view(), name='user_update'),
    path('<int:id>/delete/', UserFormDeleteView.as_view(), name='user_delete'),
]

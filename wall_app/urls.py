from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_message', views.post_message),
    path('delete/<int:id>', views.delete_comment),
    path('add_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
]
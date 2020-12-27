from django.db import models
from login_app.models import User

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name = 'user_messages', on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name = 'liked_posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name = 'user_comments', on_delete = models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name = 'post_comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)




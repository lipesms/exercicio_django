from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')

    def __str__(self):
        return f'{self.user.first_name or "comentario"} - {self.post.title}'   

    class Meta:
        ordering=['-created_at']

        verbose_name = 'comment'
        verbose_name_plural = 'comments'

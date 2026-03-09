from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import Category

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        return self.title
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'content'], name="unique_post"),
        ]
        indexes = [
            models.Index(fields=["title"], name="post_index")
        ]
        ordering = ['-created_at']

        verbose_name = 'post'
        verbose_name_plural = 'posts'
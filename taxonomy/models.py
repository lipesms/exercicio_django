from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name","slug"], name="unique_category")
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name","slug"], name="unique_tag")
        ]
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


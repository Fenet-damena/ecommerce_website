from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.title
class product(models.Model):
    user=models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)
    category=models.ForeignKey(category,related_name='product',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    description=models.TextField(max_length=50)
    price=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
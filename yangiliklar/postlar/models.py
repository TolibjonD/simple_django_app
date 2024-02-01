from django.db import models

# Create your models here.
class Postlar(models.Model):
    sarlavha = models.CharField(max_length = 300)
    post_matni = models.TextField()
    post_rasmi = models.ImageField(upload_to="post/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha
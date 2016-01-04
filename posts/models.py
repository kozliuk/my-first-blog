from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
	title = models.TextField(max_length=100)
	text = models.TextField()
	author = models.ForeignKey(User, null=True,default='k3n0b1',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta():
		verbose_name='Posts'
		verbose_name_plural ='Posts'
		ordering = ['-created_at']
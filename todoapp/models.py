from django.db import models
from django.contrib.auth.models import User

class CModel(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	task = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True,null=True,editable=False)

	def __str__(self):
		return self.task 
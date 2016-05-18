from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Soldier(models.Model):
	name = models.CharField(max_length=30)
	soldier_type = models.CharField(max_length=50)

	# def join_army(self):
	# 	pass

	def __str__(self):
		return self.name + '-' + self.soldier_type
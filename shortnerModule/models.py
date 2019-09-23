from django.db import models

# Create your models here.

class ShortUrl(models.Model):
	short_url = models.CharField(max_length = 20)
	long_url = models.URLField("URL", unique = True)

class ToDoItem(models.Model):
	content = models.TextField(null = False, blank = False)
	author = models.CharField(max_length = 120)

class Library(models.Model):
	title = models.CharField(max_length = 120)
	author = models.CharField(max_length = 120)
	document = models.FileField(upload_to = 'library/document')
	cover = models.ImageField(upload_to = 'library/cover', null = True, blank = True)

	def __str__(self):
		return self.title
	

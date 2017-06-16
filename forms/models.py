from django.db import models

# Create your models here.
class Record(models.Model):
	name=models.CharField(max_length=255)
	contact=models.IntegerField(max_length=10)
	ptm=models.CharField(max_length=255)
	companyName=models.CharField(max_length=255)
	eMail=models.CharField(max_length=250)
 	ptmContact=models.IntegerField(max_length=10)

 	def __str__(self):
 		return "name is:"+self.name 
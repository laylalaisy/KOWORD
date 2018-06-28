# _*_ encoding:utf-8 _*_

from django.db import models

class Account(models.Model):
	'''
	Account(username varchar(20) primary key, password varchar(32) not null)
	: password add salt
	'''
	username = models.CharField(max_length=20, primary_key=True)
	password = models.CharField(max_length=32, null=Talse)
	# salt=models.CharField(max_length=8, null=False, default="12345678")

	def save(self, *args, **kwargs):
		'''
		save account's username and password
		'''
		print("Account Saved")
		super(Account, self).save(*args, **kwargs)
from django.db import models
from django import forms

# Create your models here.

class Asset_Submission_Model(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    assets = models.CharField(max_length=200)
    manager=models.CharField(max_length=200)
    asset_serialno=models.CharField(max_length=200)
    issuedate=models.DateField()
    accesstype=models.CharField(max_length=200)
    approval_status=models.BooleanField(default="False")

    def approvals(username):
        # print (username)
        posts = asset_submission.objects.filter(approval_status=False,manager=username),
        # print (posts[0].fname)
        return (posts[0])

    
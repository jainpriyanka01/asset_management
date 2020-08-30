from django.db import models
from django import forms
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your models here.

class Asset_Submission_Model(models.Model):
    
    username=models.CharField(max_length=200,default="")
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    assets = models.CharField(max_length=200)
    manager_name=models.CharField(max_length=200,default='')
    manager_email=models.CharField(max_length=200,default='')
    asset_serialno=models.CharField(max_length=200)
    issuedate=models.DateField()
    accesstype=models.CharField(max_length=200)
    approval_status=models.CharField(max_length=200,default="Pending")
    keyboard=models.BooleanField("keyboard",default="False")
    mouse=models.BooleanField("mouse",default="False")
    headset=models.BooleanField("headset",default="False")
    email=models.CharField(max_length=200,default="")
    
    
    def add_assets_form_model(request):
        access_types=[]
        assets_types=[]
        username=(request.user)
        email=request.user.email
        first_name=request.POST['fname']
        last_name=request.POST["lname"]
        designation=request.POST["designation"]
        location=request.POST["location"]
        asset_type=request.POST["assets"]
        manager_name=request.POST["manager"]
        manager_email=request.POST["manager_email"]
        asset_serialno=request.POST["asset_serialno"]
        issuedate=request.POST["issuedate"]
        # accesstype=request.POST["accesstype"]
        keyboard=request.POST.get('assets1')
        mouse=request.POST.get('assets2')
        headset=request.POST.get('assets3')

        if (keyboard):
            assets_types.append(keyboard)
        if (mouse):
            assets_types.append(mouse)
        if (headset):
            access_types.append(headset)


        access1=request.POST.get('access1')
        access2=request.POST.get('access2')
        access3=request.POST.get('access3')
        access4=request.POST.get('access4')
        access5=request.POST.get('access5')


        if (access1):
            access_types.append(access1)
        if (access2):
            access_types.append(access2)
        if (access3):
            access_types.append(access3)
        if (access4):
            access_types.append(access4)
        if (access5):
            access_types.append(access5)
        

        # data=Asset_Submission_Model(email=email,fname=first_name,lname=last_name,designation=designation,location=location,assets=assets_types,manager_name=manager_name,manager_email=manager_email,asset_serialno=asset_serialno,issuedate=issuedate,keyboard=keyboard,mouse=mouse,headset=headset,accesstype=access_types)
        data=Asset_Submission_Model(email=email,fname=first_name,lname=last_name,designation=designation,location=location,assets=assets_types,manager_name=manager_name,manager_email=manager_email,asset_serialno=asset_serialno,issuedate=issuedate,accesstype=access_types)
        data.save()


        subject='A request has been raised for ypur approval'
        message=first_name + 'with email: ' + email + ' has raised a request to submit an asset'
        from_email=settings.EMAIL_HOST_USER
        # print (manager_email)
        to_list=[manager_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        # send_mail(subject,message,from_email,to_list)
        # # return render(request ,'addassets.html',{'username': username})
        
        results = Asset_Submission_Model.objects.filter(email=email)
        context = {'username': username,
                    'results':results
                }
        return (context)

    
   
    def approvals_model(username):
        # print (username)
        posts = Asset_Submission_Model.objects.filter(approval_status="Pending",manager_name=username),
        print (posts[0].fname)
        return (posts[0])

    def logout_model(request):
        auth.logout(request)

    # def ApprovalsModel(request):
    #     username = (request.user)
    #     results = Asset_Submission_Model.approvals(username)
    #     context = {'results': results}
    #     return (context)


    def dashboard_model(request):
        posts = Asset_Submission_Model.objects.all()
        return (posts)

    def approved_model(request):
        id_user=request.GET['id']
        posts = Asset_Submission_Model.objects.filter(id=id_user).update(approval_status="Approved")
        message="Approved!"
        return (message)

    def rejected_model(request):
        id_user=request.GET['id']
        posts = Asset_Submission_Model.objects.filter(id=id_user).update(approval_status="Rejected")
        message='Rejected!'
        return (message)

    def add_assets_model(request):
        username=(request.user)
        super_user=request.user.is_superuser
        fname=(request.user.first_name)
        lname=(request.user.last_name)
        email=(request.user.email)
        print (username)
        context = {'username': username,
                    'fname':fname,
                    'lname':lname,
                    'superuser':super_user,
                    'email':email}
        return (context)


    
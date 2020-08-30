from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from .models import Asset_Submission_Model
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    username=request.user
    email=request.user.email
    results = Asset_Submission_Model.objects.filter(email=email)
    return render(request, 'selfserviceportal.html', {'username': username,'results':results})



def add_assets_view(request):
    context = Asset_Submission_Model.add_assets_model(request)
    return render(request ,'addassets.html',context)

def add_assets_form_view(request):
    context = Asset_Submission_Model.add_assets_form_model(request)
    return render(request, 'selfserviceportal.html', context)



def search_view(request):
    print (request.method)
    laptops=Asset_Submission_Model.objects.filter(assets='laptop').count()
    desktops=Asset_Submission_Model.objects.filter(assets='desktop').count()
    print (laptops)
    if request.method == 'GET':
        query= request.GET.get('q')
        # print(query)
        submitbutton= request.GET.get('submit')
        
        if query is not None:
               
            if query != "":   
                lookups= Q(fname=query)  | Q(lname=query)| Q(designation=query) | Q(location=query) | Q(assets=query)
                
                results= Asset_Submission_Model.objects.filter(lookups).distinct()
                count=Asset_Submission_Model.objects.filter(lookups).distinct().count()
                print(count)
                context={'results': results,
                        'laptops':laptops,
                        'desktops':desktops,
                        'submitbutton': submitbutton,
                        'count':count
                        }

                return render(request, 'searchassets.html', context)
            else:
                
                results= Asset_Submission_Model.objects.all()
                count=Asset_Submission_Model.objects.all().count()
                print (count)
                context={'results': results,
                     'laptops':laptops,
                     'desktops':desktops,
                     'submitbutton': submitbutton,
                     'count':count
                     }

                return render(request, 'searchassets.html', context)

        else:
            print ("None")
            context={
                     'laptops':laptops,
                     'desktops':desktops,
                     }
            print ('in else')
            return render(request, 'searchassets.html',context)

    else:
        return render(request, 'index.html')

def register_view(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print ('Username already exists')
               
                messages.info(request,'Username already exists')
                return redirect ('register_view')
            elif User.objects.filter(email=email).exists():
                print ("Email ID already registered")
                messages.info(request,'Email ID already registered')
                return redirect ('register_view')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User Created')
                print ("User Created")
                return redirect('login_view')
        else:
            print ('Password didn\'t match')
            messages.info(request,'Password didnt match')
            return redirect ('RegisterView')
        return redirect('dashboard_view')
    else:    
        return render(request,'register.html')



def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
                id=user.id
                print (user.id)
                email=user.email
                results = Asset_Submission_Model.objects.filter(email=email)
                # return redirect("dashboard")
                # send_mail(subject,message,from_email,to_list,fail_silently=true)
                print (settings.EMAIL_HOST_USER)
                print (settings.EMAIL_HOST_PASSWORD)
                subject='Thankyou'
                message='Hello'
                from_email=settings.EMAIL_HOST_USER
                to_list=['jainpriyanka01@yahoo.com']
                # send_mail(subject,message,from_email,to_list)
                return render(request, 'selfserviceportal.html', {'username': username,'results':results})
            else:
                username=(request.user)
                email=(request.user.email)
                # return redirect ("/assets/addassets")
                results = Asset_Submission_Model.objects.filter(email=email)
                return render(request, 'selfserviceportal.html', {'username': username,'results':results})
                # return render(request, 'addassets.html', {'username': username})
        else:
            messages.info(request,'invalid credentials')
            return redirect ('login_view')
    else:
        return render(request,'login.html')


def logout_view(request):
    Asset_Submission_Model.logout_model(request)
    return redirect('login_view')
  
# @login_required(login_url='login')

def approvals_view(request):
    results = Asset_Submission_Model.approvals_model(request)
    context = {'results': results}
    return render(request, 'approvals.html', context)

def dashboard_view(request):
    posts = Asset_Submission_Model.dashboard_model(request)
    return render(request, 'searchassets.html', {'posts': posts})

def approved_view(request):
    message = Asset_Submission_Model.approved_model(request)
    return render(request, 'approvals.html', {'message': message})

def rejected_view(request):
    message = Asset_Submission_Model.rejected_model(request)
    return render(request, 'approvals.html', {'message': message})

def password_reset(request):
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


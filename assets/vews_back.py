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
def HomeView(request):
    username=request.user
    email=request.user.email
    results = Asset_Submission_Model.objects.filter(email=email)
    return render(request, 'selfserviceportal.html', {'username': username,'results':results})



def AddAssetsView(request):
    username=(request.user)
    super_user=request.user.is_superuser
    fname=(request.user.first_name)
    lname=(request.user.last_name)
    email=(request.user.email)
    print (super_user)
    return render(request ,'addassets.html',{'username': username,'fname':fname,'lname':lname,'superuser':super_user,'email':email})

def AddAssets_FormView(request):
    access_types=[]
    assets_types=[]
    print ("Form is submitted")
    username=(request.user)
    email=request.user.email
    print (username)
    # records=request.Get["assets"]
    first_name=request.POST['fname']
    print (first_name)
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
    # if (headset):
    #     access_types.append(headset)


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
    print(access_types)
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
    # print (email)
    return render(request, 'selfserviceportal.html', {'username': username,'results':results})



def SearchView(request):
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

def RegisterView(request):
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
                return redirect ('RegisterView')
            elif User.objects.filter(email=email).exists():
                print ("Email ID already registered")
                messages.info(request,'Email ID already registered')
                return redirect ('RegisterView')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User Created')
                print ("User Created")
                return redirect('LoginView')
        else:
            print ('Password didn\'t match')
            messages.info(request,'Password didnt match')
            return redirect ('RegisterView')
        return redirect('DashboardView')
    else:    
        return render(request,'register.html')
def LoginView(request):
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
            return redirect ('LoginView')
    else:
        return render(request,'login.html')
def LogoutView(request):
    Asset_Submission_Model.LogoutModel(request)
    return redirect('LoginView')
  
# @login_required(login_url='login')

def ApprovalsView(request):
    context = Asset_Submission_Model.ApprovalsModel(request)
    # username=(request.user)
    # results = Asset_Submission_Model.approvals(username)
    # context={'results': results}
    return render(request, 'approvals.html', context)

def DashboardView(request):
    # user = User.objects.get(username=request.user)
    # print (user)
    posts = Asset_Submission_Model.objects.all()
    print (posts)
    return render(request, 'searchassets.html', {'posts': posts})

def approved(request):
    print (request.method)
    fname=request.GET['id']
    print (fname)
    posts = Asset_Submission_Model.objects.filter(id=fname).update(approval_status="Approved")
    message="Approved!"
    return render(request, 'approvals.html', {'message': message})

def rejected(request):
    print (request.method)
    fname=request.GET['id']
    print (fname)
    posts = Asset_Submission_Model.objects.filter(id=fname).update(approval_status="Rejected")
    # posts.save()
    # user = User.objects.get(username=request.user)
    # posts = Model.objects.filter(id=id).update(field=F('field') +1))
    # print (posts)
    # return render(request, 'approvals.html')

    # Entry.objects.filter(headline__contains='Lennon').count()
def password_reset(request):
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


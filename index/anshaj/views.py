from django.shortcuts import render,redirect
from .models import job_post,applyed_candidates,imp_messages,job_category,Interview_attended_datas,Shortlisted
from django.db.models import Q
from django.contrib import messages
import json
from django.http import HttpResponse
from django.http import JsonResponse 

# Create your views here.


def index(request):
    jobpost        =   job_post.objects.all()
    return render(request,'anshaj/index.html',{'jobpost':jobpost})


def aboutus(request):
    return render(request,'anshaj/about-us.html')


def contact(request):
    return render(request,'anshaj/contact.html')


def category(request):
    return render(request,'anshaj/category.html')


def postjob(request):
    
    if request.method   ==  'POST':
        
        title       = request.POST.get("title")
        company_name= request.POST.get("company_name")
        des         = request.POST.get("des")
        job_nature  = request.POST.get("job_nature")
        location    = request.POST.get("location")
        salary      = request.POST.get("salary")
        tag_1       = request.POST.get("tag_1")
        tag_2       = request.POST.get("tag_2")
        tag_3       = request.POST.get("tag_3")
        img         = request.FILES.get("img")
        datetime    = request.POST.get("datetime")
        code        = request.POST.get("code")
        job_cat     = request.POST.get("job_category")
        # imm         = request.POST.get("immediate")

        postjob                 = job_post()
        postjob.img             = img
        postjob.title           = title
        postjob.company_name    = company_name
        postjob.des             = des
        postjob.job_nature      = job_nature
        postjob.location        = location
        postjob.salary          = salary
        postjob.tag_1           = tag_1
        postjob.tag_2           = tag_2
        postjob.tag_3           = tag_3
        postjob.datetime        = datetime
        postjob.code            = code
        postjob.job_category    = job_cat
        # postjob.immediate       = imm
        
        postjob.save()
        messages.info(request,'Job Posting Successful')
        return redirect('postjob')

    else:
        job_cat           =   job_category.objects.all()
        applyed_candi     =   applyed_candidates.objects.all()
        job_poste        =    job_post.objects.all()

        return render(request,'anshaj/postjob.html',{'applyed_candidates':applyed_candi,'job_cat':job_cat,'job_posted':job_poste})


def search(request):
    
    if request.method       ==  'POST':

        search_title       = request.POST['title']
        
        if search_title:
            print('/////////////////////////////////////////')
            match       = job_post.objects.filter(Q(title__icontains=search_title))

            if match:
                return render(request,'anshaj/search.html',{'match':match})
                
            else:
                messages.info(request,'Search was not found')
                return redirect('index')

        else:
            messages.info(request,'Please enter any value')
            return redirect('index')
    
    else:
        return render(request,'anshaj/search.html')


def apply(request):

    if request.method == 'POST':

        title   = request.POST.get("apply_title")
        job     = job_post.objects.get(code=title)
        print(title,'---------------')
        return render(request,'anshaj/apply.html',{'job':job})


    else:

        return render(request,'anshaj/apply.html')


def applying(request):
    
    if request.method  ==  'POST':

        givenname       = request.POST.get("givenname")
        surename        = request.POST.get("surename")
        email           = request.POST.get("email")
        phonenumber     = request.POST.get("phonenumber")
        file            = request.FILES.get("file")
        code            = request.POST.get("code")

        applying                            = applyed_candidates()
        applying.candidates_givenname       = givenname
        applying.candidates_surename        = surename
        applying.candidates_email           = email
        applying.candidates_phonenumber     = phonenumber
        applying.code                       = code
        applying.candidates_resume          = file
        
        applying.save()
        return redirect('index')

    else:

        return render(request,'anshaj/apply.html')



def impmessage(request):

    if request.method   == 'POST':
        imp_message     = request.POST.get("imp_message")
        imp_datetime    = request.POST.get("datetime")
        
        imp             = imp_messages()
        imp.message     = imp_message
        imp.datetime    = imp_datetime

        imp.save()
        return redirect('postjob')

    else :
        imp             = imp_messages.objects.all()
        return render(request,'anshaj/postjob.html',{'imp':imp})


        
def applied_candi_by_job(request):

    
    selected_job    =   request.GET.get("xyz")
    posted_job      =   job_post.objects.get(id=selected_job)
    a               =   posted_job.code

    select_applied_candi    =   applyed_candidates.objects.filter(code=a)
    length                  =   len(select_applied_candi)

    print(length,'------------')
    print(a,'++++++++++++++++')
    print(selected_job,'----------------') 
   
    data = {
        "respond":length
    }

    return JsonResponse(data)    
    



def view_applied_datewise(request):

    if request.method == 'POST':

        date            =   request.POST['interview_date']

        if date:
            match       =  job_post.objects.filter(Q(datetime__icontains=date))
            aa          = match
            

            print(match,'------------')
            # a           =  applyed_candidates.objects.get(code=match
            if match:

                return render(request,'anshaj/postjob.html',{'match':match})

            else:
                messages.info(request,'The Date Interview was not founded')
                return redirect('postjob')

        else:
            messages.info(request,'Select any date')
            return redirect('postjob')


    else:
        return render(request,'anshaj/postjob.html')

    
    

    


def select_shortlist(request):

    if request.method == 'POST':

        givenname = request.POST.get("givenname_n")
        surename = request.POST.get("surename_n")
        email = request.POST.get("email_n")
        phonenumber = request.POST.get("phonenumber_n")
        job_code        =  request.POST.get("job_code_n")
        print(givenname,'8888888888888888888888888')

        s   =  Interview_attended_datas()
        s.candidates_givenname   =   givenname
        s.candidates_surename    =   surename
        s.candidates_email       =   email
        s.candidates_phonenumber =   phonenumber
        s.code                   =   job_code
        s.save()

        messages.info(request,'Registration Successful')
        return redirect('select_shortlist')

    else:
        

        jobpost         =  job_post.objects.all()
        Interview_attended    =  Interview_attended_datas.objects.all()
        shortlist_view  =  Shortlisted.objects.all()

        # w   =  shortlist_view.Shortlisted_candidates_id

        # shortlist_view_other        = Interview_attended_datas.objects.filter(id=shortlist_view)
        

        return render(request,'anshaj/select_shortlist.html',{
                                                                'jobpost':jobpost,
                                                                'interview_attended':Interview_attended,
                                                                'shortlisted_view':shortlist_view,
                                                                # 'shortlist_view_other':shortlist_view_other
                                                            })



    
def select_shortlist_search(request):
    if request.method == 'POST':

        searched     =  request.POST["searched"]

        if searched:
            match   =   applyed_candidates.objects.filter(Q(candidates_phonenumber__icontains=searched))

            if match:

                return render(request,'anshaj/select_shortlist.html',{'match':match})
            
            else:

                messages.info(request,'Sorry,No result founded')
                return redirect('select_shortlist_search')
            
        else:

            messages.info(request,'please enter phone number')
            return redirect('select_shortlist_search')

    else:
        jobpost         =  job_post.objects.all()
        return render(request,'anshaj/select_shortlist.html',{'jobpost':jobpost})





def shortlisted(request):

    if request.method == 'POST':

        selected        =   request.POST.get("shortlisted")

        s  = Shortlisted()
        s.Shortlisted_candidates_id   = selected
        s.save()

        messages.info(request,'Shortlist Successful')
        return redirect('select_shortlist')

    else:
        jobpost         =  job_post.objects.all()
        shortlist_view  =  shortlisted.objects.all()
        return render(request,'anshaj/select_shortlist.html',{'jobpost':jobpost,'shortlisted_view':shortlist_view})



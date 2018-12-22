from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from .forms import NameForm
from polls.models import Users,Userrequests
from django.http import HttpResponse, HttpResponseRedirect


def submitrqst(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)
        # check whether it's valid:
        form = NameForm(request.POST)
        fcont=request.POST['fcontent']
        fn="ab"
        cn="cd"
        #lsn=request.POST['lastName']
        #usn=request.POST['username']
        #pwd=request.POST['password']
        #print(fsn)
        #print("First Name {} , Last Name {},username {},pas {}".format(fsn,lsn,usn,pwd))
        q=Userrequests(fanuname=fn,celuname=cn,fcontent=fcont)
        q.save()
       
    return render(request, 'polls/index3.html', {'form': form})

def createrqst(request):
    
    template = loader.get_template('polls/createrqst.html')
    context = {   
    }
    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('polls/profile.html')
    context = {   
    }
    return HttpResponse(template.render(context, request))

#sign up submit request
def supsub(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)
        # check whether it's valid:
        form = NameForm(request.POST)
        fsn=request.POST['firstName']
        lsn=request.POST['lastName']
        usn=request.POST['username']
        pwd=request.POST['password']
        print(fsn)
        print("First Name {} , Last Name {},username {},pas {}".format(fsn,lsn,usn,pwd))
        q=Users(firstname=fsn,lastname=lsn,username=usn,passwd=pwd)
        q.save()
       
    return render(request, 'polls/index3.html', {'form': form})


def signsub(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)
        # check whether it's valid:
        form = NameForm(request.POST)
        usn=request.POST['choice']
        b=Users.objects.get(username=usn)
        pwd=request.POST['passwd']
        if b.passwd == pwd:   #oauth
            request.session['member_id'] = b.id
            print("user logged in")
            template = loader.get_template('polls/userpage.html')
            context = {   'usnme':usn,
              }
            return HttpResponse(template.render(context,request))
       
    return render(request, 'polls/index3.html', {'form': form})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    template = loader.get_template('polls/index3.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("You're logged out.")
    # if this is a POST request we need to process the form data
   
  


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index3.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#the login page
def login(request):  
    
    template = loader.get_template('polls/signin1.html')
    context = {
        
    }
   # return render(request, 'polls/signin1.html', {'question': latest_question_list})
    return HttpResponse(template.render(context, request))

def signup(request):
    
    template = loader.get_template('polls/signup.html')
    context = {   
    }
    return HttpResponse(template.render(context, request))

def browse(request):
    
    template = loader.get_template('polls/Browse.html')
    context = {   
    }
    return HttpResponse(template.render(context, request))

def userpage(request):
    
    template = loader.get_template('polls/userpage.html')
    context = {   
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.

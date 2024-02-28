from django.shortcuts import render , HttpResponse , redirect

from django.contrib import messages
from GenAI.models import Member
import openai, os ,requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile



# Create your views here.
def index(request):
    return render(request , 'index.html')

def contact(request):
    return render(request , 'contact.html')

def signup(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        member = Member( Name=Name, Email=Email , Password=Password)
        member.save()
        return redirect('/signin')
    else:
        return render(request, 'signup.html')
    


def signin(request):
    if request.method == 'POST':
        if Member.objects.filter(Email=request.POST['Email'], Password=request.POST['Password']).exists():
            member = Member.objects.get(Email=request.POST['Email'], Password=request.POST['Password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'signin.html', context)
    else:
        return render(request , 'signin.html')
    

def home(request):
    return render(request , 'home.html')





# Creating Smart Bot 
load_dotenv()

api_key = os.getenv("OPENAI_KEY" ,None)
openai.api_key = api_key


def qa(request):
    chat = None
   
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input2= request.POST.get('user-input1')
        prompt = user_input2
      
        
        response = openai.Completion.create(
            engine = 'gpt-3.5-turbo-instruct',
            prompt = prompt,
            max_tokens = 256,
            temperature = 0.5

        )

        print(response)

        chat = response["choices"][0]["text"]

    return render(request , 'QA.html' ,{"response":chat})
   
    

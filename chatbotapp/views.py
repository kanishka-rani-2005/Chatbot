<<<<<<< HEAD
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def chatbot_view(request):
    if request.method=='POST':
        message=request.POST.get('message') # from body of fetch in html
        response = "This is a dummy response to: " + message # dummy response sending
        return JsonResponse({'message': message, 'response':response})
    return render(request, "chatbot.html")
=======
from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


GROQ_API_KEY = 'REMOVED_SECRET'
API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def ask_ai(message):
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    print(result)  # Debugging line to see the response structure
    return result['choices'][0]['message']['content']


def chatbot_view(request):
    
    if request.method=='POST':
        message=request.POST.get('message') # from body of fetch in html
        response = ask_ai(message)
        return JsonResponse({'message': message, 'response':response})
    return render(request, "chatbot.html")



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatbot')
        else:
            return render(request, "login.html", {'error_message': 'Invalid credentials'})
    return render(request, "login.html")


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not email or not password1 or not password2:
            return JsonResponse({'message': 'All fields are required'}, status=400)
        
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return render(request, "login.html", {'message': 'Registration successful,Please Log In'})
        else:
            return render(request, "register.html", {'error_message': 'Passwords do not match'})

    return render(request, "register.html")


def logout_view(request):    
    logout(request)
    return redirect('login')
>>>>>>> d7d5bd9 (Add chatbot views and API integration for user interactions)

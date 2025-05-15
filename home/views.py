from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def index(request):
    skills = ['HTML5', 'CSS3', 'JavaScript', 'Django', 'Python', 'MySQL', 'Git', 'Bootstrap']
    return render(request, 'home/index.html', {'skills': skills})


def about(request):
    skills = ['Time Management', 'Adaptability', 'Teamwork', 'Problem Solving', 'Communication', 'Learning Agility']
    return render(request, 'home/about.html', {'skills': skills})

def portfolio(request):
    return render(request, 'home/portfolio.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"From: {name} <{email}>\n\nSubject: {subject}\n\nMessage:\n{message}"
        send_mail(subject, full_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'home/contact.html')

def project1(request):
    return render(request,'home/project1.html')

def project2(request):
    return render(request,'home/project2.html')

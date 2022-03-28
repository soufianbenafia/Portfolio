import email
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from portfolio.settings import EMAIL_HOST_USER

def create(request):
    if request.method == 'POST':
            from_email = request.POST['Email']
            subject = request.POST['subject']
            message = request.POST['message']

            message = '''
            New message: {}

            subject: {}

            From: {}
            '''.format(message,subject,from_email)

            try:
                send_mail(subject, message, from_email, [EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            success = 'Success! Thank you for your message.'
            return HttpResponse(success)
    else:
        success = 'fail.'
        return HttpResponse(success)



def index(request):

    # Home
    try:
        home = Home.objects.latest('updated')
    except Home.DoesNotExist:
        home = None

    # About
    try:
        about = About.objects.latest('updated')
    except about.DoesNotExist:
        about = None

    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # form = ContactForm()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        # 'form': form
    }


    return render(request, 'index.html', context)
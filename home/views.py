from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .forms import HeroForm
from .models import Article, Hero
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# create your views here


def contactFormHandle(request):
    received = 0
    if request.method == 'POST':
        received = 1
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully submitted the your message ')
        else:
            messages.error(
                request, 'Error submitting your message. Please correct you informations'
            )
    context = {
        "form": ContactForm()
    }


def index(request):
    article_list = Article.objects.all()
    hero_list = Hero.objects.all()
    print(article_list)
    context = {
        "articles": article_list,
        "hero_list": hero_list
    }
    return render(request, 'home/index.html', context)
    # return HttpResponse("<h2>Hello, we have done it</h2>")


def contact(request):
    context = {
        "form": contactFormHandle(request)

    }
    return render(request, 'home/contact.html', context)


# @login_required(login_url='admin/')
# this is for uploading form in the hero
@login_required(login_url='/admin/login/')
def hero_create(request):
    def heroFormHandle(request):
        received = 0
        if request.method == 'POST':
            received = 1
            form = HeroForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'You have successfully submitted the your message ')
            else:
                messages.error(
                    request, 'Error submitting your message. Please correct you informations'
                )
    context = {
        "form": HeroForm()
    }
    context = {
        "form": heroFormHandle(request)
    }
    return render(request, 'home/hero.html', context)


@login_required(login_url='/admin/login/')  # this is for update in the hero
def hero_update(request, id=None):
    instance = get_object_or_404(Hero, id=id)
    form = HeroForm(request.POST or None,
                    request.FILES or None, instance=instance)
    if request.method == 'POST':
        received = 1
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully submitted the your message ')
        else:
            messages.error(
                request, 'Error submitting your message. Please correct you informations'
            )
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'home/hero.html', context)

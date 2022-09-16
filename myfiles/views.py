import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Project,Messagelar
# Create your views here.


def index(information):
    if 'matn' in information.POST:
        malumot= str(information.POST.get('matn'))
        malumot = malumot.strip()
        qidirish = Q(nomi__contains =malumot )| Q(manzil__contains =malumot )|Q(tur__nomi__contains =malumot )

        proyektlar = Project.objects.filter(qidirish)
        return render(information, 'index.html', {'pro': proyektlar})
    else:

        uzunlik = len(Project.objects.all())
        oxirigi2 = uzunlik-2
        proyektlar = Project.objects.all()[oxirigi2:]
        return render(information,'index.html',{'pro':proyektlar})

def about(information):
    return render(information,'about.html')

def blog(information):
    return render(information,'blog.html')

def contact(information):

    if information.method =="POST":
        ism = information.POST.get('name')
        familya = information.POST.get('sure')
        email = information.POST.get('mail')
        malumot = information.POST.get('text')
        vaqt = datetime.datetime.now()
        Messagelar(ism=ism,fam=familya,mail=email,matn=malumot,vaqt=vaqt).save()
    return render(information,'contact.html')

def main(information):
    return render(information,'main.html')

def project(information):
    proyektlar = Project.objects.all()
    return render(information,'project.html',{'pro':proyektlar})

def services (information):
    return render(information,'services.html')

def single(information):
    return render(information,'single.html')
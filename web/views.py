from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact, Dashboard,News,Fake,Messages, NotePad, Remote,First,Second,Third
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.contrib.auth import user_logged_in
import csv



# Create your views here.

def home(request):
    return render(request,"web/index.html")


def contact(request):
    name=request.POST["Full Name"]
    email=request.POST["Email"]
    phone=request.POST["Phone Number"]
    message=request.POST["message"]
    con=Contact(name=name, email=email,phone=phone,message=message)
    con.save()
    messages.success(request , "account created")

    return HttpResponseRedirect(reverse('home'))

def newslater(request):

    email=request.POST["Enter Your Email"]
    news=News(email=email)
    news.save()

    return HttpResponseRedirect(reverse("home"))

def dashboard(request):
    dash=Dashboard.objects.all()
    messa=Messages.objects.all()
    note=NotePad.objects.all()
    context={
        "dash":dash,
        "messa":messa,
        "note":note
    }

    return render(request,"web/dashboard.html",context )

def tables(request):
    fk=Fake.objects.all()
    context={
        "fk":fk
    }

    return render(request,"web/table.html" ,context)
def remote_table(request):
    rt=Remote.objects.all()
    context={
        "rt":rt
    }

    return render(request,"web/remote.html" ,context)

def first_table(request):
    rt=First.objects.all()
    context={
        "rt":rt
    }

    return render(request,"web/first.html" ,context)

def second_table(request):
    rt=Second.objects.all()
    context={
        "rt":rt
    }

    return render(request,"web/second.html" ,context)

def third_table(request):
    rt=Third.objects.all()
    context={
        "rt":rt
    }

    return render(request,"web/third.html" ,context)

def delete(request,id):
    obj=get_object_or_404(Fake,pk=id)
    obj.delete()
    return redirect("records")

def remote_delete(request,id):
    obj=get_object_or_404(Remote,pk=id)
    obj.delete()
    return redirect("rem")


def fake(request):
    dash=Dashboard.objects.all()
    context={
        "dash":dash
    }
    try:
        URL = "https://realpython.github.io/fake-jobs/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="ResultsContainer")
        job_elements = results.find_all("div", class_="card-content")
        dash=Dashboard(website="https://realpython.github.io/fake-jobs/",date=datetime.now(),data="Job opportunity")
        dash.save()
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")
            title=title_element.text.strip()
            company=company_element.text.strip()
            location=location_element.text.strip()

            jobs=Fake(title=title , company_element=company,location_element=location)
            jobs.save()
        
        return HttpResponseRedirect(reverse('home'),context)
    except:
        return redirect("error")


def remote(request):
    dash=Dashboard.objects.all()
    context={
        "dash":dash
    }
    try:
        source=requests.get("https://remote.co/remote-jobs/").text
        soup=BeautifulSoup(source,'lxml')
        dash=Dashboard(website="https://remote.co/remote-jobs/",date=datetime.now(),data="Job opportunity")
        dash.save()
        for job in soup.find_all("div",class_="row no-gutters align-items-center"):
            title=job.find("p",class_="m-0").text
            discript=job.find("p",class_="m-0 text-secondary").get_text()
            time=job.find("date").text
            web=job.find("a",class_="font-weight-bold larger stretched-link")['href']
            website="https://remote.co/"+web
            try:
                description=discript.split()[0] + " " + discript.split()[1] + " " + discript.split()[2] + " " + discript.split()[3] + " " + discript.split()[4] + " " + discript.split()[5]
            except:
                description=discript.split()[0] + " " + discript.split()[1] + " " + discript.split()[2] + " " + discript.split()[3] + " " + discript.split()[4]
            jobs=Remote(title=title , description=description,time_posted=time,website=website)
            jobs.save()
            
        return HttpResponseRedirect(reverse('home'),context)
    except:
        return redirect("error")

def first(request):
    dash=Dashboard.objects.all()
    context={
        "dash":dash
    }
    try:
        url="https://news.google.com/search?q=break-ground%2Bgeneral-contractor&hl=en-US&gl=US&ceid=US%3Aen"
        source=requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        web="https://news.google.com"

        for info in soup.find_all("a",class_="VDXfz"):
            link=info['href']
            lnikq=web+link[1:]
            linker=First(info="links",website=lnikq)
            linker.save()
        return HttpResponseRedirect(reverse('home'),context)
    except:
        return redirect("error")

def second(request):
    dash=Dashboard.objects.all()
    context={
        "dash":dash
    }
    try:
        url="https://news.google.com/search?q=breaking-ground%2Bgeneral-contractor&hl=en-US&gl=US&ceid=US%3Aen"
        source=requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        web="https://news.google.com"

        for info in soup.find_all("a",class_="VDXfz"):
            link=info['href']
            lnikq=web+link[1:]
            linker=Second(info="links",website=lnikq)
            linker.save()
        return HttpResponseRedirect(reverse('home'),context)
    except:
        return redirect("error")

def third(request):
    dash=Dashboard.objects.all()
    context={
        "dash":dash
    }
    try:
        url="https://news.google.com/search?q=construction%2Bbegins%2Bgeneral-contractor&hl=en-US&gl=US&ceid=US%3Aen"
        source=requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        web="https://news.google.com"

        for info in soup.find_all("a",class_="VDXfz"):
            link=info['href']
            lnikq=web+link[1:]
            linker=Third(info="links",website=lnikq)
            linker.save()
        return HttpResponseRedirect(reverse('home'),context)
    except:
        return redirect("error")

def message(request):
    messa=request.POST['messenger']
    mes=Messages(writer= user_logged_in ,time=datetime.now(),mess=messa)
    mes.save()

    return HttpResponseRedirect(reverse("dashboard"))

def note(request):

    no=request.POST['note'] 
    news=NotePad(note=no)
    news.save()

    return HttpResponseRedirect(reverse("dashboard"))

def note_delete(request,id):
    obj=get_object_or_404(NotePad,pk=id)
    obj.delete()
    return redirect("dashboard")


def csvexport(request):
    dats=Remote.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=data_export.csv'
    writer=csv.writer(response)
    writer.writerow(['title','description','time_posted','website'])
    fake_fields=dats.values_list('title','description','time_posted','website')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))

def firstcsv(request):
    dats=First.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=first.csv'
    writer=csv.writer(response)
    writer.writerow(['info','website'])
    fake_fields=dats.values_list('info','website')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))

def secondcsv(request):
    dats=Second.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=second.csv'
    writer=csv.writer(response)
    writer.writerow(['info','website'])
    fake_fields=dats.values_list('info','website')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))

def thirdcsv(request):
    dats=Third.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=third.csv'
    writer=csv.writer(response)
    writer.writerow(['info','website'])
    fake_fields=dats.values_list('info','website')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))




def error(request):
    return render(request,"web/404.html")
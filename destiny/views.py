from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .models import viewForm, popular, Plan,Home
from django.db.models import Q
from .forms import BookingForm,PlanForm
from django.http import HttpResponseRedirect

def index(request):
    pop= popular.objects.all()
    more=Home.objects.all()
    return render(request, 'index.html',   {'pop':pop,'more':more})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def destinationDetails(request):
    more = Home.objects.all()
    return render(request, 'destination_details.html', {'more':more})

def elements(request):
    more = Home.objects.all()
    return render(request, 'elements.html', {'more':more})


def main(request):
    return render(request, 'main.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def travelDestinations(request):
    return render(request, 'travel-destinations.html')


def Booking(request):
    form = BookingForm()
    if request.method=='POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'form.html',{'form':form})
    return render(request, 'form.html', {'form':form})


def plan(request):
    form = PlanForm()
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'plan.html',{'form': form})
    return render(request,'plan.html',{'form':form})



def flight(request):
    return render(request, 'Flight.html')
def nissan(request):
    list = viewForm.objects.all()
    more=Home.objects.all()
    return render(request,'Nissan.html', {'list':list,'more':more})
def private(request):
    list = viewForm.objects.all()
    more = Home.objects.all()
    return render(request, 'Private.html', {'list': list, 'more':more})
def bus(request):
    list = viewForm.objects.all()
    return render(request, 'Bus.html',{'list': list})

def form(request):
    submitted =  False
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'form.html', {'form':form, 'submitted':submitted})

def flight_list(request):
    list= viewForm.objects.all()
    return render(request,'Flight.html', {'list':list})

def popularContent(request):
    return render(request,'addDest.html')

def addDest(request):
    form=AddDestForm()
    if request.method == 'POST':
        form=AddDestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'save successfully')
            return redirect('/')
        return render(request,'addDest.html',{'form':form})
    return render(request,'addDest.html',{'form': form})

def editDest(request,pk):
    po= popular.objects.get(id=pk)
    form=EditDestForm(instance=po)

    if request.method == 'POST':
        form=EditDestForm(request.POST,instance=po)
        if form.is_valid():
            form.save()
            messages.success(request,'Update successfully')
            return redirect('/')
        return render(request,'editDest.html',{'form':form})
    return render(request,'editDest.html',{'form': form})

def delete(request,pk):
    pop= popular.objects.get(id=pk)
    pop.delete()
    return redirect('/')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            lst = viewForm.objects.all().filter(Q(title__icontains=query) | Q(flightNo__icontains=query))
            return render(request,'searchbar.html',{'list': lst})

        return render(request,'searchbar.html')

def explore(request):
    return render(request,'Explore.html')

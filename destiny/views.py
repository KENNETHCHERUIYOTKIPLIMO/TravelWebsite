
from django.shortcuts import render, redirect

from .forms import BookingForm
from .models import viewForm, popular

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def destinationDetails(request):
    return render(request, 'destination_details.html')

def elements(request):
    return render(request, 'elements.html')


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
    return render(request, 'plan.html')

def flight(request):
    return render(request, 'Flight.html')
def nissan(request):
    return render(request, 'Nissan.html')
def private(request):
    return render(request, 'Private.html')
def bus(request):
    return render(request, 'Bus.html')

def form(request):
    return render(request, 'form.html')

def flight_list(request):
    list= viewForm.objects.all()
    return render(request,'Flight.html', {'list':list})

def popularContent(request):
    content=popular.objects.all()
    return render(request,'index.html', {'content':content})


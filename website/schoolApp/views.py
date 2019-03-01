from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Timecard
from .forms import NewTimecard

def index(request):
    allcards = Timecard.objects.all()
    return render(request, 'schoolApp/index.html', {'timecard': allcards})


def timecard(request):
    new_card = NewTimecard(request.POST or None)
    if new_card.is_valid():
        new_card.save()
        return redirect('index')

    return render(request, 'schoolApp/timecard.html', {'newcard': new_card})

def editcard(request, id):
    teacherName = get_object_or_404(Timecard, pk=id)
    edit_card = NewTimecard(request.POST or None, instance=teacherName)
    if edit_card.is_valid():
        edit_card.save()
        return redirect('index')
    return render(request, 'schoolApp/timecard.html', {'newcard': edit_card})

def deletecard(request, id):
    user = get_object_or_404(Timecard, pk=id)
    if request.method == "POST":
        user.delete()
        return redirect('index')
    return render(request, 'schoolApp/delete.html', {'seletedcard':timecard})
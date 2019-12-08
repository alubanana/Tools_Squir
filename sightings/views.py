from django.shortcuts import render
import random
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

def all_squir(request):

    squirrels = Squirrel.objects.all()
    context = {
             'squirrels':squirrels,
            }
    return render(request, 'sightings/all.html',context)
    #return HttpResponse(text)

def squir_stats(request):
    
    squirrels = Squirrel.objects.all()
    AM_count = 0
    Age_count = 0
    Loc_count = 0
    Eat_count = 0
    Runs_count = 0
    total = 0
    for s in squirrels:
        total += 1
        if s.shift == 'AM':
            AM_count += 1
        if s.age == 'Juvenile':
            Age_count +=1
        if s.location == 'Ground Plane':
            Loc_count +=1
        if s.eating is True:
            Eat_count +=1
        if s.running is True:
            Runs_count +=1        
    AM = AM_count/total
    Age = Age_count/total
    Loc = Loc_count/total
    Eat = Eat_count/total
    Runs = Runs_count/total
    
    
    context = {
            'squirrels':squirrels,
            'total':total,
            'AM_count':AM_count,
            'Age_count':Age_count,
            'Loc_count':Loc_count,
            'Eat_count':Eat_count,
            'Runs_count':Runs_count,
            'AM':AM,
            'Age':Age,
            'Loc':Loc,
            'Eat':Eat,
            'Runs':Runs,
            
            }
    
    return render(request, 'sightings/stats.html',context)




def edit_squir(request, uid):
    squir = get_object_or_404(Squirrel, pk=uid)
    if request.method == 'POST':
        # check data with form
        form = SquirrelForm(request.POST, instance = squir)
        if  form.is_valid():
            form.save()
            return redirect(f'/sightings/{uid}')
    else:
        form  = SquirrelForm(instance = squir)
        # build empty form
    context = {
            'form':form,
            }
    return render(request, 'sightings/edit.html',context)

def add_squir(request):
    if request.method == 'POST':
        # check data with form
        form = SquirrelForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form  = SquirrelForm()
        # build empty form
    context = {
            'form':form,
            }
    return render(request, 'sightings/edit.html',context)




def map_squir(request):
    
    sightings = Squirrel.objects.all()
    sightings = random.choices(sightings, k=100)   #randomly choose 100 squirrels so as to avoid overload

    context = {
        'sightings': sightings,
    }
    
    
    return render(request, 'sightings/map.html', context)
# Create your views here.

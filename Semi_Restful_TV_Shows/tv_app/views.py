from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

# Root
def index(request):
    return redirect('/shows')

# All Shows
def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'allShows.html', context)

# New Shows
def showNew(request):
    return render(request, 'showNew.html')

# Add
def add(request):
    Show.objects.create(title=request.POST['title'],network=request.POST['network'],release=request.POST['date'],desc=request.POST['desc'])
    context = {
        'show': Show.objects.last()
    }
    return render(request, 'showShow.html', context)


# Edit Shows
def showEdit(request, num):
    context = {
        'show': Show.objects.get(id=num)
    }
    return render(request, 'showEdit.html', context)

# Update
def update(request, num):
    print(
        request.POST['title'],
        request.POST['network'],
        request.POST['date'],
        request.POST['desc'],
    )
    c = Show.objects.get(id=num)
    c.title=request.POST['title']
    c.network=request.POST['network']
    c.release=request.POST['date']
    c.desc=request.POST['desc']
    c.save()
    context = {
        'show': Show.objects.get(id=num)
    }
    return render(request, 'showShow.html', context)

# Show Shows
def showShow(request, num):
    context = {
        'show': Show.objects.get(id=num)
    }
    return render(request, 'showShow.html', context)

# Delete Shows
def showDelete(request, num):
    c = Show.objects.get(id=num)
    c.delete()
    return redirect('/shows')
    
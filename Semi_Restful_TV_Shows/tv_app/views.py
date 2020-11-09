from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

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
    Box = request.POST
    print(Box)
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release=request.POST['new_date'],
        desc=request.POST['desc']
    )
    num = Show.objects.last().id
    num = str(num)
    return redirect('/shows/'+num)
    # print(request.POST)
    # errorM = Show.objects.validMake(request.POST)
    # if len(errorM) == 0:
    #     print('No errors')
    #     print(request.POST['title'],request.POST['network'],request.POST['new_date'],request.POST['desc'],)
    #     # Show.objects.create(
    #     #     title=request.POST['title'],
    #     #     network=request.POST['network'],
    #     #     release=request.POST['new_date'],
    #     #     desc=request.POST['desc']
    #     # )
    #     # num = Show.objects.last().id
    #     # num = str(num)
    #     return redirect('/shows/9')
    # else:
    #     print(request.POST['title'],request.POST['network'],request.POST['new_date'],request.POST['desc'],)
    #     print('There are', len(errorM), 'ERRORS!!!')
    #     for key, val in errorM.items():
    #         print(key, val)
    #         messages.error(request, val)
    #     return redirect('/shows/new/add')


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
    errors = Show.objects.validate(request.POST)
    reNum = str(num)
    if len(errors) > 0:
        print('There are', len(errors), 'ERRORS!!!')
        for key, val in errors.items():
            print(key, val)
            messages.error(request, val)
        return redirect('/shows/'+reNum+'/edit')
    else:
        print('No errors')
        c = Show.objects.get(id=num)
        c.title=request.POST['title']
        c.network=request.POST['network']
        c.release=request.POST['date']
        c.desc=request.POST['desc']
        c.save()
        num = str(num)
    return redirect('/shows/'+num)

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
    
from django.shortcuts import render, redirect

# Create your views here.

# Root
def index(request):
    return redirect('/shows')

# All Shows
def shows(request):
    return render(request, 'allShows.html')

# New Shows
def showNew(request):
    return render(request, 'showNew.html')

# Edit Shows
def showEdit(request):
    return render(request, 'showEdit.html')

# Show Shows
def showShow(request):
    return render(request, 'showShow.html')
from django.shortcuts import render
from main.models import Animals
from main.forms import KommentForm
from main.models import KommentModel


def index(request):
    return render(request, 'index.html')

def komment(request):
    komment = KommentModel.objects.all()
    if request.method == "POST":
        form = KommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = KommentForm()

    else:
        form = KommentForm()
    return render(request,'komment.html', {'komments':komment, 'komment_form':form})

def list(request):
    animals = Animals.objects.all()
    context = {'animals_list': animals}
    return render(request, 'list.html', context)


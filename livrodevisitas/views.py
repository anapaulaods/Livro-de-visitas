from django.shortcuts import render
from django.shortcuts import render
from .models import Recado
from django.http import HttpResponse
from .forms import RecadoForm

# Create your views here.
def index(request):
    return render(request, 'livrodevisitas/index.html', {})

def recado_new(request): 
    form = RecadoForm()      
    return render(request, 'livrodevisitas/index.html', {'form': form})


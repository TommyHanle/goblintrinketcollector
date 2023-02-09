from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trinket
from .forms import UsesForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trinkets_index(request):
  return render(request, 'trinkets/index.html', {
    'trinkets': trinkets
})

def trinkets_index(request):
  trinkets = Trinket.objects.all()
  return render(request, 'trinkets/index.html', { 'trinkets': trinkets })

def trinkets_detail(request, trinket_id):
  trinket = Trinket.objects.get(id=trinket_id)
  uses_form = UsesForm()
  return render(request, 'trinkets/detail.html', {
    'trinket': trinket, 'uses_form': uses_form
  })

def add_uses(request, trinket_id):
  form = UsesForm(request.POST)
  if form.is_valid():
    new_uses = form.save(commit=False)
    new_uses.trinket_id = trinket_id
    new_uses.save()
  return redirect('detail', trinket_id=trinket_id)

class TrinketCreate(CreateView):
  model = Trinket
  fields = '__all__'

class TrinketUpdate(UpdateView):
  model = Trinket
  fields = '__all__'

class TrinketDelete(DeleteView):
  model = Trinket
  success_url = '/trinkets'
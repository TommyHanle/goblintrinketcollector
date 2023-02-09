from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trinket, Merchant
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
  id_list = trinket.merchants.all().values_list('id')
  merchants_trinket_doesnt_have = Merchant.objects.exclude(id__in=id_list)
  uses_form = UsesForm()
  return render(request, 'trinkets/detail.html', {
    'trinket': trinket, 'uses_form': uses_form,
    'merchants': merchants_trinket_doesnt_have
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

def merchants_index(request):
    merchants = Merchant.objects.all()
    return render(request, 'merchants/index.html', {'merchants': merchants})

def merchants_detail(request, merchant_id):
    merchant = Merchant.objects.get(id=merchant_id)
    return render(request, 'merchants/detail.html', {'merchant': merchant})

class MerchantList(ListView):
  model = Merchant

class MerchantDetail(DetailView):
  model = Merchant

class MerchantCreate(CreateView):
  model = Merchant
  fields = '__all__'

def assoc_merchant(request, trinket_id, merchant_id):
    Trinket.objects.get(id=trinket_id).merchants.add(merchant_id)
    return redirect('detail', trinket_id=trinket_id)

def unassoc_merchant(request, trinket_id, merchant_id):
    Trinket.objects.get(id=trinket_id).merchants.remove(merchant_id)
    return redirect('detail', trinket_id=trinket_id)
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.decorators.http import require_POST
from .models import Keys
from .forms import NewKeyForm
from django.db.models import Sum
from django.utils import timezone
from django.utils.decorators import method_decorator
from django import forms

import json

def KeyCode(request):
    return render(request, 'feed/keyCode.html')

def PrintOptions(request):
    return render(request, 'feed/print.html')

class StockListView(ListView):
    model = Keys
    template_name = 'feed/stock.html'
    context_object_name = 'keys'
    ordering = ['name']
    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('p')
        for key in context['keys']:
            key.total = key.saran  + key.minda + key.madin
        if(not query):
            return context
        keys_list = Keys.objects.filter(name__icontains=query)
        for key in keys_list:
            key.total = key.saran  + key.minda + key.madin
        context['keys_list'] = keys_list
        return context

def key_detail(request, pk):
    key = get_object_or_404(Keys, pk=pk)
    total = key.saran  + key.minda + key.madin
    return render(request, 'feed/key_detail.html', {'key':key, 'total':total})

def create_post(request):
    user = request.user
    if request.method == "POST":
        form = NewKeyForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            messages.success(request, f'Posted Successfully')
            return redirect('stock')
    else:
        form = NewKeyForm()
    return render(request, 'feed/create_post.html', {'form':form})

def key_update(request, pk):    
    user = request.user
    if pk:
        post = get_object_or_404(Keys, id=pk)
    else:
        post = None
    if request.method == "POST":
        form = NewKeyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            messages.success(request, 'Post Updated Successfully' if post else 'Posted Successfully')
            return redirect('stock')
    else:
        form = NewKeyForm(instance=post)
    
    return render(request, 'feed/create_post.html', {'form': form})

def key_delete(request, pk):
    key = Keys.objects.get(pk=pk)
    key.delete()
    return redirect('stock')

def search(request):
    query = request.GET.get('p')
    if(not query):
        return redirect('stock')
    keys_list = Keys.objects.filter(name__icontains=query)
    context ={
        'keys_list': keys_list,
    }
    return render(request, "feed/stock.html", context)
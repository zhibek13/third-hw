from django.shortcuts import render, get_object_or_404
from .models import Client, Account, Credit
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class DetailView(generic.DetailView):
    model = Account
    model2 = Credit
    template_name = 'detail.html'

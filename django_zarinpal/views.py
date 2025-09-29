from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView,DetailView
from .models import Transaction, TransactionStatus
from .zarinpal import Zarinpal
from . import forms
from django.http import HttpRequest,HttpResponse

class TransactionRequestView(CreateView):
    pass

class TransactionVerifyView(DetailView):
    pass
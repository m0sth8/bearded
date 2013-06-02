# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index(request):
    return redirect('dashboard:target')
    # ctx = {}
    # return render(request, 'index.html', ctx)

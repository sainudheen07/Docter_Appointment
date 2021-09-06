from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import Appoiment, Docter, Department
from django.contrib import messages
import datetime
from django.http import HttpResponse, HttpResponseRedirect

from .models import PatientDetail
from .forms import appoimentform


# Create your views here.

def DocDetails(request, c_slug, doc_slug):
    dept = Department.objects.all()
    docter = Docter.objects.get(slug=doc_slug)

    return render(request, 'news-detail.html', dict(dept=dept, docter=docter))


def FormDetail(request):
    submitted = False
    form = appoimentform(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            # messages.success(request, "Your Appointment is Succesfully Updated ")

            return HttpResponseRedirect('/FormDetail?submitted=True')
    else:
        form = appoimentform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'test.html', dict(form=form, submitted=submitted))

from django.shortcuts import render, get_object_or_404

from .models import Docter, Department
from django.http import HttpResponse


# Create your views here.
def DetailView(request):
    c_dept = None
    c_doc = None
    # if c_slug != None:
    #     c_dept = get_object_or_404(Department, slug=c_slug)
    #     c_doc = Docter.objects.all().fliter(department=c_slug)
    # else:
    c_doc=Docter.objects.all()
    c_dept = Department.objects.all()
    return render(request, 'index.html', {'dept': c_dept, 'doc': c_doc})

    # return HttpResponse('hellow')
def DepartmentView(request,c_slug=None):
    c_doc=None
    c_dept=None

    if c_slug!=None:
        # c_dept = get_object_or_404(Department, slug=c_slug)
        c_dept = Department.objects.all().filter(slug=c_slug).first()
        c_doc = Docter.objects.all().filter(department=c_dept)
    return render(request, 'dept_detail.html', {'dept': c_dept, 'doc': c_doc})



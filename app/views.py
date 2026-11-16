from django.shortcuts import render

# Create your views here.
from app.models import *


def empdeptdata(request):
    LEDO=Emp.objects.select_related('DEPTNO').all()
    LEDO=Emp.objects.select_related('DEPTNO').filter(SAL__gt=5000)
    LEDO=Emp.objects.select_related('DEPTNO').filter(COMM__isnull=False)
    d={'LEDO':LEDO}
    return render(request,'empdeptdata.html',d)
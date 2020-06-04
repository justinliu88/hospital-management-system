# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from mydoct.models import User
def login(request):
    return render(request,'login.html')



def hello(request):
    # Check to see if there is activitycode, return to vilidation if none
    # if there is activitycode then check if this activitycode passes vilidation
    # if state == 1,return to index.html
    # cant operate if cant access index page
    activitycode = request.GET.get("activitycode")

    if not activitycode :
        return render(request, 'wait.html')

    if not User.objects.filter(AcivityCode = activitycode) :
        return render(request, 'wait.html')

    u = User.objects.get(AcivityCode = activitycode)
    if u.State == 1:
        return render(request, 'index.html')
    else:
        return render(request, 'wait.html')

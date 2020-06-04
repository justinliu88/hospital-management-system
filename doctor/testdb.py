# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
import smtplib,time
from . import settings
from email.mime.text import MIMEText

from mydoct.models import Doct,User


# database operation
def testdbAdd(request):
    # need permission to access，no access when state == 0，unable to operate database
    state = request.session.get("state",0)
    if not state:
        return HttpResponse(json.dumps([]))

    test1 = Doct()
    test1.Phone = request.POST.getlist("Phone")[0]
    test1.eMail = request.POST.getlist("eMail")[0]
    test1.FName = request.POST.getlist("FName")[0]
    test1.LName = request.POST.getlist("LName")[0]
    test1.Address = request.POST.getlist("Address")[0]
    test1.OID = request.POST.getlist("OID")[0]
    test1.Description = request.POST.getlist("Description")[0]
    test1.QText = request.POST.getlist("QText")[0]
    test1.save()
    return HttpResponse(test1.UID)


import json


def testdbGet(request):
    # values = {"Phone":"1111111","eMail":"213@asd.com","FName":"aaa","LName":"bbb","Address":"sadsd","OID": 1,"Description":"aaaaa","QText":"ccccc"}

    state = request.session.get("state",0)

    if not state:
        return HttpResponse(json.dumps([]))

    offset = request.GET.get("offset")
    limit = request.GET.get("limit")
    print(offset)
    print(limit)
    DoctList = Doct.objects.order_by("UID")[int(offset):int(limit)]
    # alllist = serializers.serialize('json',DoctList)
    alllist = [
        {"UID": x.UID, "Phone": x.Phone, "eMail": x.eMail, "FName": x.FName, "LName": x.LName, "Address": x.Address,
         "OID": x.OID, "Description": x.Description, "QText": x.QText} for x in DoctList]

    return HttpResponse(json.dumps(alllist))


def testdbUpdate(request):

    state = request.session.get("state",0)

    if not state:
        return HttpResponse("error")

    id = request.POST.getlist("UID")[0]
    values = {"Phone": request.POST.getlist("Phone")[0], "eMail": request.POST.getlist("eMail")[0],
              "FName": request.POST.getlist("FName")[0], "LName": request.POST.getlist("LName")[0],
              "Address": request.POST.getlist("Address")[0], "OID": request.POST.getlist("OID")[0],
              "Description": request.POST.getlist("Description")[0], "QText": request.POST.getlist("QText")[0]}
    D = Doct.objects.filter(UID=id)
    for k in values.keys():
        if k == "Phone":
            D.update(Phone=values["Phone"])
        elif k == "eMail":
            D.update(eMail=values["eMail"])
        elif k == "FName":
            D.update(FName=values["FName"])
        elif k == "LName":
            D.update(LName=values["LName"])
        elif k == "Address":
            D.update(Address=values["Address"])
        elif k == "OID":
            D.update(OID=values["OID"])
        elif k == "Description":
            D.update(Description=values["Description"])
        elif k == "QText":
            D.update(QText=values["QText"])

    return HttpResponse("update success ! ")


def testdbDel(request):

    state = request.session.get("state",0)
    if not state:
        return HttpResponse("error")

    if not request.POST.getlist("ids") is []:
        ids = request.POST.getlist("ids")[0].split(",")
        for id in ids:
            # print(id)
            Doct.objects.get(UID=id).delete()
        return HttpResponse("delete success")




def send_mail(to_list, sub, content):
    me = "<" + settings.EMAIL_HOST_USER + "@" + settings.EMAIL_SUBJECT_PREFIX + ">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  # sperate reciver list with‘；’
    try:
        server = smtplib.SMTP()
        server.connect(settings.EMAIL_HOST)  # connect to server
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)  # sign in to operate
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False



def testdbLogin(request):
    # save the received Name，eMail info，save database,activitycode(activation code)
    #  randomcode(random), state（0,1 activation state）
    # savedatabase Name eMial activitycode randomcode state = 1

    activitycode = request.COOKIES.get("activitycode")
    Name = request.POST.get("Name")
    EMail = request.POST.get("eMail")

    if User.objects.filter(AcivityCode = activitycode):
        randomcode = User.objects.get(AcivityCode = activitycode).RandomCode
        # not yet passed
        if not User.objects.get(AcivityCode = activitycode).State:
            # send email activation to administrator
            try:
                send_mail(settings.SERVER_EMAIL,"apply for access","applicant："+Name+" \n"+"Email："+EMail+" \n"+
                      "link：\n"+ "http://127.0.0.1:8000/savecode?randomcode="+randomcode+"&activitycode="+activitycode)
            except Exception as e:
                print(e)
    else:
        randomcode = str(int(time.time()))
        u = User()
        u.Name = Name
        u.EMail = EMail
        u.RandomCode = randomcode
        u.AcivityCode = activitycode
        u.save()

        # send email activation to administrator
        try:
            send_mail(settings.SERVER_EMAIL,"apply for access","applicant："+Name+" \n"+"Email："+EMail+" \n"+
                  "link：\n"+ "http://127.0.0.1:8000/savecode?randomcode="+randomcode+"&activitycode="+activitycode)
        except Exception as e:
            print(e)

    return render(request, 'wait.html')

def testdbSaveCode(request):
    # save activiycode, check with randomcode to see if it matches

    randomcode = request.GET.get("randomcode")
    activitycode = request.GET.get("activitycode")

    u = User.objects.get(AcivityCode = activitycode)
    if u.RandomCode == randomcode:
        u.State = 1
        print("state == 1")
        u.save()
        return HttpResponse("save success")
    else:
        return HttpResponse("save fail")

def testdbCheckCode(request):
    # check activityCode to see if access is granted
    # save login status Session
    activitycode = request.POST.get("activitycode")
    if User.objects.filter(AcivityCode = activitycode):
        u = User.objects.get(AcivityCode = activitycode)
        if u.State == 1:
            request.session["state"] = 1
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")

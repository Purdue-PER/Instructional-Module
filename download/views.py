from django.shortcuts import render
from django.http import HttpResponse
from calibrate.models import clicks
import Force_HLG.models as force
import Login.models as log
from django.contrib.auth.models import User
from csv import writer

#### Calibrate ###########################################
def cal_download_view(request):
    
    obj = clicks.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="calibrate.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["user","mouseX","mouseY","time_stamp","event"])
    for row in obj:
        csv_writer.writerow([row.user, row.mouseX, row.mouseY, row.time_stamp, row.event])

    return response


## Pretest ###############################################


def preEDU_download_view(request):
    
    obj = force.pretestEdu.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="pretestEDU.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","timeStamp","user","question","choice"])
    for row in obj:
        csv_writer.writerow([row.pageState, row.timeStamp, row.user, row.question, row.choice])

    return response

def preLOG_download_view(request):
    
    obj = force.pretestLog.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="prettestLog.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","VideoNumber","videoTime","timeStamp","wandering"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.videoNumber,row.timeStamp,row.wandering])

    return response

def preMouse_download_view(request):
    
    obj = force.pretestMouseEvent.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="pretestMouse.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","timeStamp","mouseX","mouseY","clickedITMtl","clickedITMbr","keyPressed"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.timeStamp,row.mouseX,row.mouseY,row.clickedITMtl,row.clickedITMbr,row.keyPressed])

    return response


## force/instructional #############################################


def forceEDU_download_view(request):
    
    obj = force.forceEDU.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="forceEDU.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","timeStamp","question","choice"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.timeStamp,row.question,row.choice])

    return response

def forceLOG_download_view(request):
    
    obj = force.forceLog.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="forceLog.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","VideoNumber","videoTime","timeStamp","wandering"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.videoNumber,row.timeStamp,row.wandering])

    return response

def forceMouse_download_view(request):
    
    obj = force.forceMouseEvent.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="forceMouse.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","timeStamp","mouseX","mouseY","clickedITMtl","clickedITMbr","keyPressed"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.timeStamp,row.mouseX,row.mouseY,row.clickedITMtl,row.clickedITMbr,row.keyPressed])

    return response


## Post-Test #########################################################3


def postEDU_download_view(request):
    
    obj = force.posttestEdu.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="posttestEDU.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","timeStamp","user","question","choice"])
    for row in obj:
        csv_writer.writerow([row.pageState, row.timeStamp, row.user, row.question, row.choice])

    return response

def postLOG_download_view(request):
    
    obj = force.posttestLog.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="posttestLog.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","VideoNumber","videoTime","timeStamp","wandering"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.videoNumber,row.timeStamp,row.wandering])

    return response

def postMouse_download_view(request):
    
    obj = force.posttestMouseEvent.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="posttestMouse.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","timeStamp","mouseX","mouseY","clickedITMtl","clickedITMbr","keyPressed"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.timeStamp,row.mouseX,row.mouseY,row.clickedITMtl,row.clickedITMbr,row.keyPressed])

    return response

## User model ########################################33

from django.contrib.auth.models import User

def user_download_view(request):
    
    obj = User.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="users.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["username","email_address","first_name","last_name","staff"])
    for row in obj:
        csv_writer.writerow([row.username,row.email,row.first_name,row.last_name,row.is_staff])

    return response

def download_api(request):
    return render(request,"download/data_download.html")
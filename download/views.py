from django.shortcuts import render
from django.http import HttpResponse
from calibrate.models import clicks
import Force_HLG.models as force
import Login.models as log
from llm.models import llm_data
from django.contrib.auth.models import User
from csv import writer
from django.contrib.auth.decorators import login_required, user_passes_test

#### Calibrate ###########################################
@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
def forceEDU_download_view(request):
    
    obj = force.forceEdu.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="forceEDU.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","timeStamp","question","choice"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.timeStamp,row.question,row.choice])

    return response

@login_required
@user_passes_test(lambda u: u.is_superuser)
def forceLOG_download_view(request):
    
    obj = force.forceLog.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="forceLog.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["pageState","event","user","VideoNumber","videoTime","timeStamp","Wandering"])
    for row in obj:
        csv_writer.writerow([row.pageState,row.event,row.user,row.videoNumber,row.videoTime,row.timeStamp,row.Wandering])

    return response

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

@login_required
@user_passes_test(lambda u: u.is_superuser)
def download_api(request):
    return render(request,"download/data_download.html")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def llm_download_view(request):
    
    obj = llm_data.objects.all()
    response = HttpResponse(content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="llm_responses.csv"'}
    )

    csv_writer = writer(response)
    csv_writer.writerow(["user","message","response"])
    for row in obj:
        csv_writer.writerow([row.user,row.message,row.response])

    return response
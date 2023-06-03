from django.shortcuts import render
from .form import cal_form
from django.http import HttpResponse
from Modules.settings import admins 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def calibrate(request):
    if request.method == "POST":
        form = cal_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("there was a problem")
    else:
        is_admin = None
        if str(request.user) in admins:
            is_admin = True
        form = cal_form(initial={"user":request.user})
        context = {"form":form,"is_admin":is_admin}
        return render(request,"calibrate/cal_admin.html",context)

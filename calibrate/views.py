from django.shortcuts import render
from .form import cal_form
from django.http import HttpResponse

# Create your views here.
def calibrate(request):
    if request.method == "POST":
        form = cal_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("there was a problem")
    else:
        form = cal_form(initial={"user":request.user})
        return render(request,"calibrate/cal.html",{"form":form})

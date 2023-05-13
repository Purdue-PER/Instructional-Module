from django.shortcuts import render

# Create your views here.
def calibrate(request):
    return render(request,"calibrate/cal.html")

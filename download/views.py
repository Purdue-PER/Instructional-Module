from django.shortcuts import render
from django.http import HttpResponse
import calibrate.models as cal
import Force_HLG.models as force
import Login.models as log
from csv import writer

# Create your views here.
def download_view(request):
    
    obj = cal.objects.all()
    response = HttpResponse(
    content_type="text/csv",
    headers={"Content-Disposition": 'attachment; filename="calibrate.csv"'},
    )

    print(obj)

    writer = csv.writer(response)
    writer.writerow(["user","mouseX","mouseY","time_stamp","event"])
    writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])

    return response

    return response
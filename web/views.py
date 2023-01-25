import json

from django.shortcuts import render
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from .tasks import generate_csv


def index(request):
    return render(request,'web/index.html')


@csrf_exempt
def generate(request):
    file_name = request.POST["file_name"]
    number = request.POST["number"]
    generate_csv.apply_async(args=[number,file_name])
    response_data={
        "title":'success'
    }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import long_running_tasks
# Create your views here.

def index(request):
    long_running_tasks.delay(2)
    return JsonResponse(
        data = {"message":"This is long running task"}
    )
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import time
# Create your views here.
def long_running_task(request):
    start_time= datetime.now()
    print("#### start task at {}".format(start_time))
    
    time.sleep(2) #pause task execution for 2 seconds
    
    end_time= datetime.now()
    print("#### end task at {}".format(end_time))
    return JsonResponse(
        data = {"message":"This is long running task"}
    )
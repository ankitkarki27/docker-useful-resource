from datetime import datetime
import time
from celery import shared_task

@shared_task
def long_running_tasks(delay=2):
    start_time= datetime.now()
    print("#### start task at {}".format(start_time))
    
    time.sleep(2) #pause task execution for 2 seconds
    
    end_time= datetime.now()
    print("#### end task at {}".format(end_time))
    
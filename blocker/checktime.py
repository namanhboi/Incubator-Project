import datetime 


def checktime(time_start, time_end): #check xem thời gian hiện tại có trong thời gian gian không
    time_start_hour = int(time_start[:2])
    time_start_min = int(time_start[-2:])
    datetime_time_start = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, time_start_hour, time_start_min)
    
    time_end_hour = int(time_end[:2])
    time_end_min = int(time_end[-2:])
    datetime_time_end = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, time_end_hour, time_end_min)
 
    if datetime_time_start < datetime.datetime.now() < datetime_time_end:
        return True
    
    return False
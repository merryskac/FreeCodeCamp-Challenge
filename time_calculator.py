def add_time(start, duration, the_day=''):
    start=start.split()
    day_or_night=start[1].lower()
    hour_and_minute=start[0].split(':')
    hour=hour_and_minute[0]
    minute=hour_and_minute[1]
    
    duration=duration.split(':')
    hour_duration=duration[0]
    minute_duration=duration[1]

    name_ofdays=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    result_hour=int(hour)+int(hour_duration)
    result_minute=int(minute)+int(minute_duration)
    count_day=result_hour/24
    day=int(count_day)
    result_hour=result_hour%24
    

    if(day_or_night=='am'):
        
        if(int(result_hour)+1>=12):
            day_or_night='PM'
            if(result_hour+1==12):
                result_hour=(result_hour+1)
                result_minute=int(result_minute)%60
                
            else:
                result_hour=(result_hour+1)%12
                result_minute=int(result_minute)%60
                
        else:
            if(result_minute>59):
                result_hour=(result_hour+1)
                result_minute=int(result_minute)%60
            else:
                result_hour=(result_hour)
                result_minute=int(result_minute)%60
            
    elif(day_or_night=='pm'):
        if(int(result_hour)+1>=12):
            day_or_night='AM'
            day=day+1
            if(result_minute>59):
                
                result_hour=(result_hour+1)
                result_minute=int(result_minute)%60
                
            else:
                
                result_hour=(result_hour)%12
                result_minute=int(result_minute)%60
                
        else:
            
            if(result_minute>59):
                result_hour=(result_hour+1)
                result_minute=int(result_minute)%60
               
            else:
                result_hour=(result_hour)
                result_minute=int(result_minute)%60
                
    else:
        print('wrong input!')

    if(the_day==''):
        
        if (day==1):
            new_time=f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()} (next day)'
        elif (day>1):
            new_time=(f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()} ({day} days later)')
        else:
            new_time=(f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()}')
    
    elif(the_day.lower() in name_ofdays):

        the_day=the_day.lower()
        num_day=name_ofdays.index(the_day)
        if (day==1):
            new_time=f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()}, {name_ofdays[(num_day+1)%7].capitalize()} (next day)'
        elif (day>1):
            new_time=f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()}, {name_ofdays[(num_day+day)%7].capitalize()} ({day} days later)'
        else:
            new_time=(f'{result_hour}:{str(result_minute).zfill(2)} {day_or_night.upper()}, {the_day.capitalize()}')
    return new_time

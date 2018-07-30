start_date="2018-07-10"
import datetime
date_1=datetime.datetime.strptime(start_date,"%Y-%m-%d")
print(date_1)
import datetime
from dateutil.relativedelta import relativedelta

def dateadd(date, part ,value):

    if part=='year':
        result = date + (value * relativedelta(years = 1))
    elif part == 'month':
        result = date + (value * relativedelta(months = 1))
    elif part == 'day':
        result = date + (value * relativedelta(days = 1))
    elif part == 'hour':
        result = date + (value * relativedelta(hours = 1))
    elif part == 'minute':
        result = date + (value * relativedelta(minutes = 1))
    elif part == 'second':
        result = date + (value * relativedelta(seconds = 1))
    return result
    
    date_2=dateadd(date_1.date(),'month',-6)
    
    
    dateadd(dateadd(date_4,'month',1),'day',-1)
    
    start_dt=dateadd(date_1,'month',-6)
    start_dt=datetime.date(start_dt.year,start_dt.month,1)
    end_dt=dateadd(dateadd(start_dt,'month',1),'day',-1)
    start_dt=str(start_dt)

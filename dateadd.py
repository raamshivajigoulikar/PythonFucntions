import os
import datetime
from dateutil.relativedelta import relativedelta
import math

startdt=os.environ(['startdt'])
enddt=os.environ(['enddt'])
#startdt='2018-07-10'
#enddt='2018-08-15'
def dateadd(date, part ,value):

    if part=='year':
        result = date + (value * relativedelta(years = 1))
    elif part == 'month':
        result = date + (value * relativedelta(months = 1))
    elif part == 'day':
        result = date + (value * relativedelta(days = 1))
    return result
#Creating Date Variables for Query
startdt=datetime.datetime.strptime(startdt,"%Y-%m-%d")
enddt=datetime.datetime.strptime(enddt,"%Y-%m-%d")
start_dt=dateadd(startdt,'month',-6)
end_dt=dateadd(dateadd(enddt,'month',-6),'month',1)
end_dt=str(dateadd(datetime.date(end_dt.year,end_dt.month,1),'day',-1))
start_dt=str(datetime.date(start_dt.year,start_dt.month,1))
#Creating Quarter Variables
start_qrt=dateadd(dateadd(startdt,'month',1),'month',-6)
start_qrt=str(start_qrt.year) + "Q" + str(math.ceil((start_qrt.month/3)))
pull_qrt=dateadd(dateadd(startdt,'month',1),'month',0)
pull_qrt=str(pull_qrt.year) + "Q" + str(math.ceil((pull_qrt.month/3)))


print(start_dt)
print(end_dt)
print(start_qrt)
print(pull_qrt)

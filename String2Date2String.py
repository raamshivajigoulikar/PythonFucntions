df['app_date']=pd.to_datetime(df['app_date'],format('%d%b%Y')).dt.strftime("%d%b%Y")


Convert YYYYMMDD to YYYY-MM-DD
From raju

Python
>>> from datetime import datetime
>>> dt = 20140716
>>> datetime.strptime(str(dt), '%Y%m%d').strftime('%Y-%m-%d')
'2014-07-16'
To do the same thing for a column in a dataframe

>>> import pandas as pd
>>> from datetime import datetime
>>> name = ['foo', 'bar']; date = ['20160824', '20160825']; name_date = pd.DataFrame({'name': name, 'date': date}); name_date
       date name
0  20160824  foo
1  20160825  bar

>>> name_date['date'] = pd.to_datetime(name_date['date'], format='%Y%m%d').dt.strftime("%Y-%m-%d"); name_date
         date name
0  2016-08-24  foo
1  2016-08-25  bar
Tested with

>python --version
Python 3.4.4 :: Continuum Analytics, Inc.
Ref:-

http://importpython.blogspot.com/2014/07/how-to-convert-date-formats-from.html
http://strftime.org/ - Tells what different format specifiers do

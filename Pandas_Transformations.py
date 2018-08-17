import pandas as pd
import numpy as np

data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df


capitalizer = lambda x: x.upper()

df['name'].map(capitalizer)

#applymap() applies a function to every single element in the entire dataframe.
# Drop the string variable so that applymap() can run
df = df.drop('name', axis=1)

# Return the square root of every cell in the dataframe
df.applymap(np.sqrt)

# create a function called times100
def times100(x):
    # that, if x is a string,
    if type(x) is str:
        # just returns it untouched
        return x
    # but, if not, return it multiplied by 100
    elif x:
        return 100 * x
    # and leave everything else
    else:
        return
df.applymap(times100)

#If Else if and multiple column conditions.
import pandas as pd
import numpy as np
raw_data = {'student':['A','B','C','D','E'],
        'score': [100, 96, 80, 105,156], 
    'height': [7, 4,9,5,3],
    'trigger1' : [84,95,15,78,16],
    'trigger2' : [99,110,30,93,31],
    'trigger3' : [114,125,45,108,46]}

df2 = pd.DataFrame(raw_data, columns = ['student','score', 'height','trigger1','trigger2','trigger3'])

print(df2)


I have a dataframe like below.

import pandas as pd
import numpy as np
raw_data = {'student':['A','B','C','D','E'],
        'score': [100, 96, 80, 105,156], 
    'height': [7, 4,9,5,3],
    'trigger1' : [84,95,15,78,16],
    'trigger2' : [99,110,30,93,31],
    'trigger3' : [114,125,45,108,46]}

df2 = pd.DataFrame(raw_data, columns = ['student','score', 'height','trigger1','trigger2','trigger3'])

print(df2)
I need to derive Flag column based on multiple conditions.

i need to compare score and height columns with trigger 1 -3 columns.

Flag Column:

if Score greater than equal trigger 1 and height less than 8 then Red --

if Score greater than equal trigger 2 and height less than 8 then Yellow --

if Score greater than equal trigger 3 and height less than 8 then Orange --

if height greater than 8 then leave it as blank

How to write if else conditions in pandas dataframe and derive columns?

Expected Output

  student  score  height  trigger1  trigger2  trigger3    Flag
0       A    100       7        84        99       114  Yellow
1       B     96       4        95       110       125     Red
2       C     80       9        15        30        45     NaN
3       D    105       5        78        93       108  Yellow
4       E    156       3        16        31        46  Orange




def flag_df(df):

    if (df['trigger1'] <= df['score'] < df['trigger2']) and (df['height'] < 8):
        return 'Red'
    elif (df['trigger2'] <= df['score'] < df['trigger3']) and (df['height'] < 8):
        return 'Yellow'
    elif (df['trigger3'] <= df['score']) and (df['height'] < 8):
        return 'Orange'
    elif (df['height'] > 8):
        return np.nan

df2['Flag'] = df2.apply(flag_df, axis = 1)

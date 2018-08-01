import pandas as pd
import os
def val_dup_check(lib, indata, dest, outp, qtr, module):
    indata=pd.read_csv(lib+indata)
    outdata=indata[indata.duplicated(['app_id'],keep=False)]
    
    num_obs=outdata.shape[0]

    if num_obs > 0 and num_obs < 90000:
        outdata.to_csv(dest+outp)
    
    if outdata[outdata['tranche']==qtr].shape[0] > 0:
        currtfound=True
        print("Error: Duplicates in Current Quarter")
    else:
        currtfound=False
    print("Current Quarter Duplicates is: ",currtfound)

    if num_obs > 90000:
        #Write an email step to masi_jobstatus@capitalone.com
        subject="Dupe Check - &module : Too many records for excel output check the file at "+dest+" With name "+outp
    
    if num_obs > 0:    
        if currtfound:
            t="Dupe Check - "+ module+" Data Pull Check : Duplicate records found (dup in current quarter)"
        else:
            t="Dupe Check - " + module+" Data Pull Check : Duplicate records found (dup in previous quarters)" 
        #Email with subject as t variable to masi_jobstatus@capitalone.com
        #Attach the output file with name as outp and at dest location
    else:
        #Email to same email ID as above with subject mentioning there are no duplicate records
        pass




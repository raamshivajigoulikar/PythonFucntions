import os
import datetime
from dateutil.relativedelta import relativedelta
import math
import pandas as pd

#Main Function from above append function will be called
in="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/data/G3_VLM/"

cmf_efx="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_vlm_efx/input"
cmf_efx2="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_vlm_efx_2/input"
cmf_efx3="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_vlm_efx_3/input"

cmf_xpn="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_xpn_efx/input"
cmf_xpn2="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_xpn_efx_2/input"
cmf_xpn3="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_xpn_efx_3/input"

cmf_tu="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_tu_efx/input"
cmf_tu2="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_tu_efx_2/input"
cmf_tu3="/prod/user/sam/coaf/npi/masi/model_monitoring/G3/cmf/g3_tu_efx_3/input"


#Variable List for keep the columns
efx_var="CAP1KEY pre_bur_ind AF001 \
AF002 AF009 AF011 AF040 AF041 AF048 AF049 AF051 AF070 AF071 AF073 \
AF076 AF080 C2001 C2012 C2019 C2021 C2028 C2036 C2040 C2042 C2045 \
C2056 C2065 C2067 CI001 CI002 CI003 CI004 CI006 CI010 CI012 CI014 CI019 \
CI024 CI029 CI030 CI032 CI037 CI038 CI039 CI041 CI042 CI043 CI044 \
CI045 CI048 CI055 CI056 CI057 CI058 CI059 CI060 CI061 CI065 CI083 CI085 \
CI086 CI087 CI089 CI091 CI092 CI093 CI097 CI098 CI101 CI105 CI106 \
CI107 CI108 CI111 CI114 CI121 CI124 CI126 CI136 CI137 CI146 CI149 \
CI152 CI153 CI155 CI156 CI159 CI160 CI163 CI164 CI165 CI166 CI168 \
CI189 CI192 CI197 CI199 CI200 ED001 ED039 ED040 ED041 ED074 ED076 \
ED077 ED078 ED080 ED081 ED082 HE001 HE002 HE027 HE028 HE033 HE034 \
HE040 HE041 HE047 IL001 IL002 IL005 IL007 IL008 IL013 IL014 IL021 \
IL022 IL023 IL024 IL040 IL041 IL043 IL047 IL048 IL051 IL057 IL065 \
IL066 IL068 MG001 MG002 MG027 MG028 MG033 MG034 MG040 MG041 MG047 \
RE001 RE002 RE027 RE028 RE033 RE034 RE040 RE041 RE047 RL001 RL002 \
RL011 RL040 RL041 RL043 RL047 RL048 RL049 RL057 RL059 RL060 RL061 \
RL065 RL066 RL068 app_id appdate efx_fico"
efx_var=efx_var.split()

xpn_var=" CAP1KEY pre_bur_ind AF001 \
AF002 AF003 AF004 AF005 AF011 AF016 AF021 AF022 AF027 AF028 AF033 AF034 \
AF040 AF041 AF048 AF049 AF059 AF061 AF065 AF066 AF068 AF070 AF071 AF073 \
AF078 C2016 C2035 C2036 C2043 C2054 C2055 C2056 C2059 C2064 C2065 CI001 \
CI002 CI003 CI004 CI010 CI012 CI018 CI022 CI029 CI031 CI032 CI037 CI038 CI039 \
CI041 CI042 CI043 CI044 CI045 CI048 CI049 CI059 CI060 CI061 CI063 CI064 \
CI065 CI083 CI085 CI086 CI087 CI089 CI091 CI092 CI093 CI098 CI101 CI105 CI107 \
CI108 CI114 CI121 CI123 CI124 CI126 CI136 CI137 CI145 CI146 CI148 CI149 \
CI150 CI151 CI152 CI153 CI155 CI156 CI159 CI160 CI163 CI164 CI165 CI166 \
CI167 CI168 CI170 CI178 CI181 CI182 CI189 CI192 CI193 CI197 CI202 ED001 \
ED039 ED040 ED041 ED061 ED076 ED077 ED078 ED080 ED081 ED082 HE001 HE002 \
HE032 HE038 HE040 HE041 HE047 HE056 HE065 HE066 HE067 IL001 IL002 IL005 \
IL009 IL011 IL040 IL041 IL043 IL047 IL048 IL058 IL059 MG001 MG002 MG032 \
MG038 MG040 MG041 MG047 MG056 MG065 MG066 MG067 RE001 RE002 RE032 RE038 \
RE040 RE041 RE047 RE056 RE065 RE066 RE067 RL001 RL002 RL009 RL013 RL014 \
RL027 RL028 RL029 RL030 RL033 RL034 RL035 RL036 RL040 RL041 RL043 RL046 \
RL047 RL048 RL049 RL056 RL059 RL061 RL065 RL066 RL068 \
app_id appdate xpn_fico"
xpn_var=xpn_var.split()

tu_var="CAP1KEY pre_bur_ind AF001 \
AF002 AF009 AF011 AF021 AF022 AF027 AF028 AF033 AF034 AF040 AF041 AF043 AF048 \
AF049 AF055 AF075 AF077 AF078 C2017 C2018 C2019 C2025 C2036 C2037 C2038 C2040 \
C2041 C2043 C2057 C2063 C2069 CI002 CI003 CI004 CI006 CI010 CI012 CI013 CI014 CI018 \
CI019 CI024 CI029 CI030 CI033 CI037 CI038 CI039 CI042 CI043 CI044 CI045 CI048 \
CI055 CI056 CI057 CI059 CI060 CI061 CI065 CI074 CI076 CI083 CI085 CI086 CI087 CI090 \
CI092 CI093 CI101 CI105 CI106 CI107 CI111 CI114 CI117 CI124 CI126 CI129 CI136 \
CI137 CI139 CI140 CI143 CI145 CI146 CI147 CI148 CI149 CI150 CI151 CI152 CI153 \
CI155 CI156 CI159 CI163 CI164 CI165 CI166 CI167 CI168 CI169 CI171 CI172 CI175 \
CI177 CI182 CI189 CI192 CI194 CI196 CI204 ED001 ED039 ED040 ED041 ED074 ED076 \
ED077 ED078 ED080 ED081 ED082 HE001 HE002 HE016 HE040 HE041 HE047 IL001 IL002 \
IL005 IL007 IL008 IL009 IL013 IL014 IL016 IL018 IL020 IL021 IL022 IL023 IL024 \
IL039 IL040 IL041 IL043 IL047 IL048 IL049 IL065 IL066 IL068 MG001 MG002 MG016 \
MG040 MG041 MG047 RE001 RE002 RE016 RE040 RE041 RE047 RL001 RL002 RL009 RL015 \
RL016 RL040 RL041 RL043 RL047 RL048 RL049 RL065 RL066 RL068 app_id appdate \
tu_fico"
tu_var=tu_var.split()

efx_var1= "CAP1KEY pre_bur_ind prsweight scorecard Mtranche ci2cpdcure9mos AF001 \
AF002 AF009 AF011 AF040 AF041 AF048 AF049 AF051 AF070 AF071 AF073 \
AF076 AF080 C2001 C2012 C2019 C2021 C2028 C2036 C2040 C2042 C2045 \
C2056 C2065 C2067 CI001 CI002 CI003 CI004 CI006 CI010 CI012 CI014 CI019 \
CI024 CI029 CI030 CI032 CI037 CI038 CI039 CI041 CI042 CI043 CI044 \
CI045 CI048 CI055 CI056 CI057 CI058 CI059 CI060 CI061 CI065 CI083 \
CI085 CI086 CI087 CI089 app_id appdate efx_fico"
efx_var1=efx_var1.split()

xpn_var1= "CAP1KEY pre_bur_ind prsweight scorecard Mtranche ci2cpdcure9mos AF001 \
AF002 AF003 AF004 AF005 AF011 AF016 AF021 AF022 AF027 AF028 AF033 AF034 \
AF040 AF041 AF048 AF049 AF059 AF061 AF065 AF066 AF068 AF070 AF071 AF073 \
AF078 C2016 C2035 C2036 C2043 C2054 C2055 C2056 C2059 C2064 C2065 CI001 \
CI002 CI003 CI004 CI010 CI012 CI018 CI022 CI029 CI031 CI032 CI037 CI038 CI039 \
CI041 CI042 CI043 CI044 CI045 CI048 CI049 CI059 CI060 CI061 \
app_id appdate xpn_fico"
xpn_var1=xpn_var1.split()

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
#start_dt=dateadd(startdt,'month',-6)
#end_dt=dateadd(dateadd(enddt,'month',-6),'month',1)
#end_dt=str(dateadd(datetime.date(end_dt.year,end_dt.month,1),'day',-1))
#start_dt=str(datetime.date(start_dt.year,start_dt.month,1))

diff= relativedelta.relativedelta(enddt,startdt)
months=diff.months

#First Append Function
def append(base,indata,keep,SC):
    indata=pd.read_csv(indata)
    base=pd.read_csv(base)
    indata=indata.sort_values(by=['app_id','borrower_id'],ascending=True)
    g3_vlm_weighted_dups=indata[indata.duplicated(['app_id'])]
    g3_vlm_weighted_dups['prsweight']=0.5
    g3_vlm_weighted=indata.drop_duplicates(subset=['app_id'],keep=False)
    g3_vlm_weighted['prsweighted']=1
    g3_vlm_weighted.append(g3_vlm_weighted_dups)
    g3_vlm_weighted['scorecard']=SC
    g3_vlm_weighted['Mtranche']=Mtranche_var
    g3_vlm_weighted['ci2cpdcure9mos']=   g3_vlm_weighted['ci042']
                                        -g3_vlm_weighted['ci048']
                                        -g3_vlm_weighted['ci037']
                                        -g3_vlm_weighted['ci038']
                                        -g3_vlm_weighted['ci039']
                                        -g3_vlm_weighted['ci043']
                                        -g3_vlm_weighted['ci044']
                                        -g3_vlm_weighted['ci045']
    base_del=base.drop(base[base['Mtranche']==Mtranche_var].index)
    g3_vlm_weighted=g3_vlm_weighted[keep]
    base=base_del.append(g3_vlm_weighted)
    return base

#Second Append Function

def append_new(base, indata, keep,crnt_qtr_data):
    base=pd.read_csv(base)
    indata=pd.read_csv(indata)
    crnt_qtr_data=pd.read_csv(crnt_qtr_data)
    g3_vlm_bur=indata[indata['Mtranche']==Mtranche_var]
    g3_vlm_bur=g3_vlm_bur[keep]
    base_del=base.drop(base[base['Mtranche']==Mtranche_var].index)
    base=base_del.append(g3_vlm_bur)
    crnt_qtr_data_del=crnt_qtr_data.drop(crnt_qtr_data[crnt_qtr_data['Mtranche']==Mtranche_var].index)
    crnt_qtr_data=crnt_qtr_data_del.append(g3_vlm_bur)
    crnt_qtr_data=crnt_qtr_data. \
            drop((crnt_qtr_data[crnt_qtr_data['appdate'] > start_date_var] & crnt_qtr_data[crnt_qtr_data['appdate'] < end_date_var]).index)
    return base , crnt_qtr_data

def step3_1_vlm_cmf_data_pull(i,month_dt):
    report_dt=month_dt
    i=int(i)
    startdt=dateadd(report_dt,'month',i*-1)
    yyyy=startdt.year
    mm=startdt.month
    pull_mon=str(mm)+str(yyyy[2:3])
    Mtranche=str(yyyy*100+mm)
    print(pull_mon)
    print(Mtranche)
    g3_vlm_efx_dw=append(base=in+"g3_vlm_efx_dw.csv",indata=in+"PRS_DMS_EFX_"+ pull_mon+"_ed.csv",keep=efx_var,sc="EFX")
    g3_vlm_efx_dw.to_csv(in+"g3_vlm_efx_dw.csv")
    g3_vlm_xpn_dw=append(base=in +"g3_vlm_xpn_dw.csv",indata=in+"PRS_DMS_XPN"+pull_mon+"_ed.csv",keep=xpn_var,sc="XPN")
    g3_vlm_xpn_dw.to_csv(in+"g3_vlm_xpn_dw.csv")
    g3_vlm_tu_dw=append(base=in+"g3_vlm_tu_dw.csv",indata=in+"PRS_DMS_TU"+pull_mon+"_ed.csv",keep=tu_var,sc="TU")
    g3_vlm_tu_dw.to_csv(in+"g3_vlm_tu_dw.csv")

    g3_vlm_efx_dw,g3_vlm_efx_dw_cq = append_new(base=cmf_efx+"g3_vlm_efx_dw.csv",indata=in+"g3_vlm_efx_dw.csv",keep=efx_var1, crnt_qtr_data=cmf_efx+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_efx_dw.to_csv(cmf_efx+"g3_vlm_efx_dw.csv")
    g3_vlm_efx_dw_cq.to_csv(cmf_efx+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_xpn_dw,g3_vlm_xpn_dw_cq = append_new(base=cmf_xpn+"g3_vlm_xpn_dw.csv",indata=in+"g3_vlm_xpn_dw.csv",keep=xpn_var1, crnt_qtr_data=cmf_xpn+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_xpn.to_csv(cmf_xpn+"g3_vlm_xpn_dw.csv")
    g3_vlm_xpn_dw_cq.to_csv(cmf_xpn+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_tu_dw,g3_vlm_tu_dw_cq = append_new(base=cmf_tu+"g3_vlm_tu_dw.csv",indata=in+"g3_vlm_tu_dw.csv",keep=tu_var1, crnt_qtr_data=cmf_tu+"g3_vlm_tu_dw_cq.csv")
    g3_vlm_tu_dw.to_csv(cmf_tu+"g3_vlm_xpn_dw.csv")
    g3_vlm_tu_dw_cq.to_csv(cmf_tu+"g3_vlm_xpn_dw_cq.csv")

    g3_vlm_efx_dw,g3_vlm_efx_dw_cq = append_new(base=cmf_efx2+"g3_vlm_efx_dw.csv",indata=in+"g3_vlm_efx_dw.csv",keep=efx_var2, crnt_qtr_data=cmf_efx2+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_efx_dw.to_csv(cmf_efx2+"g3_vlm_efx_dw.csv")
    g3_vlm_efx_dw_cq.to_csv(cmf_efx2+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_xpn_dw,g3_vlm_xpn_dw_cq = append_new(base=cmf_xpn2+"g3_vlm_xpn_dw.csv",indata=in+"g3_vlm_xpn_dw.csv",keep=xpn_var2, crnt_qtr_data=cmf_xpn2+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_xpn.to_csv(cmf_xpn2+"g3_vlm_xpn_dw.csv")
    g3_vlm_xpn_dw_cq.to_csv(cmf_xpn2+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_tu_dw,g3_vlm_tu_dw_cq = append_new(base=cmf_tu2+"g3_vlm_tu_dw.csv",indata=in+"g3_vlm_tu_dw.csv",keep=tu_var2, crnt_qtr_data=cmf_tu2+"g3_vlm_tu_dw_cq.csv")
    g3_vlm_tu_dw.to_csv(cmf_tu2+"g3_vlm_xpn_dw.csv")
    g3_vlm_tu_dw_cq.to_csv(cmf_tu2+"g3_vlm_xpn_dw_cq.csv")

    g3_vlm_efx_dw,g3_vlm_efx_dw_cq = append_new(base=cmf_efx3+"g3_vlm_efx_dw.csv",indata=in+"g3_vlm_efx_dw.csv",keep=efx_var3, crnt_qtr_data=cmf_efx3+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_efx_dw.to_csv(cmf_efx3+"g3_vlm_efx_dw.csv")
    g3_vlm_efx_dw_cq.to_csv(cmf_efx3+"g3_vlm_efx_dw_cq.csv")
    g3_vlm_xpn_dw,g3_vlm_xpn_dw_cq = append_new(base=cmf_xpn2+"g3_vlm_xpn_dw.csv",indata=in+"g3_vlm_xpn_dw.csv",keep=xpn_var3, crnt_qtr_data=cmf_xpn3+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_xpn.to_csv(cmf_xpn3+"g3_vlm_xpn_dw.csv")
    g3_vlm_xpn_dw_cq.to_csv(cmf_xpn3+"g3_vlm_xpn_dw_cq.csv")
    g3_vlm_tu_dw,g3_vlm_tu_dw_cq = append_new(base=cmf_tu3+"g3_vlm_tu_dw.csv",indata=in+"g3_vlm_tu_dw.csv",keep=tu_var3, crnt_qtr_data=cmf_tu3+"g3_vlm_tu_dw_cq.csv")
    g3_vlm_tu_dw.to_csv(cmf_tu3+"g3_vlm_xpn_dw.csv")
    g3_vlm_tu_dw_cq.to_csv(cmf_tu3+"g3_vlm_xpn_dw_cq.csv")

    #return g3_vlm_efx_dw,g3_vlm_efx_dw_cq,g3_vlm_xpn_dw,g3_vlm_xpn_dw_cq,g3_vlm_tu_dw,g3_vlm_tu_dw_cq

for i in range(months):
    print(i)
    step3_1_vlm_cmf_data_pull(i,enddt)

def aggr_method(base,cur_qtr_data):
    base=pd.read_csv(base)
    cur_qtr_data=pd.read_csv(cur_qtr_data)
    base[(base['appdate'] >= startdt & base['appdate'] <= enddt),'curqtr']=1
    base['curqtr'].fillna(0)
    cur_qtr_data=base[(base['appdate'] >= startdt & base['appdate'] <= enddt)]
    return base, cur_qtr_data

g3_vlm_efx_dw,g3_vlm_efx_dw_cq=aggr_method(cmf_efx+"g3_vlm_efx_dw.csv",cmf_efx+"g3_vlm_efx_dw_cq.csv")
g3_vlm_efx_dw.to_csv(cmf_efx+"g3_vlm_efx_dw.csv")
g3_vlm_efx_dw_cq.to_csv(cmf_efx+"g3_vlm_efx_dw_cq.csv")

g3_vlm_xpn_dw,g3_vlm_xpn_dw_cq=aggr_method(cmf_xpn+"g3_vlm_xpn_dw.csv",cmf_efx+"g3_vlm_xpn_dw_cq.csv")
g3_vlm_xpn_dw.to_csv(cmf_efx+"g3_vlm_xpn_dw.csv")
g3_vlm_xpn_dw_cq.to_csv(cmf_efx+"g3_vlm_xpn_dw_cq.csv")

g3_vlm_tu_dw,g3_vlm_tu_dw_cq=aggr_method(cmf_tu+"g3_vlm_tu_dw.csv",cmf_tu+"g3_vlm_tu_dw_cq.csv")
g3_vlm_tu_dw.to_csv(cmf_efx+"g3_vlm_tu_dw.csv")
g3_vlm_tu_dw_cq.to_csv(cmf_efx+"g3_vlm_tu_dw_cq.csv")
    



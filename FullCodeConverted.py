import os
import datetime
from dateutil.relativedelta import relativedelta
import math
import pandas as pd

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

validity_young_filename="validity_young_" + pull_qrt
"""
#Write a SQL Query to connect and extract data from teradata and name the result set as validity_young_pull_qrt

proc sql;
connect to teradata(mode=teradata server=oneview database=padw user=&TeraID. password=&TeraPwd.);
create table out.validity_young_&pull_qrt. as
select *,
int(
mean(
mean(PRIM_EFX_FICO_SCORE_VAL,PRIM_EXP_FICO_SCORE_VAL,PRIM_TRU_FICO_SCORE_VAL),
mean(SCNDRY_EFX_FICO_SCORE_VAL,SCNDRY_EXP_FICO_SCORE_VAL, SCNDRY_TRU_FICO_SCORE_VAL)
)
) as app_avg_fico
from connection to teradata

(select 
       root.APPN_ID as app_id,
    fcab.MTHS_ON_BOOK_DUR as mob,
    root.APPN_RECVD_DT as app_date, 
       root.fund_dt, 
    root.LOB_ID,
       root.ASGND_PROD_ID as prod_id,
       lsa.DLR_DMND_STAT_DESC as dealer_diamond_cd,
       croot.PASS_THRU_CHNL_NM as channel_nm,
       croot.BUMPING_FICO_SCORE_VAL as bumping_fico,
    fcs.MODEL_SCORE_VAL as model_id,
       fcs.PRIM_EFX_FICO_SCORE_VAL,
    fcs.PRIM_EXP_FICO_SCORE_VAL,
    fcs.PRIM_TRU_FICO_SCORE_VAL,
    fcs.SCNDRY_EFX_FICO_SCORE_VAL,
    fcs.SCNDRY_EXP_FICO_SCORE_VAL,
    fcs.SCNDRY_TRU_FICO_SCORE_VAL,
       fcs.APPN_MODEL_SCORE_VAL as g3_score,
       fcs.PRICG_MODEL_SCORE_VAL as v3_score,
       cast(fcab.DELQ_60_PLUS_DAYS_IND as int) as del_60_plus,
    cast(fcab.CHRGOF_IND as int) as chargeoff_flag,
    fcab.PDUE_DAY_CNT as days_past_due
 from PADW.PL_APPN_ROOT as root
 join PADW_CREDIT.PL_LOAN_STG_APPN as fcs
         on root.APPN_ID=fcs.APPN_ID
 left join padw.pl_loan_stg_appn as lsa
       on root.appn_id = lsa.appn_id
 left join padw_credit.PL_APPN_ROOT as croot
       on root.appn_id = croot.appn_id
 left join PADW.PL_CURR_DEFN_LOSS_FRCST_ME as fcab 
      on fcs.APPN_ID= fcab.APPN_ID
      and fcab.MTHS_ON_BOOK_DUR>=0 and fcab.MTHS_ON_BOOK_DUR<=6

 where upper(root.fundd_ind)='Y'
    and fcs.MODEL_SCORE_VAL=22
    and root.APPN_RECVD_DT >=%str(%')&start_dt.%str(%') 
       and root.APPN_RECVD_DT <=%str(%')&end_dt.%str(%')
       and root.FUND_DT<=%str(%')&end_dt.%str(%')

 );
disconnect from teradata;
quit;
"""
"""
##Write a SQL query to pull data from Teradata and name result set as val6mon_direct_pull_qrt 
proc sql;
connect to teradata(mode=teradata server=oneview database=padw user=&TeraID. password=&TeraPwd.);
create table out.val6mon_direct_&pull_qrt. as
select
,
int(
mean(
mean(PRIM_EFX_FICO_SCORE_VAL,PRIM_EXP_FICO_SCORE_VAL,PRIM_TRU_FICO_SCORE_VAL),
mean(SCNDRY_EFX_FICO_SCORE_VAL,SCNDRY_EXP_FICO_SCORE_VAL, SCNDRY_TRU_FICO_SCORE_VAL)
)
) as app_avg_fico
from connection to teradata
(select b.app_id,b.app_date,b.prod_id ,a., b.g3_app_score as g3_score,b.lob_id
from

 (select 
       
       ap.asoc_appn_id,
    fcab.MTHS_ON_BOOK_DUR as mob,
 
       root.fund_dt, 
 
       root.fundd_ind,
       
       lsa.DLR_DMND_STAT_DESC as dealer_diamond_cd,
       croot.PASS_THRU_CHNL_NM as channel_nm,
       croot.BUMPING_FICO_SCORE_VAL as bumping_fico,
    fcs.MODEL_SCORE_VAL as model_id,
       fcs.PRIM_EFX_FICO_SCORE_VAL,
    fcs.PRIM_EXP_FICO_SCORE_VAL,
    fcs.PRIM_TRU_FICO_SCORE_VAL,
    fcs.SCNDRY_EFX_FICO_SCORE_VAL,
    fcs.SCNDRY_EXP_FICO_SCORE_VAL,
    fcs.SCNDRY_TRU_FICO_SCORE_VAL,
       fcs.APPN_MODEL_SCORE_VAL as g3_score_36x,
       fcs.PRICG_MODEL_SCORE_VAL as v3_score,
       cast(fcab.DELQ_60_PLUS_DAYS_IND as int) as del_60_plus,
    cast(fcab.CHRGOF_IND as int) as chargeoff_flag,
    fcab.PDUE_DAY_CNT as days_past_due
 from PADW.PL_APPN_ROOT as root

 join padw.appn ap on root.appn_id=ap.appn_id
 join padw_credit.PL_APPN_ROOT as croot on root.appn_id = croot.appn_id
join PADW_CREDIT.PL_LOAN_STG_APPN as fcs on root.APPN_ID=fcs.APPN_ID
 join padw.pl_loan_stg_appn as lsa on root.appn_id = lsa.appn_id
 left join PADW.PL_CURR_DEFN_LOSS_FRCST_ME as fcab  on fcs.APPN_ID= fcab.APPN_ID
                                                                  and fcab.MTHS_ON_BOOK_DUR>=0 and fcab.MTHS_ON_BOOK_DUR<=6
WHERE root.fundd_ind = 'Y'
AND root.APPN_RECVD_DT >= %str(%')&start_dt.%str(%')
AND root.APPN_RECVD_DT <= %str(%')&end_dt.%str(%')
AND root.FUND_DT<=%str(%')&end_dt.%str(%')
AND asoc_appn_id IS NOT NULL
QUALIFY ROW_NUMBER() OVER (PARTITION BY asoc_appn_id, mob ORDER BY root.fund_dt) =1) a
inner join

       (select root.appn_id as app_id,
       root.APPN_RECVD_DT as app_date, 
       root.fund_dt, 
    root.LOB_ID,
       root.ASGND_PROD_ID as prod_id,
       ap.asoc_appn_id,
       fc.SCORE_VAL AS g3_app_score
       from PADW.PL_APPN_ROOT as root
       JOIN padw.appn ap ON root.appn_id=ap.appn_id 
       inner join PADW.DCSNG_APPN           ba     on root.appn_id=ba.appn_id
       inner join  PADW_CREDIT.DCSNG_APPN  cr     on  ba.dcsng_appn_id =cr.dcsng_appn_id 
       left join padw_credit.dcsng_appn_score fc  on ba.dcsng_appn_id = fc.dcsng_appn_id 
       where fc.scormdl_id=22 and fc.score_nm = 'T3' 
       and  root.APPN_RECVD_DT >= %str(%')&start_dt.%str(%')
and  root.APPN_RECVD_DT <= %str(%')&end_dt.%str(%')
and cr.scormdl_id =22 
       and root.LOB_ID in (252,254)
       and ap.asoc_appn_id is not null
       QUALIFY ROW_NUMBER() OVER (PARTITION BY root.appn_id ORDER BY fc.DCSNG_SCORE_ID DESC)=1) b on a.asoc_appn_id = b.app_id
            
 );
disconnect from teradata;
quit;
"""
"""
##Write a SQL query to pull data from Teradata and name result set as id_val6mon_direct_pull_qrt 
proc sql;
connect to teradata(mode=teradata server=oneview database=padw user=&TeraID. password=&TeraPwd.);
create table out.id_val6mon_direct_&pull_qrt. as
select *,
int(
mean(
      mean(PRIM_EFX_FICO_SCORE_VAL,PRIM_EXP_FICO_SCORE_VAL,PRIM_TRU_FICO_SCORE_VAL),
      mean(SCNDRY_EFX_FICO_SCORE_VAL,SCNDRY_EXP_FICO_SCORE_VAL, SCNDRY_TRU_FICO_SCORE_VAL)
     )
     ) as app_avg_fico
from connection to teradata
(select b.app_id,b.app_date,b.prod_id ,a.*, b.g3_app_score as g3_score,b.lob_id
from
(select

       ap.asoc_appn_id,
    fcab.MTHS_ON_BOOK_DUR as mob,
 
       root.fund_dt, 
 
       root.fundd_ind,
       
       lsa.DLR_DMND_STAT_DESC as dealer_diamond_cd,
       croot.PASS_THRU_CHNL_NM as channel_nm,
       croot.BUMPING_FICO_SCORE_VAL as bumping_fico,
    fcs.MODEL_SCORE_VAL as model_id,
       fcs.PRIM_EFX_FICO_SCORE_VAL,
    fcs.PRIM_EXP_FICO_SCORE_VAL,
    fcs.PRIM_TRU_FICO_SCORE_VAL,
    fcs.SCNDRY_EFX_FICO_SCORE_VAL,
    fcs.SCNDRY_EXP_FICO_SCORE_VAL,
    fcs.SCNDRY_TRU_FICO_SCORE_VAL,
       fcs.APPN_MODEL_SCORE_VAL as g3_score_36x,
       fcs.PRICG_MODEL_SCORE_VAL as v3_score,
       cast(fcab.DELQ_60_PLUS_DAYS_IND as int) as del_60_plus,
    cast(fcab.CHRGOF_IND as int) as chargeoff_flag,
    fcab.PDUE_DAY_CNT as days_past_due
 from PADW.PL_APPN_ROOT as root
 join padw.appn ap on root.appn_id=ap.appn_id
 join padw_credit.PL_APPN_ROOT as croot on root.appn_id = croot.appn_id
 join PADW_CREDIT.PL_LOAN_STG_APPN as fcs on root.APPN_ID=fcs.APPN_ID
 join padw.pl_loan_stg_appn as lsa on root.appn_id = lsa.appn_id
 left join PADW.PL_CURR_DEFN_LOSS_FRCST_ME as fcab  on fcs.APPN_ID= fcab.APPN_ID
                                                                  and fcab.MTHS_ON_BOOK_DUR>=0 and fcab.MTHS_ON_BOOK_DUR<=6
WHERE root.fundd_ind = 'Y'
AND root.APPN_RECVD_DT >= %str(%')&start_dt.%str(%')
AND root.APPN_RECVD_DT <= %str(%')&end_dt.%str(%')
AND root.FUND_DT<=%str(%')&end_dt.%str(%')
AND asoc_appn_id IS NOT NULL
QUALIFY ROW_NUMBER() OVER (PARTITION BY asoc_appn_id, mob ORDER BY root.fund_dt) =1) a
inner join
       (select root.appn_id as app_id,
       root.APPN_RECVD_DT as app_date, 
       root.fund_dt, 
    root.LOB_ID,
    root.ASGND_PROD_ID as prod_id,
       ap.asoc_appn_id,
/* fc.SCORE_VAL AS g3_app_score*/
CAST(1500 - 200/LN(2)fc.SCORE_LOGIT_VAL + 0.5 AS INTEGER) AS g3_app_score
from PADW.PL_APPN_ROOT as root
join padw.appn ap on root.appn_id=ap.appn_id
inner join PADW.DCSNG_APPN_IDEAL ba on root.appn_id=ba.appn_id
left join padw_credit.dcsng_appn_score fc on root.appn_id = fc.dcsng_appn_id
LEFT JOIN padw_credit.pl_undwrtg_stg_appn pl ON root.appn_id=pl.appn_id
where fc.scormdl_id=22 and fc.score_nm = 'T3'
and root.APPN_RECVD_DT >= %str(%')&start_dt.%str(%')
and root.APPN_RECVD_DT <= %str(%')&end_dt.%str(%')
and PL.MODEL_SCORE_VAL =22
and root.LOB_ID in (252,254)
and ap.asoc_appn_id IS NOT NULL
QUALIFY ROW_NUMBER() OVER (PARTITION BY root.appn_id ORDER BY fc.DCSNG_SCORE_ID DESC)=1) b on a.asoc_appn_id = b.app_id

 );
disconnect from teradata;
quit;
"""
val6mon_direct_pull_qrt.append(id_val6mon_direct_pull_qrt)
validity_young_pull_qrt=validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'] != 361) & (validity_young_pull_qrt['lob_id']=363)]
var_sel_list=
[
'app_id',
'mob',
'app_date',
'FUND_DT',
'LOB_ID',
'prod_id',
'dealer_diamond_cd',
'channel_nm',
'bumping_fico',
'model_id',
'PRIM_EFX_FICO_SCORE_VAL',
'PRIM_EXP_FICO_SCORE_VAL',
'PRIM_TRU_FICO_SCORE_VAL',
'SCNDRY_EFX_FICO_SCORE_VAL',
'SCNDRY_EXP_FICO_SCORE_VAL',
'SCNDRY_TRU_FICO_SCORE_VAL',
'g3_score',
'v3_score',
'del_60_plus',
'chargeoff_flag',
'days_past_due',
'app_avg_fico'
]

val_direct=val6mon_direct_pull_qrt[var_sel_list] #Define a list named var_sel_list with all required variables as above statemnt
validity_young_pull_qrt.append(val_direct)

validity_young_pull_qrt.loc[(ecom['days_past_due'] >= 60 or ecom['chargeoff_flag'] =1),'DQ60']=1
validity_young_pull_qrt['DQ60'].fillna(value=0)

loans_max_mob=validity_young_pull_qrt.groupby(['app_id','app_date','fund_dt']).max()['mob']
loans_max_mob['mob_max']=loans['mob']
loans_max_mob.drop(columns='mob')

validity_young_pull_qrt=validity_young_pull_qrt.sort_values(by=['app_id' ascending=False])
validity_young_pull_qrt=validity_young_pull_qrt.sort_values(by=['DQ60','mob' ascending=True])

validity_young_&pull_qrt=validity_young_&pull_qrt.drop_duplicates('app_id')


validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'].isin([201,202,204])&
~(validity_young_pull_qrt['prod_id'].isin([7155,7156,7157,7165,7166,7175,7185,7186,7195,6140,6141,6142,6143,6144]),'lob']='sp'
validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'].isin([350])|
(validity_young_pull_qrt['prod_id'].isin([7155,7156,7157,7165,7166,7175,7185,7186,7195,6140,6141,6142,6143,6144]),'lob']='np'
validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'].isin([301,302,304])|
,'lob']='pr'
validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'].isin([203,303])|
,'lob']='CarMax'
validity_young_pull_qrt[(validity_young_pull_qrt['lob_id'].isin([200])|
,'lob']='pa'


validity_young_pull_qrt[(validity_young['prod_id'] >= 6140)&(validity_young['prod_id'] < 6148)
(validity_young['lob'].isin(['sp','np','pr'])),'lob1']='N2C'
validity_young_pull_qrt['lob1'].fillna('')
validity_young_pull_qrt['weight']=1
validity_young_pull_qrt['scorecard']='G3'

# Segmentation for Business Tier Cuts
"""
Write SQL query to extract data from terdata and name result set as segs_all
proc sql;
connect to teradata(mode=teradata server=oneview user=&TeraID. password=&TeraPwd.);
create table segs_all as select * from connection to teradata
( select APPN_ID as app_id
, BUS_SEG_NM as seg_1
, ASOCD_LOB_NM as seg_2
, ASOCD_LOB_SUB_SEG_NM as seg_3
from padw.pl_appn_root
where APPN_RECVD_DT >=%str(%')&start_dt.%str(%') and APPN_RECVD_DT <=%str(%')&end_dt.%str(%')
and FUND_DT<=%str(%')&end_dt.%str(%')
group by 1,2,3,4
order by 1,2,3,4
);
disconnect from teradata;
quit;
"""
validity_young_pull_qrt =validity_young_pull_qrt.sort_values(by=['app_id','tranche' ascending=True])

def cr_lob_desc(df):
    if ((df['lob'].isin([252,253,254,255,361,362,363])) | (df['seg_1'].isin(['DIRECT','direct']))):
        return 'Direct';
    elif ((df['seg_1'].isin(['DEALER_S','dealer_s']))):
        if (df['seg_3'].isin(['PA','pa'])):
            return 'PA';
        elif (df['seg_3'].isin(['CARMAX','carmax'])):
            return 'Carmax';
        else:
            return 'Dealer_S';
    elif ((df['seg_1'].isin(['DEALER_P','dealer_p'])) & (df['seg_2'].isin(['IP_NP','ip_np'])) ):
        return 'Dealer_NP';
    else:
        return 'Dealer_P';

input_data['lob_desc'].apply(cr_lob_desc,axis=1)

def cr_tier(df):
    if (df['lob']=='pr'):
        if (df['g3_score'] >= 3013):
            return 0;
        elif (df['g3_score'] >= 2776):
            return 1;
        elif (df['g3_score'] >= 2565):
            return 2;
        elif (df['g3_score'] >= 2470):
            return 3;
        elif (df['g3_score'] >= 2389):
            return 4;
        elif (df['g3_score'] >= 2347):
            return 5;
    #Creating np_tier    
    if (df['lob']=='np'):
        if (df['g3_score'] >= 2776):
            return 1;
        elif (df['g3_score'] >= 2565):
            return 2;
        elif (df['g3_score'] >= 2470):
            return 3;
        elif (df['g3_score'] >= 2389):
            return 4;
        elif (df['g3_score'] >= 2347):
            return 5;
        elif (df['g3_score'] >= 2207):
            return 6;
        elif (df['g3_score'] >= 2117):
            return 7;
        elif (df['g3_score'] >= 2042):
            return 8;
        elif((df['app_date'] <= '2016-02-09') & (df['g3_score'] >= 1911)):
            return 9;
        elif((df['app_date'] >= '2016-02-10') & (df['app_date'] >= '2017-08-15') & (df['g3_score'] >= 1822)):
            return 9;
        elif((df['app_date'] >= '2017-08-16') & (df['g3_score'] >= 1831)):
            return 9;
input_data['pr_tier'].apply(cr_tier,axis=1)
input_data['np_tier'].apply(cr_tier,axis=1)

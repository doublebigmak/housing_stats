#script to pull eviews data from pareto -> pandas-> csv files for storage/usage

import pyeviews as evp
import numpy as np
import pandas as pd
import os

#start eviews
eviewsapp =evp.GetEViewsApp(instance='either',showwindow=False)

pareto_db = 'Z:\\DATABASE\\pareto.edb'

geo = 'ACA'


q_series = ["NLIUNA_Q", 
"NLIUNR_Q",
"PRICNA_Q",
"PRICNR_Q",
"SALUNA_Q",
"SALUNR_Q",
"SMMURA_Q",
"SSMURA_Q",
"STMURA_Q",
"SNLRVA_Q",
"SMMURA_Q",
"SSMURA_Q",
"STMURA_Q",
]

m_series =[
"nsmurr",
"ntmurr",
"nrmurr",
"npmurr",
"stmucr",
"stmuer",
"stmuhr",
"stmuor",
"stmupr",
"smuucr",
"smuuer",
"smuuhr",
"smuuor",
"smuupr",
"samucr",
"samuer",
"samuhr",
"samuor",
"samupr",
"semucr",
"semuer",
"semuhr",
"semuor",
"semupr",
"ssmucr",
"ssmuer",
"ssmuhr",
"ssmuor",
"ssmupr",
"srmucr",
"srmuer",
"srmuhr",
"srmuor",
"srmupr"
]

a_series=[
"ua31ur",
"ua32ur",
"ua33ur",
"ua3bur",
"ua3tur",
"va31rr",
"va32rr",
'va33rr',
'va3brr',
'va3trr',
'ra3tcr',
'rat31cr',
'rat32cr',
'rat33cr',
'rat3bcr',
'pa31rr',
'pa32rr',
'pa33rr',
'pa3brr',
'pa3trr'
]

geo_q_series = [geo+series.upper() for series in q_series]
geo_m_series = [geo+series.upper() for series in m_series]
geo_a_series = [geo+series.upper() for series in a_series]


name_scheme = {"ACANLIUNA_Q":"new_list_sa",
 "ACANLIUNR_Q":"new_list_act",
 "ACAPRICNA_Q":"avg_price_sa",
 "ACAPRICNR_Q":"avg_price_act",
 "ACASALUNA_Q":"sales_sa",
 "ACASALUNR_Q":"sales_act",
 "ACASMMURA_Q":"multi_starts",
 "ACASSMURA_Q":"single_starts",
 "ACASTMURA_Q":"total_starts",
 "ACASNLRVA_Q":"sales_new_list",
 "ACASMMURA_Q":"multi_starts_saar",
 "ACASSMURA_Q":"single_starts_saar",
 "ACASTMURA_Q":"total_starts_saar",
 "ACASNLRVA_Q":"snl_sa",
 "acansmurr":"sfd_unabsorb",
 "acantmurr":"total_unabsorb",
 "acanrmurr":"row_unabsorb",
 "acanpmurr":"row_apart_unabsorb",
 'acastmucr':'starts_condo',
 'acastmuer':'starts_rental',
 'acastmuhr':'starts_other',
 'acastmuor':'starts_homeowner',
 'acastmupr':'starts_coop',
 'acasmuucr':"multi_condo",
 'acasmuuer':"multi_rental",
 'acasmuuhr':"multi_other",
 'acasmuuor':"multi_homeowner",
 'acasmuupr':"multi_coop",
 'acasamucr':"apart_condo",
 'acasamuer':"apart_rental",
 'acasamuor':'apart_other',
 'acasamuhr':'apart_homeowner',
 'acasamupr':"apart_coop",
 'acasemucr':'semi_condo',
 'acasemuer':'semi_rental',
 'acasemuhr':'semi_other',
 'acasemuor':'semi_homeowner',
 'acasemupr':'semi_coop',
 'acassmucr':'sing_condo',
 'acassmuer':'sing_rental',
 'acassmuhr':'sing_other',
 'acassmuor':'sing_homeowner',
 'acassmupr':'sing_coop',
 'acasrmucr':'row_condo',
 'acasrmuer':"row_rental",
 'acasrmuhr':'row_other',
 'acasrmuor':'row_homeowner',
 'acasrmupr':'row_coop',
 'acaua31ur':'uni_onebd',
 'acaua32ur':'uni_twobd',
 'acaua33ur':'uni_thrbd',
 'acaua3bur':'uni_zerobd',
 'acaua3tur':'uni_tot',
 'acava31rr':'vac_onebd',
 'acava32rr':'vac_twobd',
 'acava33rr':'vac_thrbd',
 'acava3brr':'vac_zerobd',
 'acava3trr':'vac_tot',
 'acara3tcr':'rent_tot',
 'acarat31cr':'rent_onebd',
 'acarat32cr':'rent_twobd',
 'acarat33cr':'rent_thrbd',
 'acarat3bcr':'rent_zerobd',
 'acapa31rr':'rent_chg_onebd',
 'acapa32rr':'rent_chg_twobd',
 'acapa33rr':'rent_chg_thrbd',
 'acapa3brr':'rent_chg_zerobd',
 'acapa3trr':'rent_chg_tot'
 }


# last quarter for series
recent_q = '2021Q4'
recent_m = '2022M02'
recent_a='2021'


command = 'workfile quarterly q 1980Q1 '+recent_q

#create workfile

print('creating workfile')
evp.Run(command,app = eviewsapp)
#open pareto db
print('opening pareto')
evp.Run('open '+pareto_db,app = eviewsapp)

for series in geo_q_series:
    
    print('fetching '+series)
    

    command= "fetch " + series.lower()
    evp.Run(command,app = eviewsapp)

    df=evp.GetWFAsPython(app=eviewsapp, wfname="quarterly", namefilter=series.lower())
    
    df=df.rename(columns={series.upper():name_scheme[series.upper()]})
    os.makedirs('data/pareto',exist_ok=True)
    print('dumping: ' + name_scheme[series])
    df.to_csv('data/pareto/'+name_scheme[series]+'.csv')

m_command = 'workfile monthly m 1980M01 '+recent_m
evp.Run(m_command,app = eviewsapp)
#open pareto db

for series in geo_m_series:
    
    print('fetching '+series)
    

    command= "fetch " + series.lower()
    evp.Run(command,app = eviewsapp)

    df=evp.GetWFAsPython(app=eviewsapp, wfname="monthly", namefilter=series.lower())
    
    df=df.rename(columns={series:name_scheme[series.lower()]})
    os.makedirs('data/pareto',exist_ok=True)
    print('dumping: ' + name_scheme[series.lower()])
    df.to_csv('data/pareto/'+name_scheme[series.lower()]+'.csv')

    
a_command = 'workfile annual a 1992 '+recent_a
evp.Run(a_command,app = eviewsapp)

for series in geo_a_series:
    
    print('fetching '+series)
    

    command= "fetch " + series.lower()
    evp.Run(command,app = eviewsapp)

    df=evp.GetWFAsPython(app=eviewsapp, wfname="annual", namefilter=series.lower())
    
    df=df.rename(columns={series:name_scheme[series.lower()]})
    os.makedirs('data/pareto',exist_ok=True)
    print('dumping: ' + name_scheme[series.lower()])
    df.to_csv('data/pareto/'+name_scheme[series.lower()]+'.csv')

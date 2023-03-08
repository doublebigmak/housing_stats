#script to pull eviews data from pareto -> pandas-> csv files for storage/usage

import pyeviews as evp
import numpy as np
import pandas as pd
import os

#start eviews
eviewsapp =evp.GetEViewsApp(instance='either',showwindow=False)

#make sure you establish connection to thsi folder first
pareto_db = 'Z:\\DATABASE\\pareto.edb'

# last quarter for series
recent_q = '2022Q4'
recent_m = '2022M12'
recent_a='2022'

geo = 'AZZ'


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


name_scheme = {"acanliuna_q":"new_list_sa",
 "acanliunr_q":"new_list_act",
 "acapricna_q":"avg_price_sa",
 "acapricnr_q":"avg_price_act",
 "acasaluna_q":"sales_sa",
 "acasalunr_q":"sales_act",
 "acasmmura_q":"multi_starts",
 "acassmura_q":"single_starts",
 "acastmura_q":"total_starts",
 "acasnlrva_q":"sales_new_list",
 "acasmmura_q":"multi_starts_saar",
 "acassmura_q":"single_starts_saar",
 "acastmura_q":"total_starts_saar",
 "acasnlrva_q":"snl_sa",
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




#open pareto db
print('opening pareto')
evp.Run('open '+pareto_db,app = eviewsapp)



def fetch_series(series_group,timeframe,current_time):

    if (timeframe == 'monthly'):
        workfile_cmd = 'workfile monthly m 1980M01 '+current_time
    elif (timeframe=='quarterly'):
        workfile_cmd = 'workfile quarterly q 1980Q1 '+current_time
    else:
        workfile_cmd = 'workfile annual a 1992 '+current_time
    print('creating workfile')
    evp.Run(workfile_cmd,app = eviewsapp)


    for series in series_group:
    
        print('fetching '+series)
        

        command= "fetch " + series.lower()
        evp.Run(command,app = eviewsapp)

        df=evp.GetWFAsPython(app=eviewsapp, wfname=timeframe, namefilter=series.lower())
        
        name = series.lower()
        try:
            #df=df.rename(columns={series:name_scheme[name]})
            os.makedirs('data/pareto',exist_ok=True)
            print('dumping: ' + name_scheme[name])
            #df.to_csv('data/pareto/'+name_scheme[name]+'.csv')
            df.to_csv('data/pareto/'+name+'.csv')
        except KeyError as e:
            os.makedirs('data/pareto',exist_ok=True)
            print('dumping: ' + name)
            df.to_csv('data/pareto/'+name+'.csv')



fetch_series(geo_m_series,'monthly',recent_m)
fetch_series(geo_a_series,'annual',recent_a)
fetch_series(geo_q_series,'quarterly',recent_q)

resales = 'abrnliunr_q,abrpricnr_q,abrsalunr_q,abrvolcnr_q,acanliunr_q,acapricna_q,acapricnr_q,acasaluna_q,acasalunr_q,acasmmura_q,acassmura_q,acastmura_q,acavolcnr_q,aednliunr_q,aedpricnr_q,aedsalunr_q,aedvolcnr_q,afmnliunr_q,afmpricnr_q,afmsalunr_q,afmvolcnr_q,agpnliunr_q,agppricnr_q,agpsalunr_q,agpvolcnr_q,alenliunr_q,alepricnr_q,alesalunr_q,alevolcnr_q,almnliunr_q,almpricnr_q,almsalunr_q,almvolcnr_q,amenliunr_q,amepricnr_q,amesalunr_q,amevolcnr_q,anenliunr_q,anepricnr_q,anesalunr_q,anevolcnr_q,arenliunr_q,arepricnr_q,aresalunr_q,arevolcnr_q,awenliunr_q,awepricnr_q,awesalunr_q,awevolcnr_q,azznliunr_q,azzpricnr_q,azzsalunr_q,azzvolcnr_q'.split(',')
starts = 'acasamurr,acasemurr,acasrmurr,acassmurr,acastmurr,aedsamurr,aedsemurr,aedsrmurr,aedssmurr,aedstmurr,agpsalurr,agpselurr,agpsrlurr,agpsslurr,agpstlurr,alesalurr,aleselurr,alesrlurr,alesslurr,alestlurr,amesalurr,ameselurr,amesrlurr,amesslurr,amestlurr,aresalurr,areselurr,aresrlurr,aresslurr,arestlurr,awbsalurr,awbselurr,awbsrlurr,awbsslurr,awbstlurr,azzsauurr,azzseuurr,azzsruurr,azzssuurr,azzstuurr'.split(',')

#fetch_series(resales,'quarterly',recent_q)
#fetch_series(starts,'monthly',recent_m)

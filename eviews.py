#script to pull eviews data from pareto -> pandas-> csv files for storage/usage

import pyeviews as evp
import numpy as np
import pandas as pd
import os

#start eviews
eviewsapp =evp.GetEViewsApp(instance='either',showwindow=True)

pareto_db = 'Z:\\DATABASE\\pareto.edb'

q_series = ["ACANLIUNA_Q", 
"ACANLIUNR_Q",
"ACAPRICNA_Q",
"ACAPRICNR_Q",
"ACASALUNA_Q",
"ACASALUNR_Q",
"ACASMMURA_Q",
"ACASSMURA_Q",
"ACASTMURA_Q",
"ACASNLRVA_Q",
"ACASMMURA_Q",
"ACASSMURA_Q",
"ACASTMURA_Q"]

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
 "ACASNLRVA_Q":"snl_sa"}

#create workfile
print('creating workfile')
evp.Run('workfile quarterly q 1980Q1 2021Q4',app = eviewsapp)
#open pareto db
print('opening pareto')
evp.Run('open Z:\\DATABASE\\pareto.edb',app = eviewsapp)

for series in q_series:
    
    print('fetching '+series)
    

    command= "fetch " + series.lower()
    evp.Run(command,app = eviewsapp)

    df=evp.GetWFAsPython(app=eviewsapp, wfname="quarterly", namefilter=series.lower())
    
    df=df.rename(columns={series:name_scheme[series]})
    os.makedirs('data/pareto',exist_ok=True)
    print('dumping: ' + name_scheme[series])
    df.to_csv('data/pareto/'+name_scheme[series]+'.csv')
    
    
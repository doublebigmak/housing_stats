import pandas as pd
import os
from datetime import datetime, date, timedelta


#resale excel file path local
#path = 'C:\\Users\\mmak\\Desktop\\calgary\\Calgary_Resale.xlsx'
#pra_mac drive
path = 'J:\\Alberta\\Calgary\\Calgary_Resale.xlsx'

current_day = date.today().replace(day=1)
current_month = datetime.now().month
prev_month = current_day - timedelta(days=1)
os.makedirs('data/calgary_resales',exist_ok=True)

'''
Code for Economic Region sheet
'''
# date range for ER sheet
date_range = pd.date_range(start='2014/01/01', end = prev_month, freq='M')

# read ER sheet
df = pd.read_excel(path,engine='openpyxl',sheet_name='CREB - Economic Region', header=[3,4])
df=df[:len(date_range)]

#collapsing multiindex column
df.columns=df.columns.map(' '.join).str.strip(' ')
df=df.set_index(date_range)

df=df.filter(items=['# Sales','New Listings','Active Listings','Average Price','Benchmark Price'])
df.columns = ['er_sales','er_new_listings','er_active_listings','er_avg_price','er_benchmark_price']

for columns in df.columns:
    print('dumping '+columns)
    df[columns].to_csv('data/calgary_resales/'+columns+'.csv')

'''
City of Calgary data
'''

date_range = pd.date_range(start='2006/01/01', end = prev_month, freq='M')
sheet_names = ['CREB - City of Calgary Total','CREB - City Detached','CREB - City Apartment','CREB - City Semi-detached','CREB - City Row']
for sheet in sheet_names:
    #read sheets
    data = pd.read_excel(path,engine='openpyxl',sheet_name=sheet, header=[3,4])
    
    data=data[:len(date_range)]
    data.columns=data.columns.map(' '.join).str.strip(' ')
    data=data.set_index(date_range)
    
    
    
    sheet_prefix = sheet.split()[-1].lower()
    if sheet_prefix == 'total':
        data=data.filter(items=['# Sales','New Listings','Active Listings','Average Price','Benchmark Price','Index (HPI)','Days on Market','Sales$ / List$'])
    
        cols=['sales','new_listings','active_listings','avg_price','benchmark_price','hpi','dom','slpr']
        cols = [sheet_prefix+'_'+col for col in cols]
    else:
        data=data.filter(items=['# Sales','New Listings','Active Listings','Average Price','Benchmark Price','Days on Market','Sales$ / List$'])
    
        cols=['sales','new_listings','active_listings','avg_price','benchmark_price','dom','slpr']
        cols = [sheet_prefix+'_'+col for col in cols]
        
    data.columns = cols
    
    for column in data.columns:
        print('dumping '+column)
        data[column].to_csv('data/calgary_resales/'+column+'.csv')

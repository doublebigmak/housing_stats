import pandas as pd
from os import listdir, getcwd
from os.path import isfile

current_dir = getcwd()

print(current_dir)

resales_dir = current_dir+'/data/calgary_resales'
for file in listdir(resales_dir):

    if '_avg_price' in file:
        #get first word of string

        series_var = file.split('_')[0]
        avg_price = pd.read_csv(resales_dir+'/'+file, index_col=0)
        sales = pd.read_csv(resales_dir+'/'+(series_var+'_sales.csv'),index_col=0)


 
        vol = avg_price.iloc[:,0]*sales.iloc[:,0]
        vol.rename(series_var+'_volume',inplace=True)
        vol.to_csv(resales_dir+'/'+series_var+'_volume.csv')
        


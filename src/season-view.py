import csv
import pandas as pd
import matplotlib.pyplot as plt

from Log import *

PATH = 'database/'


def getColumn(df, dimension):
    return (df.iloc[:, dimension])


def plot(x, y, title, unit):
    plt.plot(x, y[0], label = "Verão", color="r", marker=".")
    plt.plot(x, y[1], label = "Outono", color="darkorange", marker=".")
    plt.plot(x, y[2], label = "Inverno", color="b", marker=".")
    plt.plot(x, y[3], label = "Primavera", color="g", marker=".")
    plt.grid()
    
    plt.title(title+" do Rio Paraíba do Sul")
    plt.xlabel("Anos")
    plt.ylabel(title+' ('+ unit+')')
    plt.legend()
    plt.savefig('view/'+title+'.pdf', dpi=300) 
    plt.cla()   # Clear axis
    plt.clf()   # Clear figure


if __name__ == "__main__" :
    """ Docs and Reference
        * [loc] 
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
            (https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values)
        * [iloc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)
            (https://stackoverflow.com/questions/14941097/selecting-pandas-column-by-location)
        * [df to csv](https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file)
    """
    l = Log()
    tp_season = ('V','O','I','P')
    title = ('Vazão','Temperatura','pH','Condutividade','OD',
             'HCO3','MPS','Clorofila','COD',
             'NO2','NO3','NH4','NID','NT','NTD','NOD',
             'NP','PO4','PTD','PT','POD', 'PP ','Silica',
             'Cl','SO','Na','Ca','K','Mg')
    unit = ('m³/s','ºC','','µS/cm','mg/L',
            'meq/L','mg/L','mg/L','mg/L',
            'µM','µM','µM','µM','µM','µM','µM',
            'µM','µM','µM','µM','µM', 'µM','µM',
            'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L')
   
    df_v = pd.read_csv(PATH+'avg/'+tp_season[0].lower()+'.csv')
    df_o = pd.read_csv(PATH+'avg/'+tp_season[1].lower()+'.csv')
    df_i = pd.read_csv(PATH+'avg/'+tp_season[2].lower()+'.csv')
    df_p = pd.read_csv(PATH+'avg/'+tp_season[3].lower()+'.csv')
    
    x = getColumn(df_v, 0)
    
    for i in range(len(title)):
        y = []
        y.append(df_v.iloc[:, i+1])
        y.append(df_o.iloc[:, i+1])
        y.append(df_i.iloc[:, i+1])
        y.append(df_p.iloc[:, i+1])
        
        # y.append(getColumn(df_v, (i+1)))
        # y.append(getColumn(df_o, (i+1)))
        # y.append(getColumn(df_i, (i+1)))
        # y.append(getColumn(df_p, (i+1)))
        
        plot(x, y, title[i], unit[i])
        
    l.time('view')
import pandas as pd

from library.Log import Log
from library.Graph import Graph

PATH = 'database/'


if __name__ == "__main__" :
    l = Log()
    tp_season = ('V','O','I','P')
    label = ('Verão','Outuno','Inverno','Primavera')
    header = ('Vazão','Temperatura','pH','Condutividade','OD',
             'HCO3','MPS','Clorofila','COD',
             'NO2','NO3','NH4','NID','NT','NTD','NOD',
             'NP','PO4','PTD','PT','POD', 'PP ','Silica',
             'Cl','SO','Na','Ca','K','Mg','Ano')
    unit = ('m³/s','ºC','','µS/cm','mg/L',
            'meq/L','mg/L','mg/L','mg/L',
            'µM','µM','µM','µM','µM','µM','µM',
            'µM','µM','µM','µM','µM', 'µM','µM',
            'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L','')
    
    df_v = pd.read_csv(PATH+'avg/'+tp_season[0].lower()+'.csv')
    df_o = pd.read_csv(PATH+'avg/'+tp_season[1].lower()+'.csv')
    df_i = pd.read_csv(PATH+'avg/'+tp_season[2].lower()+'.csv')
    df_p = pd.read_csv(PATH+'avg/'+tp_season[3].lower()+'.csv')
    
    g = Graph('Rio Paraíba do Sul', header, unit)
    x = df_v.iloc[:, 0]

    for i in range((len(header)-1)):
        y = []
        y.append(df_v.iloc[:, i+1])
        y.append(df_o.iloc[:, i+1])
        y.append(df_i.iloc[:, i+1])
        y.append(df_p.iloc[:, i+1])
        
        g.plot(x, y, (-1), i, label)
        g.boxplot(y, (-1), i)
        g.violinplot(y, (-1), i)
    
    l.time('view')
    
    
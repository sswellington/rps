import pandas as pd

from library.Log import Log
from library.Graph import Graph

PATH = 'database/preprocessing.csv'


if __name__ == "__main__" :
    l = Log('plot')
    label = ('V','O','I','P')
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
    
    df = pd.read_csv(PATH)

    g = Graph('Rio Paraíba do Sul')
    starting_year = int(df['YYYY'].min())
    final_year = int(df['YYYY'].max())
    del df['YYYY']
    
    x = []
    for i in range(starting_year, final_year):
        x.append(i)

    for i in range((len(header)-1)):
        y = []
        y.append(df.iloc[:, 0])
        df = df.drop(df.columns[0], axis=1)
     
        # g.plot(x, y, header(-1), header(i), label)
        # g.boxplot(y, -1, i)
        # g.violinplot(y, -1, i)
    
    l.time()
    
    
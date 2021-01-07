import pandas as pd

from library.Graph import Graph


PATH = 'database/preprocessing.csv'
LABEL = ('V','O','I','P')
# UNIT = ('m³/s','ºC','','µS/cm','mg/L',
#         'meq/L','mg/L','mg/L','mg/L',
#         'µM','µM','µM','µM','µM','µM','µM',
#         'µM','µM','µM','µM','µM', 'µM','µM',
#         'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L','')


if __name__ == "__main__" :
    
    df = pd.read_csv(PATH)
    del df['YYYY']
    
    header = []
    for i in df.columns: 
        header.append(i)
    header.pop()
    
    g = Graph()

    for i in range(len(header)):
        swap = header.pop(0)
        for j in LABEL:
            y = []
            query = df[df['class'] == j]
            y.append(query.iloc[:, 0])
            del query
               
            g.boxplot(y, swap, j)
            g.violinplot(y, swap, j)
            
        df = df.drop(df.columns[0], axis=1)
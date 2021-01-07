import pandas as pd

from library.Graph import Graph


PATH = 'database/preprocessing.csv'


if __name__ == "__main__" :
    
    df = pd.read_csv(PATH)
    del df['YYYY']
    del df['class']
    
    header = []
    for i in df.columns: 
        header.append(i)
    
    g = Graph()

    for i in range(len(header)):
        y = []
        y.append(df.iloc[:, 0])
        df = df.drop(df.columns[0], axis=1)
        
        swap = header.pop(0)
        
        g.boxplot(y, swap, 'every')
        g.violinplot(y, swap, 'every')
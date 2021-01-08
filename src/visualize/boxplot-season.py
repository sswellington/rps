import pandas as pd
import matplotlib.pyplot as plt

from library.Set_up import Set_up


PATH = 'database/preprocessing.csv'
LABEL = ('V','O','I','P')


if __name__ == "__main__" :
    unit = ['m³/s','ºC','','µS/cm','mg/L',
        'meq/L','mg/L','mg/L','mg/L',
        'µM','µM','µM','µM','µM','µM','µM',
        'µM','µM','µM','µM','µM', 'µM','µM',
        'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L']

    df = pd.read_csv(PATH)
    del df['YYYY']
    
    header = []
    for i in df.columns: 
        header.append(i)
    header.pop()

    su = Set_up()
    for i in range(len(header)):
        su.set_up(header.pop(0), unit.pop(0))
        for j in LABEL:
            y = ((df[df['class'] == j]).iloc[:, 0])
        
            plt.boxplot(y)
            su.plt()
            su.save('view/boxplot/' + su.get_header() + '-' + j)
            
            plt.violinplot(y)
            su.plt()
            su.save('view/violinplot/' + su.get_header() + '-' + j)

        df = df.drop(df.columns[0], axis=1)
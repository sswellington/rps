import pandas as pd
import matplotlib.pyplot as plt

from library.Const import Const
from library.Set_up import Set_up


if __name__ == "__main__" :
    const = Const()

    df = pd.read_csv(const.path)
    del df['YYYY']
    
    header = []
    for i in df.columns: 
        header.append(i)
    header.pop()

    su = Set_up()
    for i in range(len(header)):
        su.set_up(header.pop(0), const.unit.pop(0))
        for j in const.label:
            y = ((df[df['class'] == j]).iloc[:, 0])
        
            plt.boxplot(y)
            su.plt()
            su.save('view/boxplot/' + su.get_header() + '-' + j)
            
            plt.violinplot(y)
            su.plt()
            su.save('view/violinplot/' + su.get_header() + '-' + j)

        df = df.drop(df.columns[0], axis=1)
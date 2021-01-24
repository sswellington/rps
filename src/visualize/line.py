import matplotlib.pyplot as plt
from pandas import read_csv as pd_read_csv

from library import Const


LINE_STYLE = ('-', '--', '-.',':')
SEASON = ('Verão', 'Outono', 'Inverno', 'Primavera')


if __name__ == "__main__" :
    const = Const()
    df = pd_read_csv(const.path)
    
    starting_year = int(df['YYYY'].min())
    final_year = int(df['YYYY'].max()) + 1
    del df['YYYY']
    
    x = []
    for i in range(starting_year, final_year):
        x.append(i)
        
    header = []
    for i in df.columns: 
        header.append(i)
    header.pop()
    
    c = 0
    for i in range(len(header)):
        swap = header.pop(0)
        k = 0
        for j in const.label:
            y = ((df[df['class'] == j]).iloc[:, 0])
            
            plt.plot(x, y, label = SEASON[k], linestyle = LINE_STYLE[k], marker = '.')
            k += 1
            
        plt.title('Rio Paraíba do Sul: ' + swap)
        plt.xlabel('Anos')
        plt.ylabel(swap + ' - ' + const.unit[c])
        plt.legend()
        plt.grid()
    
        plt.savefig('view/line/'+ swap +'.pdf', dpi=300)
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure
        
        c += 1    
        df = df.drop(df.columns[0], axis=1)
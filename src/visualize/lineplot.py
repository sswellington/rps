import pandas as pd
import matplotlib.pyplot as plt


PATH = 'database/preprocessing.csv'
LABEL = ('V','O','I','P')
UNIT = ('m³/s','ºC','','µS/cm','mg/L',
        'meq/L','mg/L','mg/L','mg/L',
        'µM','µM','µM','µM','µM','µM','µM',
        'µM','µM','µM','µM','µM', 'µM','µM',
        'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L','')
LINE_STYLE = ('-', '--', '-.',':')
SEASON = ('Verão', 'Outono', 'Inverno', 'Primavera')


if __name__ == "__main__" :
    
    df = pd.read_csv(PATH)
    
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
        for j in LABEL:
            query = df[df['class'] == j]
            y = (query.iloc[:, 0])
            del query
            
            plt.plot(x, y, label = SEASON[k], linestyle = LINE_STYLE[k], marker = '.')
            k += 1
            
        plt.title('Rio Paraíba do Sul: ' + swap)
        plt.xlabel('Anos')
        plt.ylabel(swap + ' - ' + UNIT[c])
        plt.legend()
        plt.grid()
    
        plt.savefig('view/line/'+ swap +'.pdf', dpi=300)
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure
        
        c += 1    
        df = df.drop(df.columns[0], axis=1)
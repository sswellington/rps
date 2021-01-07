import pandas as pd
import matplotlib.pyplot as plt


PATH = 'database/preprocessing.csv'
LABEL = ('V','O','I','P')
# UNIT = ('m³/s','ºC','','µS/cm','mg/L',
#         'meq/L','mg/L','mg/L','mg/L',
#         'µM','µM','µM','µM','µM','µM','µM',
#         'µM','µM','µM','µM','µM', 'µM','µM',
#         'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L','')


if __name__ == "__main__" :
    
    df = pd.read_csv(PATH)
    
    starting_year = int(df['YYYY'].min())
    final_year = int(df['YYYY'].max()) + 1
    del df['YYYY']
    
    header = []
    for i in df.columns: 
        header.append(i)
    header.pop()
    
    x = []
    for i in range(starting_year, final_year):
        x.append(i)
    
    for i in range(1):
        swap = header.pop(0)
        for j in LABEL:
            y = []
            query = df[df['class'] == j]
            y.append(query.iloc[:, 0])
            del query
            
            plt.plot(x, y, label = "blue", color="b", marker=".")

            plt.title('Example: graph')
            plt.xlabel("X axis")
            plt.ylabel("Y axis")
            plt.legend()
            
            plt.savefig('view/line/a.pdf', dpi=300)
                
        df = df.drop(df.columns[0], axis=1)

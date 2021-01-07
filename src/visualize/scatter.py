import pandas as pd
import matplotlib.pyplot as plt


PATH = 'database/preprocessing.csv'


if __name__ == "__main__" :
    HEADER = ('Vazão', 'Temperatura', 'pH', 'Condutividade', 'OD',
              'HCO3', 'MPS','Clorofila', 'COD',
              'NO', 'NO.1', 'NH', 'NI', 'N', 'NT', 'NOD',
              'NP', 'PO4', 'PTD', 'PT', 'PO', 'PP', 'Silica', 
              'Cl', 'SO4', 'Na', 'Ca', 'K', 'Mg')

    len_header = len(HEADER)
    df = pd.read_csv(PATH)
    
    for i in range(len_header):
        for j in range(len_header):
            df.plot.scatter(x = HEADER[i], y = HEADER[j], c='DarkBlue')
            plt.savefig('view/scatter/' + HEADER[i] + '-vs-' + HEADER[j] +'.pdf', dpi=300) 
            plt.cla()   # Clear axis
            plt.clf()   # Clear figure
import pandas as pd
import matplotlib.pyplot as plt


PATH = 'database/'


if __name__ == "__main__" :
    tp_season = ('V','O','I','P')
    header = ('Vazão','Temperatura','pH','Condutividade','OD',
            'HCO3','MPS','Clorofila','COD',
            'NO2','NO3','NH4','NID','N','NT','NOD',
            'NP','PO4','PTD','PT','POD','PP','Silica',
            'Cl','SO4','Na','Ca','K','Mg')

    lower = tp_season[0].lower()

    df = pd.read_csv(PATH+'avg/'+lower+'.csv')

    len_header = len(header)
    
    for i in range(len_header):
        for j in range(len_header):
            df.plot.scatter(x=header[i],y=header[j], c='DarkBlue')
            plt.savefig('view/scatter/'+header[i]+'-vs-'+header[j]+'.pdf', dpi=300) 
            plt.cla()   # Clear axis
            plt.clf()   # Clear figure
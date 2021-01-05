import numpy as np
import pandas as pd

from library.Graph import Graph


PATH = 'database/'

if __name__ == "__main__" :
    '''
        0.9 a 1 positivo ou negativo indica uma correlação muito forte.
        0.7 a 0.9 positivo ou negativo indica uma correlação forte.
        0.5 a 0.7 positivo ou negativo indica uma correlação moderada.
        0.3 a 0.5 positivo ou negativo indica uma correlação fraca.
        0.0 a 0.3 positivo ou negativo indica uma correlação desprezível.
        https://medium.com/brdata/correla%C3%A7%C3%A3o-direto-ao-ponto-9ec1d48735fb
    '''
    tp_season = ('V','O','I','P')
    header = ('Vazão','Temperatura','pH','Condutividade','OD',
            'HCO3','MPS','Clorofila','COD',
            'NO2','NO3','NH4','NID','NT','NTD','NOD',
            'NP','PO4','PTD','PT','POD', 'PP ','Silica',
            'Cl','SO','Na','Ca','K','Mg')
    g = Graph('Correlação de Pearson sobre o RPS', None, None)
    
    for s in tp_season:
        lower = s.lower()
        df = pd.read_csv(PATH+'avg/'+lower+'.csv')
        del df['YYYY']
    
        c_pearson = df.corr()
        g.heatmap(c_pearson, lower)
        
        # c_pearson = df.corr().stack().reset_index(name="correlation")
        # g.s_heatmap(c_pearson, lower)
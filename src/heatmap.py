import numpy as np
import pandas as pd

from library.Graph import Graph


PATH = 'database/preprocessing.csv'

if __name__ == "__main__" :
    '''
        0.9 a 1 positivo ou negativo indica uma correlação muito forte.
        0.7 a 0.9 positivo ou negativo indica uma correlação forte.
        0.5 a 0.7 positivo ou negativo indica uma correlação moderada.
        0.3 a 0.5 positivo ou negativo indica uma correlação fraca.
        0.0 a 0.3 positivo ou negativo indica uma correlação desprezível.
        https://medium.com/brdata/correla%C3%A7%C3%A3o-direto-ao-ponto-9ec1d48735fb
    '''
    label = ('V','O','I','P')
    g = Graph('Correlação de Pearson sobre o RPS')
    df = pd.read_csv(PATH)
    del df['YYYY']
    
    c_pearson = df.corr()
    g.heatmap(c_pearson,'every')
    
    c_pearson = df.corr().stack().reset_index(name="correlation")
    g.s_heatmap(c_pearson, 'every')
    
    for i in label:
        query = df[df['class'] == i]
        
        c_pearson = df.corr()
        g.heatmap(c_pearson, i)
        
        c_pearson = df.corr().stack().reset_index(name="correlation")
        g.s_heatmap(c_pearson, i)

        
    
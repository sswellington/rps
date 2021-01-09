import numpy as np
import pandas as pd

from library.Const import Const
from library.Graph import Graph


if __name__ == "__main__" :
    const = Const()
    g = Graph()
    df = pd.read_csv(const.path)
    del df['YYYY']
    
    pearson = df.corr()
    g.heatmap(pearson,'every')
    
    pearson = df.corr().stack().reset_index(name="correlation")
    g.heatmap_scatter(pearson, 'every')
    
    for i in const.label:
        query = df[df['class'] == i]
        
        pearson = df.corr()
        g.heatmap(pearson, i)
        
        pearson = df.corr().stack().reset_index(name="correlation")
        g.heatmap_scatter(pearson, i)


    ''' Pearson Correlation Coefficient (PCC)
        
            Size of Correlation     |              Interpretation
        0.90 to 1.00 (−.90 to −1.0)	| Very high positive (negative) correlation
        0.70 to 0.90 (−.70 to −.90)	| High positive      (negative) correlation
        0.50 to 0.70 (−.50 to −.70)	| Moderate positive  (negative) correlation
        0.30 to 0.50 (−.30 to −.50)	| Low positive       (negative) correlation
        0.00 to 0.30 (0.00 to −.30)	| Negligible correlation
            
        References
            https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3576830/
            https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php
            https://medium.com/brdata/correla%C3%A7%C3%A3o-direto-ao-ponto-9ec1d48735fb
    '''
        
    
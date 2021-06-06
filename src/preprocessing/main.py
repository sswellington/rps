import logging
""" Pandas
    import only the method pd.read_csv(),
    thus avoiding importing the entire structure of the pandas class object
"""
from pandas import read_csv as pd_read_csv

from assets import Preprocessing


if __name__ == "__main__" :
    logging.basicConfig(filename=('log/preprocessing.txt'),
                level=logging.ERROR, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
    
    PATH_OF_DATABASE = 'database/source.csv'
    LABEL_OF_SEASONS_OF_YEAR = ('V','O','I','P')
    
    try: 
        df = pd_read_csv(PATH_OF_DATABASE)
    except:
        logging.error('pandas did not find the dataset source')
    finally:
        del PATH_OF_DATABASE
        
    rps = Preprocessing(df)
    del df
    rps.export(LABEL_OF_SEASONS_OF_YEAR, 'database/preprocessing.csv')
    del rps
    del LABEL_OF_SEASONS_OF_YEAR
    
import logging
from pandas import read_csv as pd_read_csv

from library import Preprocessing


if __name__ == "__main__" :
    logging.basicConfig(filename=('log/preprocessing.txt'),
                level=logging.ERROR, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
    
    PATH = 'database/source.csv'
    LABEL = ('V','O','I','P')
    
    try: 
        df = pd_read_csv(PATH)
    except:
        logging.error('pandas did not find the dataset source')
    finally:
        del PATH
        
    rps = Preprocessing(df)
    del df
    
    rps.export(LABEL, 'database/preprocessing.csv')
    del rps
    del LABEL
    
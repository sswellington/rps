import logging
import matplotlib.pyplot as plt
from pandas import read_csv as pd_read_csv

from library import Const


if __name__ == "__main__" :
    logging.basicConfig(filename=('log/view-scatter.txt'),
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable()
    logging.debug('Start of program')
    
    const = Const()
    df = pd_read_csv(const.path)
    del df['YYYY']
    del df['class']
    
    header = []
    for i in df.columns: 
        header.append(i)
    
    len_header = len(header)
    
    logging.debug('PATH: ' + const.path)
    logging.debug('header.len: ' + str(len_header))
    logging.debug('header: ' + str(header))
    
    for i in range(len_header):
        for j in range(len_header):
            df.plot.scatter(x = header[i], y = header[j], c='DarkBlue')
            plt.savefig('view/scatter/' + header[i] + '-vs-' + header[j] +'.pdf', dpi=300) 
            plt.cla()   # Clear axis
            plt.clf()   # Clear figure
            
    logging.debug('End of program')

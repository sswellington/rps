# /usr/bin/env python3.9.0

import logging
import time
from pandas import read_csv as pd_read_csv


if __name__ == "__main__" :
    logging.basicConfig(filename=("log/test_df_py.txt"),
                level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
    END = 1000 
    sum = 0
    for i in range(END):
        clock = time.time()
        try: 
            df = pd_read_csv("database/source.csv")
        except:
            logging.error("pandas did not find the dataset source")
        clock = time.time() - clock
        sum += clock
        logging.debug(clock)
    logging.info("AVG - " + str(sum/END))
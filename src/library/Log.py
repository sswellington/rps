import sys
import csv
import time


class Log(object):
    
    def __init__(self):
        self._list = []
        self._start = time.time()
        
    
    def time(self, path):
        ''' Return program execution time '''
        end = time.time()
        end -= self._start
        f = open('log/'+path+'.txt', 'a')
        f.write(str(end))
        f.write('\n')
        f.close()
        return (end)
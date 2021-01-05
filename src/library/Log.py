import sys
import csv
import time


class Log(object):
    
    def __init__(self, name):
        self._name = name
        self._start = time.time()
    
    def variable_2_text(self, path, variable):
        f = open(path, 'a')
        f.write(str(variable))
        f.write('\n')
        f.close()
            
    
    def debug(self, variable):
        self.variable_2_text(('log/debug/'+self._name+'.txt'), variable)
    
    
    def time(self):
        ''' Return program execution time '''
        end = time.time()
        end -= self._start
        self.variable_2_text(('log/runtime/'+self._name+'.txt'), end)
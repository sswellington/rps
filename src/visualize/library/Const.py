class Const(object):
    
    def __init__(self):
        
        self.path = 'database/preprocessing.csv'
        self.label = ('V','O','I','P')
        
        self.unit = ['m³/s'  , 'ºC'  , ''    , 'µS/cm', 'mg/l', 'meq/l',	
                'mg/l'  , 'mg/l', 'mg/l',	
                'µM'    , 'µM'  , 'µM'  , 'µM'   , 'µM'  , 'µM',	
                'mg/l'  , 'mg/l', 'mg/l', 'mg/l' ,'mg/l']
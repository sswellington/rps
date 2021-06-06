import csv
from pandas import DataFrame as pd_DataFrame


""" preprocessing: 
    RPS dataframe
        * Number of Instances: 569 + header
        * Number of Attributes: 23 + class
        * Attribute information:
            01. coleta:
            02. YYYY:
            03. MM
            04. Vazão
            05. Temperatura
            06. pH
            07. Condutividade
            08. OD
            09. HCO3
            10. MPS
            11. Clorofila
            12. COD
            13. NO2
            14. NO3
            15. NH4
            16. NID
            17. PO4
            18. Silica
            19. Cloro
            20. Na
            21. Ca
            22. K
            23. Mg
            24. class
    Remove column:
        * coleta
        * MM
    Mean of seasons per year  
"""
class Preprocessing(object):
    
    def __init__(self, df):
        self.index = 0
        self.start_year = 1995
        self.final_year = 2020

        self.df_cp = df
        self.del_column_id_and_month()
        self.set_header(df)
        del df
    
    
    def del_column_id_and_month(self) -> pd_DataFrame:
        del self.df_cp['MM']
        del self.df_cp['coleta']
        return self.df_cp 
        
    
    def df_new(self, year, label) -> pd_DataFrame:
        season = self.query_year_and_label(year, label)
        season = self.df_to_list(season, label)
        
        self.df.loc[self.index] = season
        del season
        self.index += 1
        
        return self.df
    
    
    def df_to_csv(self, path) -> None:
        self.df.to_csv(path, encoding='utf-8', index=False)  
    
    
    def df_to_list(self, df, label) -> list:
        df = (df.mean())
        swap = []
        
        for i in df:
            swap.append(i)
        swap.append(label)
        
        return swap
    
            
    def export(self, label, path) -> None:
        for i in range(self.start_year, self.final_year):
            for j in label:
                self.df_new(i, j)    
        self.df_to_csv(path)
        
        
    def query_year_and_label(self, year, label) -> pd_DataFrame:
        return self.df_cp[(self.df_cp['YYYY'] == year) & (self.df_cp['class'] == label)]
        
        
    def set_start_year(self, year) -> None:
        self.start_year = year
        
    
    def set_final_year(self, year) -> None:
        self.final_year = year + 1
    
    
    def set_header(self, df) -> None:
        self.df = pd_DataFrame(df.iloc[[0]])
    
    
    # https://docs.python.org/pt-br/3/library/functions.html?highlight=property#property
    @property
    def index(self):
        return self._index 
    
    @index.setter
    def index(self, index):
        self._index = index
        
    @index.deleter
    def index(self):
        del self._index
       
    
    @property
    def start_year(self):
        return self._start_year 
    
    @start_year.setter
    def start_year(self, start_year):
        self._start_year = start_year
        
    @start_year.deleter
    def start_year(self):
        del self._start_year  
        
        
    @property
    def final_year(self):
        return self._final_year 
    
    @final_year.setter
    def final_year(self, final_year):
        self._final_year = final_year
        
    @final_year.deleter
    def final_year(self):
        del self._final_year   
        

    """ Pandas - DataFrame: Docs and Reference 
        Introduction
            import only the method pd.DataFrame(),
            thus avoiding importing the entire structure of the pandas class object

        * [query]
            (https://stackoverflow.com/questions/22591174/pandas-multiple-conditions-while-indexing-data-frame-unexpected-behavior)
        * [loc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
            (https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values)
        * [iloc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)
            (https://stackoverflow.com/questions/14941097/selecting-pandas-column-by-location)
        * [Remove Columns](https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe)
            del
                del df['column_name']
                del df.column_name
            drop
                df.drop(columns=['coleta', 'MM'])
                df.drop(['coleta', 'MM'], axis=1, inplace=True)
        * [Dataframe to CSV](https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file)
    """
    
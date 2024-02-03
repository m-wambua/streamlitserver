# file_reader.py
import pandas as pd
import streamlit as st

class FileReader:
    def __init__(self, file_path, method, parameters):
        self.file_path = file_path
        self.method = method
        self.parameters = parameters

    def read_file(self):
        try:
            if self.method == 'CSV':
                return pd.read_csv(self.file_path, **self.parameters)
            elif self.method in ['XLS', 'XLSX']:
                return pd.read_excel(self.file_path, **self.parameters)
            elif self.method == 'JSON':
                return pd.read_json(self.file_path, **self.parameters)
            elif self.method == 'PARQEUT':
                return pd.read_parquet(self.file_path, **self.parameters)
            elif self.method == 'FEATHER':
                return pd.read_feather(self.file_path, **self.parameters)
            elif self.method in ['H5', 'HDF5']:
                return pd.read_hdf(self.file_path, **self.parameters)
            elif self.method == 'MSGPACK':
                return pd.read_msgpack(self.file_path, **self.parameters)
            elif self.method == 'DTA':
                return pd.read_stata(self.file_path, **self.parameters)
            elif self.method == 'XML':
                return pd.read_xml(self.file_path, **self.parameters)
            elif self.method=='FWF':
                return pd.read_fwf(self.file_path, **self.parameters)
            elif self.method =='ORC':
                return pd.read_orc(self.file_path, **self.parameters)
            elif self.method == 'HTML':
                return pd.read_html(self.file_path, **self.parameters)
            elif self.method == 'SAS':
                return pd.read_sas(self.file_path, **self.parameters)
            elif self.method =='SPSS':
                return pd.read_spss(self.file_path, **self.parameters)
            elif self.method == 'SQL_TABLE':
                return pd.read_sql_table(self.file_path, **self.parameters)
            
            elif self.method =='SQL QUERY':
                return pd.read_sql_query(self.file_path, **self.parameters)
            
            elif self.method == 'SQL':
                return pd.read_sql(self.file_path, **self.parameters)
            
            elif self.method =='GBQ':
                return pd.read_gbq(self.file_path, **self.parameters)
            
            elif self.method =='STATA':
                return pd.read_stata(self.file_path, **self.parameters
                                     )
            else:
                return None
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return None

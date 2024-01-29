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
                return pd.read_parquet(self.file_path)
            elif self.method == 'FEATHER':
                return pd.read_feather(self.file_path)
            elif self.method in ['H5', 'HDF5']:
                return pd.read_hdf(self.file_path)
            elif self.method == 'MSGPACK':
                return pd.read_msgpack(self.file_path)
            elif self.method == 'DTA':
                return pd.read_stata(self.file_path)
            elif self.method == 'XML':
                return pd.read_xml(self.file_path)
            else:
                return None
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return None

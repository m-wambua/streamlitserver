
from paramters import *

class SelectParameter():
    def select_parameters(self, method):
        if method == 'CSV':
            return list(read_csv_parameters.keys())
        elif method in ['XLS', 'XLSX']:
            return list(read_excel_parameters.keys())
        elif method == 'JSON':
            return list(read_json_parameters.keys())
        elif method == 'PARQUET':
            return list(read_parquet_parameters.keys())
        elif method == 'FEATHER':
            return list(read_feather_parameters.keys())
        elif method == 'H5':
            return list(read_hdf_parameters.keys())
        elif method == 'HDF5':
            return list(read_hdf_parameters.keys())
        elif method == 'ORC':
            return list(read_orc_parameters.keys())
        elif method == 'SAS':
            return list(read_sas_parameters.keys())
        elif method == 'SQL QUERY':
            return list(read_sql_query_parameters.keys())
        elif method == 'SQL TABLE':
            return list(read_sql_table_parameters.keys())
        elif method == 'SQL':
            return list(read_sql_parameters.keys())
        elif method == 'GBQ':
            return list(read_gbq_parameters.keys())
        elif method == 'STATA':
            return list(read_stata_parameters.keys())
        elif method == 'HTML':
            return list(read_html_parameters.keys())
        elif method == 'FWF':
            return list(read_fwf_parameters.keys())
        elif method == 'XML':
            return list(read_xml_parameters.keys())

        # Add more conditions for other reading methods
        else:
            return []

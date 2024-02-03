# parameters.py
read_csv_parameters = {
    'sep': ',',
    'delimiter': None,
    'header': 'infer',
    'names': None,
    'index_col': None,
    'usecols': None,
    'dtype': None,
    'engine': None,
    'converters': None,
    'true_values': None,
    'false_values': None,
    'skipinitialspace': False,
    'skiprows': None,
    'skipfooter': 0,
    'nrows': None,
    'na_values': None,
    'keep_default_na': True,
    'na_filter': True,
    'verbose': None,
    'skip_blank_lines': True,
    'parse_dates': None,
    'infer_datetime_format': False,
    'keep_date_col': False,
    'date_parser': None,
    'date_format': None,
    'dayfirst': False,
    'cache_dates': True,
    'iterator': False,
    'chunksize': None,
    'compression': 'infer',
    'thousands': None,
    'decimal': '.',
    'lineterminator': None,
    'quotechar': '"',
    'quoting': 0,
    'doublequote': True,
    'escapechar': None,
    'comment': None,
    'encoding': None,
    'encoding_errors': 'strict',
    'dialect': None,
    'on_bad_lines': 'error',
    'delim_whitespace': False,
    'low_memory': True,
    'memory_map': False,
    'float_precision': None,
    'storage_options': None,
    'dtype_backend': None
}

read_excel_parameters = {
    'sheet_name': 0,
    'header': 0,
    'names': None,
    'index_col': None,
    'usecols': None,
    'dtype': None,
    'engine': None,
    'converters': None,
    'true_values': None,
    'false_values': None,
    'skiprows': None,
    'nrows': None,
    'na_values': None,
    'keep_default_na': True,
    'na_filter': True,
    'verbose': False,
    'parse_dates': False,
    'date_parser': None,
    'date_format': None,
    'thousands': None,
    'decimal': '.',
    'comment': None,
    'skipfooter': 0,
    'storage_options': None,
    'dtype_backend': None,
    'engine_kwargs': None
}

read_json_parameters = {
    'orient': None,
    'typ': 'frame',
    'dtype': None,
    'convert_axes': None,
    'convert_dates': True,
    'keep_default_dates': True,
    'precise_float': False,
    'date_unit': None,
    'encoding': None,
    'encoding_errors': 'strict',
    'lines': False,
    'chunksize': None,
    'compression': 'infer',
    'nrows': None,
    'storage_options': None,
    'dtype_backend': None,
    'engine': 'ujson'
}

read_parquet_parameters = {
    'engine': 'auto',
    'columns': None,
    'storage_options': None,
    'use_nullable_dtypes': None,
    'dtype_backend': None,
    'filesystem': None,
    'filters': None
    # Add more parameters as needed
}

read_feather_parameters = {
    'columns': None,
    'use_threads': True,
    'storage_options': None,
    'dtype_backend': None
    # Add more parameters as needed
}
read_hdf_parameters = {
    'key': None,
    'mode': 'r',
    'errors': 'strict',
    'where': None,
    'start': None,
    'stop': None,
    'columns': None,
    'iterator': False,
    'chunksize': None,
    # Add more parameters as needed
}

read_orc_parameters = {
    'columns': None,
    'dtype_backend': None,
    'filesystem': None
    # Add more parameters as needed
}


read_fwf_parameters = {
    'colspecs': 'infer',
    'widths': None,
    'infer_nrows': 100,
    'dtype_backend': None,
    'iterator': False,
    'chunksize': None,
    # Add more parameters as needed
}

read_html_parameters = {
    'match': '.+',
    'flavor': None,
    'header': None,
    'index_col': None,
    'skiprows': None,
    'attrs': None,
    'parse_dates': False,
    'thousands': ',',
    'encoding': None,
    'decimal': '.',
    'converters': None,
    'na_values': None,
    'keep_default_na': True,
    'displayed_only': True,
    'extract_links': None,
    'dtype_backend': None,
    'storage_options': None
    # Add more parameters as needed
}


read_sas_parameters = {
    'format': None,
    'index': None,
    'encoding': None,
    'chunksize': None,
    'iterator': False,
    'compression': 'infer'
    # Add more parameters as needed
}


read_spss_parameters = {
    'usecols': None,
    'convert_categoricals': True,
    'dtype_backend': None
    # Add more parameters as needed
}


read_sql_table_parameters = {
    'table_name': None,
    'con': None,
    'schema': None,
    'index_col': None,
    'coerce_float': True,
    'parse_dates': None,
    'columns': None,
    'chunksize': None,
    'dtype_backend': None
    # Add more parameters as needed
}


read_sql_query_parameters = {
    'sql': None,
    'con': None,
    'index_col': None,
    'coerce_float': True,
    'params': None,
    'parse_dates': None,
    'chunksize': None,
    'dtype': None,
    'dtype_backend': None,
    # Add more parameters as needed
}


read_sql_parameters = {
    'sql': None,
    'con': None,
    'index_col': None,
    'coerce_float': True,
    'params': None,
    'parse_dates': None,
    'columns': None,
    'chunksize': None,
    'dtype_backend': None,
    'dtype': None
    # Add more parameters as needed
}


read_gbq_parameters = {
    'query': None,
    'project_id': None,
    'index_col': None,
    'col_order': None,
    'reauth': False,
    'auth_local_webserver': True,
    'dialect': None,
    'location': None,
    'configuration': None,
    'credentials': None,
    'use_bqstorage_api': None,
    'max_results': None,
    'progress_bar_type': None
    # Add more parameters as needed
}


read_stata_parameters = {
    'convert_dates': True,
    'convert_categoricals': True,
    'index_col': None,
    'convert_missing': False,
    'preserve_dtypes': True,
    'columns': None,
    'order_categoricals': True,
    'chunksize': None,
    'iterator': False,
    'compression': 'infer',
    'storage_options': None
    # Add more parameters as needed
}

read_xml_parameters = {
    'xpath': './*',
    'namespaces': None,
    'elems_only': False,
    'attrs_only': False,
    'names': None,
    'dtype': None,
    'converters': None,
    'parse_dates': None,
    'encoding': 'utf-8',
    'parser': 'lxml',
    'stylesheet': None,
    'iterparse': None,
    'compression': 'infer',
    'storage_options': None,
    'dtype_backend': None
    # Add more parameters as needed
}

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

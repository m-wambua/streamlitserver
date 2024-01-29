
'''
app.py
import streamlit as st
import pandas as pd
from InputOutput.fileextension import FileExtension
max_file_size=500*1024*1024
def read_file(file_path, method,parameters):
    try:
        if method == 'CSV':
            return pd.read_csv(file_path, **parameters)
        elif method == 'XLS':
            return pd.read_excel(file_path, engine='xlrd')
        elif method == 'XLSX':
            return pd.read_excel(file_path, engine='openpyxl')
        elif method == 'JSON':
            return pd.read_json(file_path,orient='records')
        elif method == 'PARQEUT':
            return pd.read_parquet(file_path)
        elif method == 'FEATHER':
            return pd.read_feather(file_path)
        elif method in ['H5', 'HDF5']:
            return pd.read_hdf(file_path)
        elif method == 'MSGPACK':
            return pd.read_msgpack(file_path)
        elif method == 'DTA':
            return pd.read_stata(file_path)
        elif method == 'XML':
            return pd.read_xml(file_path)
        else:
            return None
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

with st.sidebar:
    st.title('Dexter Labs')
    choice = st.radio('Navigation', ['Upload', 'Profiling', 'ML', 'Download'])
    st.info('This application allows you to build an automated ML pipeline ')

if choice == 'Upload':
    st.title('Upload your data for modelling')
    file = st.file_uploader('Upload your Dataset here')
    if file:
        if len(file.getvalue())>max_file_size:
            st.warning(f'File size exceeds the maximum allowed size of{max_file_size/(1024*1024)} MB.')
            filecache=st.cache(file)
        else:
            file_extension_handler = FileExtension()
            extension = file_extension_handler.get_file_extension(file.name)
            if extension:
                st.info(f'File Extension: {extension}')

                # Select reading method
                option = st.selectbox('Which Pandas reading Tool Would you prefer',
                                        ('CSV', 'XLS', 'XLSX', 'JSON', 'PARQEUT', 'FEATHER', 'H5', 'HDF5', 'MSGPACK', 'DTA','XML'))

                # Read file using selected method
                df = read_file(file, option)

                if df is not None:
                    st.dataframe(df)
                    st.success(f"File successfully loaded using {option} method.")
            else:
                st.warning('Unable to determine the file extension.')

if choice == 'Profiling':
    pass

if choice == 'ML':
    pass

if choice == 'Download':
    pass
'''
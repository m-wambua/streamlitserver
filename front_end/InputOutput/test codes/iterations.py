
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

'''
import streamlit as st
from InputOutput.data_cleaner import DataCleaner
from app import SessionState
class DataAnalyser:
    def __init__(self,df):
        self.df=df
    
    def run(self):
        st.title('Data Analysis Options')
        choice=st.radio('Select Analysis Types', ['Data information', 'Data Cleaning'])

        if choice=='Data information':
            self.data_info()

        elif choice=='Data Cleaning':
            self.data_cleaning()

        def data_info(self):
            st.subheader('DataFrame Information')
            st.write(self.df.info())

        def data_cleaning_section(self):
            st.title('Data Cleaning')

            # Get user-selected data cleaning options
            cleaning_options = st.multiselect('Select Data Cleaning Options',
                                            ['Handle Missing Values', 'Handle Duplicates', 'Correct Inconsistencies',
                                            'Handle Outliers', 'Handle Inconsistent Data Types', 'Handle Irrelevant Data',
                                            'Handle Inconsistent Formats', 'Handle Categorical Data', 'Scale and Normalize',
                                            'Handle Skewness and Transformation', 'Handle Imbalanced Datasets',
                                            'Data Integrity Checks', 'Data Quality Assessment', 'Iterative Process'])

            data_cleaner = DataCleaner(session_state.df)
            # Apply selected data cleaning options
            for option in cleaning_options:
                if option == 'Handle Missing Values':
                    data_cleaner.handle_missing_values()
                elif option == 'Handle Duplicates':
                    data_cleaner.handle_duplicates()
                elif option == 'Correct Inconsistencies':
                    data_cleaner.correct_inconsistencies()
                elif option == 'Handle Outliers':
                    data_cleaner.handle_outliers()
                elif option == 'Handle Inconsistent Data Types':
                    data_cleaner.handle_inconsistent_data_types()
                elif option == 'Handle Irrelevant Data':
                    columns_to_drop = st.multiselect('Select Columns to Drop', session_state.df.columns)
                    data_cleaner.handle_irrelevant_data(columns_to_drop)
                elif option == 'Handle Inconsistent Formats':
                    date_column = st.selectbox('Select Date Column', session_state.df.columns)
                    data_cleaner.handle_inconsistent_formats(date_column)
                elif option == 'Handle Categorical Data':
                    categorical_columns = st.multiselect('Select Categorical Columns', session_state.df.columns)
                    data_cleaner.handle_categorical_data(categorical_columns)
                elif option == 'Scale and Normalize':
                    data_cleaner.scale_and_normalize()
                elif option == 'Handle Skewness and Transformation':
                    skewed_column = st.selectbox('Select Skewed Column', session_state.df.columns)
                    data_cleaner.handle_skewness_and_transformation(skewed_column)
                elif option == 'Handle Imbalanced Datasets':
                    target_column = st.selectbox('Select Target Column', session_state.df.columns)
                    data_cleaner.handle_imbalanced_datasets(target_column)
                elif option == 'Data Integrity Checks':
                    column1 = st.selectbox('Select First Column', session_state.df.columns)
                    column2 = st.selectbox('Select Second Column', session_state.df.columns)
                    data_cleaner.data_integrity_checks(column1, column2)
                elif option == 'Data Quality Assessment':
                    data_cleaner.data_quality_assessment()
                elif option == 'Iterative Process':
                    data_cleaner.iterative_process()

            # Display cleaned DataFrame
            st.dataframe(data_cleaner.df)
            st.success("Data cleaning completed successfully.")

'''
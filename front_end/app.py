import streamlit as st
from InputOutput.file_reader import FileReader
from InputOutput.fileextension import FileExtension
from InputOutput.paramters import *
from InputOutput.data_cleaner import DataCleaner

# Streamlit SessionState Class
class SessionState:
    def __init__(self):
        self.df = None

session_state = SessionState()

class StreamlitApp:
    def __init__(self):
        self.max_file_size = 500 * 1024 * 1024
        self.default_parameter = {'sep': ',', 'header': 'infer', 'encoding': 'latin1'}

    def run(self):
        with st.sidebar:
            st.title('Dexter Labs')
            choice = st.radio('Navigation', ['Upload', 'Data Cleaning', 'Profiling', 'ML', 'Download'])
            st.info('This application allows you to build an automated ML pipeline ')

        if choice == 'Upload':
            self.upload_section()

        elif choice == 'Data Cleaning':
            if session_state.df is not None:
                self.data_cleaning_section()
            else:
                st.warning('Please upload a file first.')

        elif choice == 'Profiling':
            pass

        elif choice == 'ML':
            pass

        elif choice == 'Download':
            pass

    def upload_section(self):
        st.title('Upload your data for modelling')
        file = st.file_uploader('Upload your Dataset here')

        if file:
            if len(file.getvalue()) > self.max_file_size:
                st.warning(f'File size exceeds the maximum allowed size of {self.max_file_size / (1024 * 1024)} MB.')
                filecache = st.cache(file)
            else:
                file_extension_handler = FileExtension()
                extension = file_extension_handler.get_file_extension(file.name)
                if extension:
                    st.info(f'File Extension: {extension}')

                    # Select reading method
                    method_options = ['CSV', 'XLS', 'XLSX', 'JSON', 'PARQEUT', 'FEATHER', 'H5', 'HDF5', 'MSGPACK', 'DTA', 'XML', 'ORC', 'SAS', 'SPSS', 'SQL TABLE',
                                      'SQL QUERY', 'SQL', 'GBQ', 'STATA', 'HTML', 'FWF']
                    method = st.selectbox('Which Pandas reading Tool Would you prefer', method_options)

                    # Display method-specific parameters
                    parameters = self.select_parameters(method)

                    # Multi-select for parameters
                    selected_parameters = st.multiselect('Select Parameters', parameters, default=parameters)

                    parameter_values = {}
                    for parameter in selected_parameters:
                        parameter_values[parameter] = st.text_input(f'Enter value for "{parameter}"',
                                                                    self.default_parameter.get(parameter, ''))

                    if st.button('Read file'):
                        # Read file using selected method and parameters
                        file_reader = FileReader(file, method, parameter_values)
                        session_state.df = file_reader.read_file()

                        if session_state.df is not None:
                            st.dataframe(session_state.df)
                            st.success(f"File successfully loaded using {method} method.")
                else:
                    st.warning('Unable to determine the file extension.')

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

if __name__ == '__main__':
    app = StreamlitApp()
    app.run()

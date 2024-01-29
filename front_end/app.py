# streamlit_app.py
import streamlit as st
from InputOutput.file_reader import FileReader
from InputOutput.fileextension import FileExtension
from InputOutput.paramters import *

class StreamlitApp:
    def __init__(self):
        self.max_file_size = 500 * 1024 * 1024
        self.default_parameter = {'sep': ',', 'header': 'infer', 'encoding': 'latin1'}

    def run(self):
        with st.sidebar:
            st.title('Dexter Labs')
            choice = st.radio('Navigation', ['Upload', 'Profiling', 'ML', 'Download'])
            st.info('This application allows you to build an automated ML pipeline ')

        if choice == 'Upload':
            self.upload_section()

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
                    method_options = ['CSV', 'XLS', 'XLSX', 'JSON', 'PARQEUT', 'FEATHER', 'H5', 'HDF5', 'MSGPACK', 'DTA', 'XML']
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
                        df = file_reader.read_file()

                        if df is not None:
                            st.dataframe(df)
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
        # Add more conditions for other reading methods
        else:
            return []

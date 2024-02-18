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

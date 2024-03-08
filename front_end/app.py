import streamlit as st
from InputOutput.file_reader import FileReader
from InputOutput.fileextension import FileExtension
from InputOutput.paramters import *
from InputOutput.data_cleaner import DataCleaner
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#from InputOutput.select_parameters import SelectParameter
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
            choice = st.radio('Navigation', ['Upload', 'Exploratory Data Analysis', 'Profiling', 'ML', 'Download'])
            st.info('This application allows you to build an automated ML pipeline ')

        if choice == 'Upload':
            self.upload_section()

        elif choice == 'Exploratory Data Analysis':
            if session_state.df is not None:
                self.exploratory_data_analysis_section(session_state.df)
            else:
                st.warning('Please upload a file first.')

        elif choice == 'Profiling':
           st.title("Data Preprocessing App")

            # Sidebar menu
        option = st.sidebar.selectbox("Select Preprocessing Method", 
                                      ["StandardScaler", 
                                       "MinMaxScaler", 
                                       "RobustScaler", 
                                       "Binarizer",
                                       "FunctionTransformer",
                                       "KBinsDiscrectizer",
                                       "KernelCenterer",
                                       "LabelBinerizer",
                                       "LabelEncoder",
                                       "MultiLabelBinarizer",
                                       "MaxAbsScaler",
                                       "Normalizer",
                                       "OneHotEncoding",
                                       "OrdinalEncoder",
                                       "PolynomialFeatures",
                                       "PowerTransformer",
                                       "QuantileTransformer",
                                       "SplineTransformer",
                                       "TargetEncoder",
                                       "add_dummy_feature",
                                       "binarize",
                                       "label_binarize",
                                       "Normizer",
                                       "maxabs_scale",
                                       "minmax",
                                       "normalize",
                                       "quantile_transform",
                                       "robust_scale",
                                       "scale",
                                       "power_transform"])

            # Display parameters based on selected method
        if option == "StandardScaler":
            Preprocessing.standard_scaler_params()
        elif option == "MinMaxScaler":
            Preprocessing.min_max_scaler_params()
        elif option == "RobustScaler":
            Preprocessing.robust_scaler_params()
        elif option == "Binarizer":
            Preprocessing.binarizer_params()
        elif option== "FunctionTransformer":
            Preprocessing.functiontransformer_params()

        elif option=="KBinsDiscretizer":
            Preprocessing.kbinsdiscretizer_params()

        elif option=="KernelCenterer":
            Preprocessing.kernelcenterer_params()
        elif option=="LabelBinerizer":
            Preprocessing.labelbinarizer_params()
        elif option=="LabelEncoder":
            Preprocessing.labelencoder_params()
        elif option=="MultiLabelBinarizer":
            Preprocessing.multilabelbinerizer_params()
        elif option=="MaxAbsScaler":
            Preprocessing.maxabsscaler_params()
        elif option=="Normalizer":
            Preprocessing.normalizer_params()
        elif option=="OneHotEncoding":
            Preprocessing.onehotencoder_params()
        elif option=="OrdinalEncoder":
            Preprocessing.ordinalencoder_params()
        elif option=="Normalizer":
            Preprocessing.normalizer_params()
        elif option=="PolynomialFeatures":
            Preprocessing.polynomialfeatures_params()
        elif option=="PowerTransformer":
            Preprocessing.powertransformer_params()
        elif option=="QuantileTransformer":
            Preprocessing.quantiletransformer_params()
        elif option=="SplineTransformer":
            Preprocessing.splinetransformer_params()
        elif option=="TargetEncoder":
            Preprocessing.targetencoder_params()
        elif option=="add_dummy_feature":
            Preprocessing.adddummyfeature_params()
        elif option=="binarize":
            Preprocessing.binerizer_lower_params()
        elif option=="label_binarize":
            Preprocessing.labelbinerize_lower_params()
        elif option=="Normalizer":
            Preprocessing.normalizer_params()
        elif option=="maxabs_scale":
            Preprocessing.maxabs_scale_params()
        elif option=="minmax_scale":
            Preprocessing.minmax_scale_params()
        elif option=="normalize":
            Preprocessing.normalize_params()
        elif option=="quantile_transform":
            Preprocessing.quantile_transform_params()
        elif option=="robust_scale":
            Preprocessing.robust_scale_params()
        elif option=="scale":
            Preprocessing.scale_params()
        elif option=="power_transform":
            Preprocessing.power_transform_params()
        

                
            

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
                            if st.button('Next'):
                                self.run()

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

    def exploratory_data_analysis_section(self, df):
        st.title('Exploratory Data Analysis')

        analyzer = DataAnalyzer(df)
        analyzer.run()

class DataAnalyzer:
    
    def __init__(self, df):
        self.df = df

    def run(self):
        st.title('Data Analysis Options')
        choice = st.radio('Select Analysis Type', ['Data Info', 'Data Cleaning'])  # Add more options as needed

        if choice == 'Data Info':
            self.data_info()
        elif choice == 'Data Cleaning':
            self.data_cleaning()

    def data_info(self):
        st.subheader('DataFrame Info')
        '''
        info_output=self.get_info_output()

        from io import StringIO
        import pandas as pd
        import matplotlib.pyplot as plt

     


        info_lines=info_output.split('\n')[3:-3]
        info_str='\n'.join(info_lines)
        print(info_str)
        info_file=StringIO(info_str)
        info_df=pd.read_csv(info_file,sep='\s\s+',engine='python')
        
        st.table(info_df)
        '''
        st.subheader('Categorical Columns')
        categorical_cols=self.get_categorical_columns()
        st.write(categorical_cols)
        for col in categorical_cols:
            st.subheader(f'Assessment of {col}')
            counts=self.df[col].value_counts()
            st.write(counts)


        st.subheader('Numerical Columns')
        numerical_cols=self.get_numerical_columns()
        st.write(numerical_cols)
        st.table(self.df.describe())
        
        st.subheader('Numerical Columns')
        selected_num_col = st.selectbox('Select Numerical Column', numerical_cols)
        
        # Plot histogram for the selected numerical column
        self.plot_histogram(selected_num_col)
        
        self.correlation()
        self.scatter_matrix()
        self.group_data()

    def get_info_output(self):
        import io
        import sys
        import pandas as pd
        stdout=sys.stdout
        sys.stdout=io.StringIO()

        self.df.info()

        info_output=sys.stdout.getvalue()

        sys.stdout=stdout
        print(info_output)

        return info_output
    def get_categorical_columns(self):
        import pandas as pd
        categorical_cols=self.df.select_dtypes(include=['object']).columns.tolist()
        return categorical_cols
    
    def get_numerical_columns(self):
        import pandas as pd
        numerical_cols=self.df.select_dtypes(include=['number']).columns.tolist()
        return numerical_cols
    def plot_histogram(self, selected_num_col=None, custom_pairs=False):
        if not custom_pairs:
            if selected_num_col:
                fig, ax = plt.subplots()
                ax.hist(self.df[selected_num_col], bins=20, color='skyblue', edgecolor='black')
                ax.set_xlabel('Value')
                ax.set_ylabel('Frequency')
                ax.set_title(f'Histogram of {selected_num_col}')
                ax.grid(True)
                st.pyplot(fig)
            else:
                st.warning('Please select a numerical column to plot histogram.')
        else:
            st.write("Select two numerical variables for plotting histograms.")
            available_cols = self.get_numerical_columns()
            selected_cols = st.multiselect('Select Variables', available_cols, key='custom_hist')

            if len(selected_cols) == 2:
                x_col, y_col = selected_cols
                fig, ax = plt.subplots()
                ax.hist(self.df[x_col], bins=20, color='skyblue', edgecolor='black', alpha=0.5, label=x_col)
                ax.hist(self.df[y_col], bins=20, color='salmon', edgecolor='black', alpha=0.5, label=y_col)
                ax.set_xlabel('Value')
                ax.set_ylabel('Frequency')
                ax.set_title(f'Histograms of {x_col} and {y_col}')
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)
            else:
                st.write("Select two categorical variables for plotting histograms.")
                available_cols = self.get_categorical_columns()
                selected_cols = st.multiselect('Select Variables', available_cols, key='custom_hist')

                if len(selected_cols) == 2:
                    x_col, y_col = selected_cols
                    fig, ax = plt.subplots()
                    ax.hist(self.df[x_col], bins=20, color='skyblue', edgecolor='black', alpha=0.5, label=x_col)
                    ax.hist(self.df[y_col], bins=20, color='salmon', edgecolor='black', alpha=0.5, label=y_col)
                    ax.set_xlabel('Value')
                    ax.set_ylabel('Frequency')
                    ax.set_title(f'Histograms of {x_col} and {y_col}')
                    ax.legend()
                    ax.grid(True)
                    st.pyplot(fig)

    def correlation(self):
        st.subheader('Correlation HeatMap')
        numerical_column=self.df.select_dtypes(include=['float64','int64']).columns
        selected_column=st.selectbox('Select Numerical Column', numerical_column, key='correlation_selectbox')  # Unique key added
        st.write(f'Correlation Matrix for column: {selected_column}')
        corr_matrix_plot=self.df[numerical_column].corr()
        corr_matrix=self.df[numerical_column].corr()[selected_column].sort_values(ascending=False)
        st.write(corr_matrix)
        st.subheader('Correlation HeatMap')
        fig,ax=plt.subplots()
        sns.heatmap(corr_matrix_plot,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5,ax=ax)
        st.pyplot(fig)
        return corr_matrix

    def scatter_matrix(self):
        st.subheader('Scatter Matrix')
        numerical_columns=self.df.select_dtypes(include=['float64','int64']).columns
        selected_columns=st.multiselect('Select Numerical Columns', numerical_columns)
        
        if selected_columns:
            scatter_matrix=sns.pairplot(self.df[selected_columns])
            st.pyplot(scatter_matrix)
    
    def group_data(self):
        st.subheader('Group your data here!')
        selected_columns=st.multiselect('Select Columns for Grouping',self.df.columns)
        if st.button('Group Data'):

            grouped_data=self.df.groupby(selected_columns)

            grouped_list=[]

            #Iterate over each group

            for group_key, group_data in grouped_data:
                # Create a dictionary for each group containing the group key and the data
                group_dict={'group_key':group_key}
                for column in self.df.columns:
                    if column not in selected_columns:
                        group_dict[column]=group_data[column].tolist()

                grouped_list.append(group_dict)
            # Convert the  list of ditionaries  to a Dataframe
            grouped_df_updated=pd.DataFrame(grouped_list)

            st.dataframe(grouped_df_updated)
        
        
    def data_cleaning(self):
        st.subheader('Data Cleaning Section', self.df.columns)

        # Add data cleaning operations here
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

class Preprocessing():
    def standard_scaler_params():
        st.subheader("StandardScaler Parameters")
    # Define parameters for StandardScaler here
    # Example: with_mean, with_std, etc.
    # Allow users to set the parameters using Streamlit widgets

    def min_max_scaler_params():
        st.subheader("MinMaxScaler Parameters")
        # Define parameters for MinMaxScaler here
        # Example: feature_range, etc.
        # Allow users to set the parameters using Streamlit widgets

    def robust_scaler_params():
        st.subheader("RobustScaler Parameters")
        # Define parameters for RobustScaler here
        # Example: quantile_range, etc.
        # Allow users to set the parameters using Streamlit widgets

    def binarizer_params():
        st.subheader("Binarizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def functiontransformer_params():
        st.subheader("Function Transformer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def kbinsdiscretizer_params():
        st.subheader("KBinsDiscretizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def kernelcenterer_params():
        st.subheader("Kernel Centerer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def labelbinarizer_params():
        st.subheader("Label Binarizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def labelencoder_params():
        st.subheader("Label Encoder Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def multilabelbinerizer_params():
        st.subheader("MultiLabelBinarizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def maxabsscaler_params():
        st.subheader("MaxAbsScaler Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    
    def normalizer_params():
        st.subheader("Normalizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def onehotencoder_params():
        st.subheader("OneHotEncoding Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets

    def ordinalencoder_params():
        st.subheader("OrdinalEncoder Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    
    def normalizer_params():
        st.subheader("Normalizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    
    def polynomialfeatures_params():
        st.subheader("PolynomialFeatures Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def powertransformer_params():
        st.subheader("PowerTransformer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def quantiletransformer_params():
        st.subheader("QuantileTransformer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def splinetransformer_params():
        st.subheader("SplineTransformer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def targetencoder_params():
        st.subheader("TargetEncoder Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def adddummyfeature_params():
        st.subheader("add_dummy_feature Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def binerizer_lower_params():
        st.subheader("binarize Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def labelbinerize_lower_params():
        st.subheader("label_binerize Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def normalizer_params():
        st.subheader("Normalizer Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def maxabs_scale_params():
        st.subheader("maxabs_scale Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def minmax_scale_params():
        st.subheader("minmax_scale Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def normalize_params():
        st.subheader("normalize Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def quantile_transform_params():
        st.subheader("quantile_transform Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def robust_scale_params():
        st.subheader("robust_scale Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def scale_params():
        st.subheader("scale Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    def power_transform_params():
        st.subheader("power_transform Parameters")
        # Define parameters for Binarizer here
        # Example: threshold, etc.
        # Allow users to set the parameters using Streamlit widgets
    
if __name__ == '__main__':
    app = StreamlitApp()
    app.run()

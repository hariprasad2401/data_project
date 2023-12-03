import os 
import sys 
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.Data_Project.exception import CustomException
from src.Data_Project.logger import logging
from src.Data_Project.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transform_object(self):

        '''
           This method is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ("scaler",StandardScaler())
            ])

            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("onehotencoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical Columns:{categorical_columns}")
            logging.info(f"Numerical Columns:{numerical_columns}")

            preprocessor=ColumnTransformer([
                ("NumPipeLine",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
            ])
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        train_df=pd.read_csv(train_path)
        test_df=pd.read_csv(test_path)

        logging.info("Reading the train and test file")

        preprocessing_obj=self.get_data_transform_object()

        target_column_name='math_score'
        numerical_columns=['reading_score','writing_score']

        # divinding train dataset into dependent and independent features

        input_train_data=train_df.drop(columns=[target_column_name],axis=1)
        target_train_data=train_df[target_column_name]

        # divinding test dataset into dependent and independent features

        input_test_data=test_df.drop(columns=[target_column_name],axis=1)
        target_test_data=test_df[target_column_name]

        logging.info("Applying Preprocessing on training and test dataframe")

        input_train_arr=preprocessing_obj.fit_transform(input_train_data)
        input_test_arr=preprocessing_obj.transform(input_test_data)


        train_arr=np.c_[input_train_arr,np.array(target_train_data)]
        test_arr=np.c_[input_test_arr,np.array(target_test_data)]

        logging.info(f"Saved preprocessing object")

        save_object(

            file_path=self.data_transformation_config.preprocessor_object_file_path,
            obj=preprocessing_obj
        )

        return(
            
            train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_object_file_path
        )



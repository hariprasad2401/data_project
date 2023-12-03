import os
import sys
from src.Data_Project.exception import CustomException
from src.Data_Project.logger import logging
import pandas as pd
from src.Data_Project.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def intiate_data_ingetion(self):
        try:
            # Reading the data from mysql code
            # df=read_sql_data()
            df=pd.read_csv(os.path.join('artifacts/notebook/Data','raw.csv'))

            logging.info("Reading the data from My SQL database completed")

            # After reading the data we will get raw dataframe,and we need to store it in Artifact
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
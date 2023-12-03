from src.Data_Project.logger import logging
from src.Data_Project.exception import CustomException
from src.Data_Project.Components.data_ingestion import DataIngestion
from src.Data_Project.Components.data_ingestion import DataIngestionConfig
from src.Data_Project.Components.data_transformation import DataTransformationConfig,DataTransformation
import sys
if __name__=="__main__":
    logging.info("The execution has started....")



    try:
        Data_ingestion=DataIngestion()
        train_data_path,test_data_path=Data_ingestion.intiate_data_ingetion()

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
    except Exception as e:
        logging.info('custom exception')
        raise CustomException(e,sys)



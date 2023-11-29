from src.Data_Project.logger import logging
from src.Data_Project.exception import CustomException
from src.Data_Project.Components.data_ingestion import DataIngestion
from src.Data_Project.Components.data_ingestion import DataIngestionConfig
import sys
if __name__=="__main__":
    logging.info("The execution has started....")



    try:
        Data_ingestion=DataIngestion()
        Data_ingestion.intiate_data_ingetion()
    except Exception as e:
        logging.info('custom exception')
        raise CustomException(e,sys)



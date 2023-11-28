import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name="Data_Project"

list_of_files=[
    # ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Components/data_ingestion.py",
    f"src/{project_name}/Components/data_transformation.py",
    f"src/{project_name}/Components/model_trainer.py",
    f"src/{project_name}/Pipeline/__init__.py",
    f"src/{project_name}/Pipeline/training_pipeline.py",
    f"src/{project_name}/Pipeline/predection_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "main.py",
    "Dockerfile"
]



for filePath in list_of_files:
    filePath=Path(filePath)
    filedir,filename=os.path.split(filePath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for file {filename}")
    
    if(not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as f:
            pass
        logging.info(f"creating empty file : {filePath}")
    else:
        logging.info(f"{filePath} is already exists")

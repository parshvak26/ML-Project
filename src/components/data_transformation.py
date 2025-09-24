import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OnehotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os 

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    
    def get_data_transformer_object(self):
        """
        This Function is responsible for data transformation
        """
        try:
            numerical_columns= ["writing_score", "reading_Score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
           ]
            
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy = "median")),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info("Numerical column Standard Scaling completed")
            cat_pipeline = Pipeline(

                steps = [("imputer", SimpleImputer(strategy = "most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler())

                ]
            )
            logging.info("Categorical column encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipline", num_pipeline, numerical_columns)
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
            
        

    
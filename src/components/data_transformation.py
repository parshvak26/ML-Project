import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipelinefrom 
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

    
    
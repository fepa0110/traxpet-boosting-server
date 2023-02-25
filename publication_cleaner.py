import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from dynamic_data import DynamicData
from services.publicacion_service import PublicacionService
            
def clean_up_posts():
    publicacion_service = PublicacionService()
    all_especies = publicacion_service.clean_up_posts()
    print("cleaner")
import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score
import random

def delete_random_values(path, pathNewFile):
    csv_file = pandas.read_csv(path)
    
    columns_size = len(csv_file.columns)
    rows_size = len(csv_file.index)

    csv_file.fillna("", inplace=True)

    for row in range(0, rows_size-1):
        random_column = random.randint(1, columns_size-1)
        random_number = random.randint(0, 4)

        for times in range(random_number):
            random_column = random.randint(1, columns_size-1)
            csv_file.iloc[row, random_column] = ""

    print(csv_file)

    csv_file.to_csv(pathNewFile, sep=",")

path = './data/perrosTrainAllComplete.csv'
pathNewFile = "./data/.csv"

delete_random_values(path,pathNewFile)

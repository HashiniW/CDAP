from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
# from flask import json
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import pickle
import json

from predictions.preprocess_model import PreprocessModel

class SvmModel():

    def get_prediction(self):
        loaded_model = pickle.load(open('kmeans_model.sav', 'rb'))

        data=[request.json]
        df = pd.DataFrame.from_dict(data, orient='columns')
        
        x = PreprocessModel().preprocess_features(df)
        # x_scaled = scale(x)
        # pca = PCA(n_components=2)
        # x_reduced = pca.fit_transform(x_scaled)
        # xcv = np.array([[ 0.398077  , -0.66858342]])
        numpy_matrix = x.as_matrix()
        # print(numpy_matrix)
        result = loaded_model.predict(numpy_matrix)
        description = 'default'
        if result == [1]:
            description = 'fraud'
        else: 
            description = 'non-fraud'
        return description


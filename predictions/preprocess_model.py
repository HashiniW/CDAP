import pandas as pd

class PreprocessModel():

    def preprocess_features(self,X):
        output = pd.DataFrame(index = X.index)
        for col, col_data in X.iteritems():
            if col_data.dtype == object:
                col_data = pd.get_dummies(col_data, prefix = col)
            output = output.join(col_data)
        return output
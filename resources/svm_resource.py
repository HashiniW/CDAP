from flask_restful import Resource
from predictions.svm_model import SvmModel

class Predict(Resource):
    def post(self):
        prediction = SvmModel().get_prediction()
        return prediction
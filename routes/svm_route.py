from flask import Flask
from flask import Blueprint
from flask_restful import Api

from resources.svm_resource import Predict

svm_blueprint = Blueprint('svm', __name__)
svm_blueprint_api = Api(svm_blueprint)

svm_blueprint_api.add_resource(Predict, '/svm', methods = ['POST'])
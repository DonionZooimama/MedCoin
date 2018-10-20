from flask import Flask, request
from flask_restful import Resource, Api
from patient_processing import *

app = Flask(__name__)
api = Api(app)


class UpdatePatient(Resource):
    def post(self):
        first = request.args.get('first_name')
        last = request.args.get('last_name')
        bloodtype = request.args.get('blood_type')
        allergies = request.args.get('allergies')
        ID = request.args.get('ID')

        return UpdatePatientData(ID, first, last, bloodtype, allergies)


class NewPatient(Resource):
    def post(self):
        first = request.args.get('first_name')
        last = request.args.get('last_name')
        bloodtype = request.args.get('blood_type')
        allergies = request.args.get('allergies')
        return NewPatientData(first, last, bloodtype, allergies)


class PatientInfo(Resource):
    def get(self):
        qrcode = request.args.get('qrcode')
        GetPatientData(qrcode)
        return GetPatientData(qrcode)


class Hello(Resource):
    def get(self):
        return "Hello"


api.add_resource(UpdatePatient, '/update')
api.add_resource(NewPatient, '/new')
api.add_resource(PatientInfo, '/info')
api.add_resource(Hello, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

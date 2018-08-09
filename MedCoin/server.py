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

        return UpdatePatientData(ID, first, last, blood_type, allergies)


class NewPatient(Resource):
    def post(self):
        first = request.args.get('first_name')
        last = request.args.get('last_name')
        bloodtype = request.args.get('blood_type')
        allergies = request.args.get('allergies')
        return NewPatientData(first, last, bloodtype, allergies)


class PatientInfo(Resource):
    def get(self):
        id = request.args.get('id')
        GetPatient(id)
        return GetPatient(id)


api.add_resource(UpdatePatient, '/update')
api.add_resource(NewPatient, '/new')
api.add_resource(PatientInfo, '/info')

if __name__ == '__main__':
    app.run(debug=True)

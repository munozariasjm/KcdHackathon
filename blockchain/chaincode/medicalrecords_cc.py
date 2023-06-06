import json
import shim
from shim import Chaincode

class MedicalRecord:

    def __init__(self, patient_id, medical_data):
        self.patient_id = patient_id
        self.medical_data = medical_data

class MedicalRecordChaincode(Chaincode):

    def __init__(self):
        self.records = {}

    def Init(self, stub):
        return shim.success()

    def Invoke(self, stub):
        function, args = stub.GetFunctionAndParameters()

        if function == 'addRecord':
            return self.addRecord(stub, args)
        elif function == 'getRecord':
            return self.getRecord(stub, args)
        else:
            return shim.error('Invalid function')

    def addRecord(self, stub, args):
        patient_id = args[0]
        medical_data = args[1]
        record = MedicalRecord(patient_id, medical_data)
        self.records[patient_id] = record
        return shim.success()

    def getRecord(self, stub, args):
        patient_id = args[0]
        if patient_id in self.records:
            return shim.success(self.records[patient_id])
        else:
            return shim.error('Record not found')

def main():
    Chaincode.Start(MedicalRecordChaincode())

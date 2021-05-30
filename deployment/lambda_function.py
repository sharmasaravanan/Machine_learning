import json
import pickle

fileName = "LR_API.model"
model = pickle.load(open(fileName,'rb'))

def lambda_handler(event, context):
    data = json.loads(event['body'])
    sales = model.predict([data['investAmount']])
    resp = {"sales": sales[0]}
    return resp

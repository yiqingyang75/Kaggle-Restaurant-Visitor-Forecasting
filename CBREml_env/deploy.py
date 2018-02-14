# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:59:49 2018

@author: yiqin
"""

from sklearn.externals import joblib
from boto.s3.key import Key
from boto.s3.connection import S3Connection
#from flask import Flask
#from flask import request
#from flask import json
import numpy as np
import json
#import pickle

BUCKET_NAME = "cbremachinelearning"
MODEL_FILE_NAME = "logi_model.sav"
MODEL_LOCAL_PATH = "C://Users//yiqin//Downloads//" + MODEL_FILE_NAME

#app = Flask(__name__)

#@app.route('/', methods=['POST'])
def load_model():
    print ('Loading model from S3')
    conn = S3Connection('AKIAJS7O3QPANEZQFM7A','RsRE1G/7BiKe7HDgOz6yHOFaFdIYKQ8b17vKA3Ic')
    bucket = conn.get_bucket(BUCKET_NAME)
    key_obj = Key(bucket) #
    key_obj.key = MODEL_FILE_NAME #the model file in s3
    
    key_obj.get_contents_to_filename(MODEL_LOCAL_PATH)
    loaded_model = joblib.load(MODEL_LOCAL_PATH)
    #loaded_model = pickle.load(open(MODEL_LOCAL_PATH, 'rb'))
    #loaded_model.predict([0.41290214, 0.89820289])
    return loaded_model

def predict(data):
    # Process your data, create a dataframe/vector and make your predictions
    print ('Making predictions')
    loaded_model = load_model()
    #data = [0.41290214, 0.89820289]
    pred = loaded_model.predict(data)
    return pred


def lambda_handler(event, context):
    data = json.loads(event['body'])
    input1 = data['input1']
    input2 = data['input2']
    #input1 = 0.41290214
    #input2 = 0.89820289
    clean_data = np.array([input1,input2]).reshape(1,2)
    pred = predict(clean_data)
    
    body = {
        "predicted": str(pred),
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response
    #clean_text = preprocess_text(raw_text)



  
"""
input1 = 0.41290214
input2 = 0.89820289
clean_data = np.array([input1,input2]).reshape(1,2)
pred = predict(clean_data)

body = {
    "predicted": str(pred),
}
response = {
    "statusCode": 200,
    "body": json.dumps(body)
}
print(response)
"""
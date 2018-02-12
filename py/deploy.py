# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:59:49 2018

@author: yiqin
"""

from sklearn.externals import joblib
from boto.s3.key import Key
from boto.s3.connection import S3Connection
from flask import Flask
from flask import request
from flask import json

BUCKET_NAME = "cbremachinelearning"
MODEL_FILE_NAME = "xgb01.model"
MODEL_LOCAL_PATH = "C://Users//yiqin//Downloads" + MODEL_FILE_NAME

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    payload = json.loads(request.get_data().decode('utf-8'))
    prediction = predict(payload['payload'])
    data = {}
    data['data'] = prediction[-1]
    return json.dumps(data)

def load_model():
    print ('Loading model from S3')

def predict(data):
    print ('Making predictions')
  

conn = S3Connection('AKIAJS7O3QPANEZQFM7A','RsRE1G/7BiKe7HDgOz6yHOFaFdIYKQ8b17vKA3Ic')
bucket = conn.get_bucket(BUCKET_NAME)
key_obj = Key(bucket)
key_obj.key = MODEL_FILE_NAME

contents = key_obj.get_contents_to_filename(MODEL_LOCAL_PATH)
#k.set_contents_from_filename('filename')
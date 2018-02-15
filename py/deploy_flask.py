# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:06:45 2018

@author: yiqin
"""

from flask import Flask
from flask import request
from flask import jsonify
import pickle
import numpy as np


MODEL_FILE_NAME = "logi_model.sav"
MODEL_LOCAL_PATH = "C://Users//yiqin//Downloads//" + MODEL_FILE_NAME

app = Flask(__name__)


@app.route('/model',methods=['POST','GET'])
def model():
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    loaded_model = pickle.load(open(MODEL_LOCAL_PATH, 'rb'))
    
    if request.json:
        data = request.get_json(force=True)
        input1 = data['input1']
        input2 = data['input2']
        clean_data = np.array([input1,input2]).reshape(1,2)
        pred = loaded_model.predict(clean_data)
    
        body = {
            "predicted": str(pred)
        }
        
    return jsonify(body)

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5050) 

#.\Scripts\activate  
##curl -H "Content-Type: application/json" -X POST -d '{"input1":0.41290214,"input2":0.89820289}' http://127.0.0.1:5050/model

"""
input1 = 0.41290214
input2 = 0.89820289
#clean_data=[input1,input2]
clean_data = np.array([input1,input2]).reshape(1,2)
pred = loaded_model.predict(clean_data)

body = {
    "predicted": str(pred)
}
response = {
    "statusCode": 200,
    "body": json.dumps(body)
}
print(response)
"""
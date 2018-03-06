# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:06:45 2018

@author: yiqin
"""
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb 
import boto3
from io import StringIO
import pandas as pd

def load_model(bucket_name, model_name):
    resource = boto3.resource('s3') #high-level object-oriented API
    my_bucket = resource.Bucket('cbremachinelearning') #bucket
    my_bucket.download_file(model_name,model_name)  ##download model from s3
    xgb_load = xgb.Booster({'nthread':4}) #init model
    xgb_load.load_model(model_name)  # load model
    return xgb_load

def load_csv(bucket_name,csv_name):
    #load data from s3 
    client = boto3.client('s3') #low-level functional API                
    obj = client.get_object(Bucket=bucket_name, Key=csv_name) 
    body = obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_string))
    return df
          
app = Flask(__name__)
@app.route('/visit',methods=['POST','GET'])
def visit():
    model_name = "xgb02.model"
    bucket_name = 'cbremachinelearning'
    csv_name = 'Xtest_book.csv'
    
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    
    if request.json:
        data = request.get_json(force=True)
        id_date = data['id_date']
        #id_date = "air_00a91d42b08b08d9_2017-04-23,air_00a91d42b08b08d9_2017-04-24" 
        id_date = id_date.split(',')
        
        model = load_model(bucket_name,model_name)
        df = load_csv(bucket_name,csv_name)

        df_test = df[df["id"].isin(id_date)].copy()
        df_test.drop("id",axis = 1, inplace = True) 
        
        pred = model.predict(xgb.DMatrix(df_test))
        pred = [int(visit) for visit in pred]
        result = dict(zip(id_date,pred))   
    
        body = {
            "predicted visit": str(result)
        }
        
    return jsonify(body)

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5050) 

#.\Scripts\activate  
##curl -H "Content-Type: application/json" -X POST -d '{"id_date": "air_00a91d42b08b08d9_2017-04-23,air_00a91d42b08b08d9_2017-04-24"}' http://127.0.0.1:5050/visit

"""
model = load_model(bucket_name,model_name)
df = load_csv(bucket_name,csv_name)
id_date = "air_00a91d42b08b08d9_2017-04-23,air_00a91d42b08b08d9_2017-04-24" 
id_date = id_date.split(',')
df_test = df[df["id"].isin(id_date)].copy()
df_test.drop("id",axis = 1, inplace = True) 
pred = model.predict(xgb.DMatrix(df_test))
pred = [int(visit) for visit in pred]
result = dict(zip(id_date,pred))       
result
"""

# Restaurant Visitor Prediction
This is a machine learning project to kaggle competiton [Recruit Restaurant Visitor Forecasting](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting/data).

A comprehensive [Python Jupyter Notebook](https://github.com/yiqingyang75/Kaggle-Restaurant-Visitor-Forecasting/blob/master/py/Recruit_Restaurant_Visitor_Forecasting.ipynb) goes through EDA, Feature Engineering, Data Processing, and Model Building, Grid Search, Cross Validation, and Model Selection.

The final selected [Xgboost Model](https://github.com/yiqingyang75/Kaggle-Restaurant-Visitor-Forecasting/blob/master/model/xgb02.model) is  being saved to local and uploaded in AWS S3.

## A simple HTTP POST endpoint that returns predicted visitors.
When you send a properly formatted string (storeid_date) in the body of a POST to this endpoint, it will reply with JSON containing the predicted visitors for that specific store at specific date.

### Serverless Deploy
[Serverless](https://serverless.com/) is a toolkit for deploying and operating serverless architectures. Focus on application, not infrastructure. In this project, Serverless is being connected with [AWS Lambda](https://aws.amazon.com/lambda).
#### Usage
```bash
$ curl -H "Content-Type: application/json" -X POST -d '{"id_date":"air_00a91d42b08b08d9_2017-04-23"}' https://vnnxb5ok7i.execute-api.us-east-1.amazonaws.com/dev/visit
```
#### Setup
If you are interested in how to deploy it using Serverless, refer to [serverless docs](https://serverless.com/framework/docs/getting-started/) and [our specific example](https://github.com/yiqingyang75/Kaggle-Restaurant-Visitor-Forecasting/tree/master/cbrelambda).
### Flask Deploy
[Flask](http://flask.pocoo.org/) is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. In this project, a localhost is being built to host the endpoint.
#### Clone this repo
```bash
$ git clone https://github.com/yiqingyang75/Kaggle-Restaurant-Visitor-Forecasting.git
```
#### Run deploy_flask_cbre.py
```bash
$ python py/deploy_flask_cbre.py
```
#### Usage
```bash
curl -H "Content-Type: application/json" -X POST -d '{"id_date": "air_00a91d42b08b08d9_2017-04-23"}' http://127.0.0.1:5050/visit
```

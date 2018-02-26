import json
#path = "C://Users//yiqin//Dropbox//UCD//18Winter//452 Machine Learning//Kaggle-Restaurant-Visitor-Forecasting//py//titanic_submission_cv.csv"

def load_dict(path):
    with open(path, 'r') as f:
        mydict = {}
        for line in f:
                words = line.split(',')
                mydict[words[0]]=words[1].strip()
    return mydict

    
def lambda_handler(event,context):
    data = json.loads(event['body'])
    index = data['index']
    path = "C://Users//yiqin//Dropbox//UCD//18Winter//452 Machine Learning//Kaggle-Restaurant-Visitor-Forecasting//py//titanic_submission_cv.csv"
    with open(path, 'r') as f:
        mydict = {}
        for line in f:
                words = line.split(',')
                mydict[words[0]]=words[1].strip()
    #mydict = load_dict(path)
    pred = mydict[index]
    
    body = {
        "predicted": str(pred),
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response



def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
import boto3
import csv


def lambda_handler(event,context):
    data = json.loads(event["body"])
    id_date = data['id_date']
    #id_date = event['id_date']
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket("cbremachinelearning")
    files = list(bucket.objects.filter(Prefix = "xgb2.csv"))
    csvfile_obj = files[0].get()
    lines = csvfile_obj["Body"].read().decode('utf-8').splitlines()
    csv_dic = csv.DictReader(lines)
    record = {}
    for row in csv.DictReader(lines):
        line = dict(row)
        key = line["id"]
        record[key] = line
    
    pred = record[id_date]

    body = {
        "predicted": str(pred),
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response



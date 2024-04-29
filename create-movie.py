import json
import boto3

TABLE_NAME = 'ethomas-p2-dev'

def lambda_handler(event, context):
    db = boto3.client('dynamodb')

    body = json.loads(event['body'])

    db.put_item(
        TableName=TABLE_NAME,
        Item={
            "movieId": {
                "S": body['id']
            },
            "director": {
                "S": body['director']
            },
            "title": {
                "S": body['title']
            },
            "description": {
                "S": body['description']
            },
            "contentRating": {
                "S": body['contentRating']
            },
            "releaseYear": {
                "N": body['releaseYear']
            },
            "runTime": {
                "S": body['runTime']
            },
            "writers": {
                "L": [
                {
                    "S": body['writers'][0]
                },
                {
                    "S": body['writers'][1] if len(body['writers']) > 2 else '' 
                },
                {
                    "S": body['writers'][2] if len(body['writers']) > 3 else ''
                }
                ]
            },
            "actors": {
                "L": [
                {
                    "S": body['actors'][0]
                },
                {
                    "S": body['actors'][1] if len(body['actors']) > 2 else ''
                },
                {
                    "S": body['actors'][2] if len(body['actors']) > 3 else ''
                }
                ]
            },
            "imageURL": {
                "S": body['imageURL']
            }
    })
    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Credentials': True,
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*',
            'Content-Type': 'application/json'
        }
    }



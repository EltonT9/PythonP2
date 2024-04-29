import boto3
import json

def lambda_handler(event, context):
    if 'movieId' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('movieId is required')
        }

    # Initialize DynamoDB client
    dynamodb = boto3.client('dynamodb')

    movie_id = json.loads(event['body'])['movieId']  # Extract movieId from the event

    # Table name
    table_name = 'ethomas-p2-dev'

    # Delete table entry
    try:
        dynamodb.delete_item(
            TableName=table_name,
            Key={
                'movieId': {'S': movie_id}
            }
        )

        return {
            'statusCode': 201,
            'headers': {
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
                "X-Requested-With": "*"
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error deleting movie: {str(e)}')
        }

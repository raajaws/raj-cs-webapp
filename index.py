import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World Rajesh Singh 04/28/2032 1:17 PM',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

import json
import boto3

from sellers_api.settings import *

sqs = boto3.resource(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def send_message_sqs(instance): 
    message = {
        "subject": instance.group_name,
        "participants":instance.contacts_group
    }
    
    queue = sqs.get_queue_by_name(QueueName=SQS_SELLERS_CREATE_GROUP)

    response = queue.send_message(MessageBody=json.dumps(message), MessageAttributes={
            'Author': {
                'StringValue': 'Sellers_api',
                'DataType': 'String'
            }
        }
    )
    print("Send_message_queue")

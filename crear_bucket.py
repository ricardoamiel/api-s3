import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    
    # Proceso    
    s3 = boto3.client('s3')
    response = s3.create_bucket(
        Bucket=nombre_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'
        }
    )

    return {
        'statusCode': 200,
        'message': f'Bucket {nombre_bucket} creado exitosamente',
        'response': response
    }

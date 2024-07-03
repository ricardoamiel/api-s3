import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    region = 'us-east-1'
    
    # Proceso    
    s3 = boto3.client('s3', region_name=region)
    if region == 'us-east-1':
        response = s3.create_bucket(Bucket=nombre_bucket)
    else:
        response = s3.create_bucket(
            Bucket=nombre_bucket,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )

    return {
        'statusCode': 200,
        'message': f'Bucket {nombre_bucket} creado exitosamente',
        'response': response
    }

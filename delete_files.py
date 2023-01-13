import boto3

client = boto3.client(
    "s3",
    aws_access_key_id='key_acess',
    aws_secret_access_key='secret_key'
)
bucket_name = 'bucket_name'
paginator = client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket_name, Prefix='caminho_dentro_do_bucket/')


for page in pages:
    for key in page['Contents']:
        try:
            client.delete_object(
                Bucket=bucket_name,
                Key=key['Key']
            )
        except:
            print(key['Key'])
            pass
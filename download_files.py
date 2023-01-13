import boto3
from pathlib import Path

client = boto3.client(
    "s3",
    aws_access_key_id='key_acess',
    aws_secret_access_key='secret_key'
)

bucket_name = 'bucket_name'
paginator = client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket_name, Prefix='caminho_dentro_do_bucket')

for page in pages:

    for key in page['Contents']:

        try:

            file_name_filtred = key['Key'].replace('retirar_caminho_S3', '')
            download_file_path = Path(f'caminho_local_download/{file_name_filtred}')
            client.download_file(
                Bucket=bucket_name,
                Key = key['Key'],
                Filename = download_file_path,
            )
        except:
            pass
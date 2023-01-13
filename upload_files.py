import boto3
import os
from pathlib import Path

session = boto3.resource("s3",
    aws_access_key_id='key_acess',
    aws_secret_access_key='secret_key',
    region_name='region'
    )

for root, _, arquivo in os.walk('caminho_local_para_upload'):

    for file in arquivo:

        try:
            file_path = Path(f'caminho_local_para_upload{file}')
            session.meta.client.upload_file(file_path, 'bucket_name', f"caminho_destino_S3/{file}")

        except:
            file_path = Path(f'caminho_local_para_upload/{file}')
            session.meta.client.upload_file(file_path, 'bucket_name', f"caminho_destino_S3/{file}")
            pass
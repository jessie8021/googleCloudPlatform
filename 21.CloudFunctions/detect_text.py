from google.cloud import vision
from google.cloud import bigquery


def detect_text(event, context):
    vision_client = vision.ImageAnnotatorClient()
    bigquery_client = bigquery.Client()

    bucket_uri = 'gs://{bucket}/{file}'.format(bucket=event['bucket'], file=event['name'])
    response = vision_client.text_detection({'source': {'image_uri': bucket_uri}}).full_text_annotation.text
    query = """insert into `able-handbook-318205.functions.ocr` (image_path, detect_text) values ('{bucket}', '''{text}''');""".format(bucket=bucket_uri, text=response)
    bigquery_client.query(query)


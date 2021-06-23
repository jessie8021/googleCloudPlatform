import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('logo.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.logo_detection(image = image)
logos = response.logo_annotations
for logo in logos:
    print(logo)
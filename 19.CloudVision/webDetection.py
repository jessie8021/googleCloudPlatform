import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('web.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.web_detection(image = image)

print(response)
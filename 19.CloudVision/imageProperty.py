import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('property.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.image_properties(image = image)
print(response)
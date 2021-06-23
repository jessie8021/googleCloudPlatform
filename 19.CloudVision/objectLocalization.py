import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('object.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.object_localization(image=image)
objects = response.localized_object_annotations

for object in objects:
    print(object)

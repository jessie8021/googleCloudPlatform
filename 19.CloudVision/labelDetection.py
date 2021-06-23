import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('label.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.label_detection(image = image)
labels = response.label_annotations

for label in labels:
    print(label)
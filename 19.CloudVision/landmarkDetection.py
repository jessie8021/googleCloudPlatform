import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('landmark.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.landmark_detection(image=image)
landmarks = response.landmark_annotations

for landmark in landmarks:
    print(landmark)


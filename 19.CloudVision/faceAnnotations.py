import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('face.png', 'rb').read()
image = vision.types.Image(content = content)
response = client.face_detection(image=image)
faces = response.face_annotations

for face in faces :
    print(face)

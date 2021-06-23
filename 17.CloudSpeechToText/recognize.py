import io
from google.cloud import speech

# Speech to Text API를 위한 인스턴스 생성
client = speech.SpeechClient()
audio_file = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'
# 오디오 파일 전달
audio = speech.RecognitionAudio(uri = audio_file)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, #인코딩 LINEAR16
    sample_rate_hertz=16000, # 16000헤르츠
    language_code="en-US", # 영어 설정
)

response = client.recognize(config = config, audio = audio)
print(response)
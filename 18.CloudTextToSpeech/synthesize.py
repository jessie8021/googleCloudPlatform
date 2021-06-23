from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
input_text = texttospeech.SynthesisInput(text = "Hello World")
voice = texttospeech.VoiceSelectionParams(
    language_code = 'en-US',
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE # Voice type 설정
)

# mp3 생성을 위한 설정
audio_config = texttospeech.AudioConfig(
    audio_encoding = texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input = input_text, voice = voice, audio_config = audio_config
)

with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
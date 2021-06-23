from google.cloud import translate

client = translate.TranslationServiceClient()
parent = "projects/mysecont/locations/global"

response = client.translate_text(
    request={
        "parent": parent,
        "contents": "Cloud Translation API에 번역을 요청하면 기본적으로 인공신경망 기계 번역(NMT) 모델을 사용하여 덱스트가 번역됩니다.",
        "mime_type": "text/plain",  # mime types: text/plain, text/html
        "source_language_code": "ko",
        "target_language_code": "en",
    }
)
for translation in response.translations:
    print("Translated text: {}".format(translation.translated_text))

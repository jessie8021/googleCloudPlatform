from google.cloud import translate

client = translate.TranslationServiceClient()
parent = "projects/mysecont/locations/global"

response = client.translate_text(
    request={
        "parent": parent,
        "contents": "사과",
        "mime_type": "text/plain",  # mime types: text/plain, text/html
        "source_language_code": "ko",
        "target_language_code": "ja",
    }
)
for translation in response.translations:
    print("Translated text: {}".format(translation.translated_text))

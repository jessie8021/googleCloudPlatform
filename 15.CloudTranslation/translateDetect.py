from google.cloud import translate
client = translate.TranslationServiceClient()
parent = "projects/mysecont/locations/global"

response = client.detect_language(
    content="Hello, world!",
    parent=parent,
    mime_type="text/plain",  # mime types: text/plain, text/html
)

for language in response.languages:
    print("Language code: {}".format(language.language_code))
    print("Confidence: {}".format(language.confidence))

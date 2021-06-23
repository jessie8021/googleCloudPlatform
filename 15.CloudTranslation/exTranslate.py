from google.cloud import translate

client = translate.TranslationServiceClient()
parent = "projects/mysecont"

response = client.get_supported_languages(parent=parent)


print("Supported Languages:")

for language in response.languages:
    print("Language Code: {}".format(language.language_code))

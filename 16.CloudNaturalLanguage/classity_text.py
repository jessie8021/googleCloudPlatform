from google.cloud import language_v1
from google.cloud.language_v1 import enums

client = language_v1.LanguageServiceClient()
content = 'When I was young, there was an samazing publication called The Wole Earth Catalog, Which ' \
          'was one of the bibles og my generation. It was created by a fellow named Stewart Brand not far ' \
          'from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late ' \
          '1960s, before personal computers and desktop publishing, so it was all made with typewriters, scissors ' \
          'and Polaroid cameras. It was sort of like Google in paperback form, 35 years before Google cate along: ' \
          'It was idealistic, and overflowing with neat tools and great notions.'
type_ = enums.Document.Type.PLAIN_TEXT
gcs_content_url = 'gs://dataflow-sample-test/UptownFunk.txt'
language = 'en'

# content 카테고리 분석
document = {'content' : content, 'type' : type_, 'language' : language}

# gcs 카테고리 분석
#document = {'gcs_content_uri' : gcs_content_url, 'type' : type_, 'language' : language}
encoding_type = enums.EncodingType.UTF8

response = client.classify_text(document)

print(response)

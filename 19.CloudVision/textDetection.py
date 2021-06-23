import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
content = io.open('document.png', 'rb').read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image)

for page in response.full_text_annotation.pages:
    for block in page.blocks:
        print('\nBlock confidence: {}\n'.format(block.confidence))
        for paragraph in block.paragraphs:
            print('Paragraph confidence: {}'.format(paragraph.confidence))
            for word in paragraph.words:
                word_text = ' '.join([symbol.text for symbol in word.symbols])
                print('Word text: {}(confidence:{})'.format(word_text, word.confidence))
                for symbol in word.symbols:
                    print('\tSymbol: {} (confidence: {})'.format(symbol.text, symbol.confidence))


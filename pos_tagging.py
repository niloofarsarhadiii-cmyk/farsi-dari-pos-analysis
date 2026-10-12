import stanza

# Download the Persian model (only needed once)
stanza.download('fa')

# Load the tagger
nlp = stanza.Pipeline('fa', processors='tokenize,pos')

# Replace this with a real Dari sentence
doc = nlp("your Dari sentence here")

for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.upos)

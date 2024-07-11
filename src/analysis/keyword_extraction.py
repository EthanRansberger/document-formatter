import spacy

def extract_key_phrases(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

# Import Spacy
import spacy
from spacy import displacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("models")

# Process whole documents
text = ("which of the designs have instrument CMIS assigned to orbit LEO 600 polar NA which instruments from UCL-Geomatics do we currently use to measure Turbulence")
doc = nlp(text)

# Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for index, entity in enumerate(doc.ents):
    print("{}: '{}' corresponds to {}".format(index + 1, entity.text, entity.label_))


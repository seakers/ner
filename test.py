# Import Spacy
import spacy
from spacy import displacy
from sys import argv

if __name__ == "__main__":
    # Run test.py "model_path" "text_to_evaluate- in the termina"
    model = argv[1]
    text = argv[2]
    print("\nModel: {}\nText: {}\n".format(model, text))
    nlp = spacy.load(model)
    doc = nlp(text)
    # Analyze syntax
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])


    # Find named entities, phrases and concepts
    for index, entity in enumerate(doc.ents):
        print("{}: '{}' corresponds to {}".format(index + 1, entity.text, entity.label_))
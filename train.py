import random
import json
import os
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding

MODELS_DIR = "models"
DATASET_PATH = "data/EOSS_sentences"

def get_train_set(threshold=500, path=DATASET_PATH):
    paths_list = [path + "/" + f_path for f_path in os.listdir(path)]
    train_data = []
    for file_path in paths_list:
        with open(file_path, "r") as data_file:
            train_data += json.load(data_file)[:threshold]
    return train_data

def main(model=None, new_model_name="daphne_entities_5", models_dir=MODELS_DIR, n_iter=100):
    """Obtain Training Data"""
    TRAIN_DATA = get_train_set()
    """Set up the pipeline and entity recognizer, and train the new entity."""
    random.seed(0)
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    ner.add_label("INSTRUMENT")  # add new entity label to entity recognizer
    ner.add_label("ORBIT")  # add new entity label to entity recognizer
    ner.add_label("DESIGN_ID")  # add new entity label to entity recognizer
    ner.add_label("INSTRUMENT_PARAMETER")  # add new entity label to entity recognizer
    ner.add_label("MEASUREMENT")  # add new entity label to entity recognizer
    ner.add_label("MISSION")  # add new entity label to entity recognizer
    ner.add_label("OBJECTIVE")  # add new entity label to entity recognizer
    ner.add_label("ORBIT")  # add new entity label to entity recognizer
    ner.add_label("SPACE_AGENCY")  # add new entity label to entity recognizer
    ner.add_label("STAKEHOLDER")  # add new entity label to entity recognizer
    ner.add_label("SUBOBJECTIVE")  # add new entity label to entity recognizer
    ner.add_label("TECHNOLOGY")  # add new entity label to entity recognizer
    ner.add_label("NOT_PARTIAL_FULL")  # add new entity label to entity recognizer
    ner.add_label("NUMBER")  # add new entity label to entity recognizer
    ner.add_label("YEAR")  # add new entity label to entity recognizer


    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.1, losses=losses)
            print("Losses", losses)

    # save model to output directory
    output_dir = models_dir + "/" + new_model_name
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)


if __name__ == "__main__":
    main()
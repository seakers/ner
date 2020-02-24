# Named Entity Recognition
This model will be trained to recognize these entities:
- INSTRUMENT_PARAMETER
- INSTRUMENT
- MEASUREMENT
- MISSION
- OBJECTIVE
- ORBIT
- SPACE_AGENCY
- STAKEHOLDER
- SUB_OBJECTIVE
- TECHNOLOGY
- AGENT
- NUMBER
- NOT_PARTIAL_FULL
- YEAR

For that purpose, a combination of available commands and their possible parameters was made to create enough data to train the model on this new entities. The commands and their available parameters can be find inside the `data` directory.


## Data Processing for Training
Some of the data had to be parsed a bit first to fit the format that a normal human would use to execute commands. Here is a table with the main format alternatives that have been considered.

|  Parameter | Parsing  |
|---|---|
| instrument_parameters  |  remove -, # and () |
|  orbits |  consider spaces instead of hyphen as well |
|  measurements (eng) |  remove indexing and split by commas |
|  measurements (hist) |  remove (), add acronyms, maybe simplify|
|  missions |  maybe replace hyphen for space |

it is important to keep in mind that although parsing is done to modify some of the parameters from the list, this is just with the purpose of creating more human like expressions to train the model. The database will still need the original term in order to make a query.

## Design Decisions
- Crossing every possible command with every possible parameter. Choosing a train and test set from it.

## PP (Possible Problems)
- Presence or absence of hash symbol could affect the ability of the model to recognize an entity. // Should not matter now as data has been pre-processed.
- Commands with multiple parameters should have some kind of logic exclusion (ex: bla bla from 2019 to 2002 should not be allowed). // Update: It actually should be alloed.
- More sentences without parameters are needed to train!

## To Do
- ~~May be good to also train it on responses~~ (not really sure)
- ~~Improve design id recognition~~ (improved by considering lower case and shorter numbers)
- Make it possible to run everything from the terminal
- May be assigning more parameters that correspond to certain commands.

## Explanation of every function

#### Functions from `sentence_creation.py`
|  Function | Purpose  |
|---|---|
| `get_commands()`  | Given a commands file from `EOSS` dir, retrieves both the parameters used for those commands and the commands themselves.  |
| `get_command_placeholders_positions()` | Returns the start and end indexes of every parameter placeholder and the placeholder name ex: year1.  |
| `get_param_paths()` | Given a list of parameters ("year1 year") and a parameters dir, returns a path for where they are.|
| `sentence_combinations()` | Given a command, it's placeholders and the parameters it uses, it retrieves every possible sentence created by the combination of them.|
| `entities_positions()` | Returns the positions of every entity after beeing replaced into the sentence. |
| `obtain_parameters()` | This function opens the parameters files and retrieves them as a dictionary `<param_name>:<list_of_params>`|
| `produce_sentences()` | Main function that reads every `EOSS` file and turns it into a `.json` file at `EOSS_sentences`. Every sentence is marked with their parameters respective position.|

#### Functions from `train.py`
|  Function | Purpose  |
|---|---|
| `get_train_set()`  | Gets the minimum between the amount of sentences inside every dataset file and a given threshold to build a training set. Returns the training set. |
| `main()`  | Trains the model. |

## Observations
- Testing the model on sentences that the model hasn't been trained on doesn't return good predictions unless a "clue" is given. For example it wont be able to recognize the design id in "how can d309 be improved" but it will if the sentence is changed to "how can design d309 be improved".
- NOT_PARTIAL_FULL seems not to work with fractions.

## If you want to change the list of parameters or commands
1. Change the file you want to change.
2. Then run `python3 sentence_creation.py`
3. Run `python3 train.py` to train the model with the updated parameters
4. Give it a try with `python3 test.py <path_to_model_to_be_used> <text_to_be_tested>`
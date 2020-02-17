# Named Entity Recognition
This model will be trained to recognize:
- INSTRUMENT_PARAMETER
- INSTRUMENT
- MEASUREMENT
- MISSION
- OBJECTIVE
- ORBIT
- SPACE_AGENCY
- STAKEHOLDER
- SUB-OBJECTIVE (not sure yet) (included)
- TECHNOLOGY
- AGENT (not sure yet) (not included)

and will take advantage of the previously trained model entities: 
- CARDINAL
- PERCENT
- DATE (year? not sure yet)

For that purpose, a combination of available commands and their possible parameters will be made to create enough data to train the model on this new entities. The commands and their available parameters can be find inside the `data` directory.


## Data Processing for Training
Some of the data has to be parsed a bit first to fit the format that a normal human would use to execute commands.

|  Parameter | Parsing  |
|---|---|
| instrument_parameters  |  remove -, # and () |
|  measurements (eng) |  remove indexing and split by commas |
|  orbits |  consider spaces instead of hyphen as well |
|  measurements (hist) |  remove (), add acronyms, maybe simplify|
|  missions |  maybe replace hyphen for space |

it is important to keep in mind that although parsing is done to modify some of the parameters from the list, this is just with the purpose of creating more human like expressions to train the model. The database will still need the original term in order to make a query.

## Design Decisions
- Crossing every possible command with every possible parameter. Choosing a train, val and test set from it.

## PP (Possible Problems)
- Presence or absence of hash symbol could affect the ability of the model to recognize an entity.
- Commands with multiple parameters should have some kind of logic exclusion (ex: bla bla from 2019 to 2002 should not be allowed).
- May be assigning more parameters that correspond to certain commands.

## To Do
- Change 'vassar_something' for 'something' when it corresponds
- May be good to also train it on responses

## Explanation of every function

#### Functions from `sentence_creation.py`
|  Function | Purpose  |
|---|---|
| `get_commands()`  | Given a commands file from `EOSS` dir, retrieves both the parameters used for those commands and the commands themselves.  |
| `get_command_placeholders_positions()` | Returns the start and end indexes of every parameter placeholder and the placeholder name ex: year1.  |
| `get_param_paths()` | Given a list of parameters ("year1 year") and a parameters dir, returns a path for where they are.|
| `sentence_combinations()` | Given a command, it's placeholders and the parameters it uses, it retrieves every possible sentence created by the combination of them.|
| `entities_positions()` | Returns the positions of every entity after beeing replaced into the sentence. |
| `produce_sentences()` | Main function that reads every `EOSS` file and turns it into a `.json` file at `EOSS_sentences`. Every sentence is marked with their parameters respective position.|
| `obtain_parameters()` | This function opens the parameters files and retrieves them as a dictionary `<param_name>:<list_of_params>`|
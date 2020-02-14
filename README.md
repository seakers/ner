# Named Entity Recognition
This model will be trained to recognize:
- INSTRUMENT
- INSTRUMENT_PARAMETER
- MEASUREMENT
- OBJECTIVE
- SUB-OBJECTIVE (not sure yet)
- ORBIT
- STAKEHOLDER
- MISSION
- SPACE_AGENCY
- TECHNOLOGY
- AGENT (not sure yet)

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

## To Do
- Change 'vassar_something' for 'something' when it corresponds
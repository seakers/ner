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
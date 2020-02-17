"""
---------------------------------------------- ABOUT THIS CODE--------------+
This script is used to create sentences to train spaCy's NER model
on new entities based on the information already available for DAPHNE VA. 
The idea is to generate every possible command that exists so far and 
take a subset of it to train the model.

The decision of creating small functions to solve every problem is so 
that they can be easily modified by someone else in the future.
----------------------------------------------------------------------------+
"""

import re
import os
import json
import itertools
import random

EOSS_COMMANDS_PATH = "data/EOSS"
EOSS_SENTENCES_PATH = "data/EOSS_sentences"
PARAMS_PATH = "data/processed_parameters"


# Retrieves a list of commands and the parameters they may have
def get_commands(commands_file_path):
    commands_info = { "parameters": [], "commands": [] } 
    with open(commands_file_path, "r") as command_file:
        regex = re.compile("--\n")
        file_sections = regex.split(command_file.read())
        commands_info["parameters"] = file_sections[1].strip("\n").split("\n")
        commands_info["commands"] = file_sections[-1].strip("\n").split("\n")
    return commands_info

# Returns the start and end indexes of every parameter placeholder and the placeholder name ex: year1
def get_command_placeholders_positions(command):
    regex = re.compile(r"\${([A-z0-9]+)}")
    param_spaces = []
    for coincidence in regex.finditer(command):
        start = coincidence.start()
        end = start + len(coincidence.group()) - 1
        parameter = coincidence.group().strip("${").strip("}")
        param_spaces.append((start, end, parameter))
    return param_spaces

# Given a list of parameters ("year1 year") returns a path for where they are
def get_param_path(parameters, params_directory_path=PARAMS_PATH):
    params_names = set([param.split(" ")[1] for param in parameters])
    params_paths = {param_name: params_directory_path + "/" + param_name for param_name in params_names}
    return params_paths

def sentence_combinations(command, command_param_placeholders, parameters):
    """
    TODO: 
        - retrive corresponding lists of parameters
        - put them in a sorted list, considering how they appear on the command
        - create every possible combination of them
        - turn every combination into a sentence and append it to a file
    """
    all_parameters = obtain_parameters()
    sorted_parameters = []
    for element in command_param_placeholders:
        sorted_parameters.append(all_parameters[parameters[element[2]]])
    every_possible_combination_of_parameters = list(itertools.product(*sorted_parameters))
    params_per_command = len(list(every_possible_combination_of_parameters[0]))
    every_possible_sentence = []
    for possible_combination_tuple in every_possible_combination_of_parameters:
        possible_combination = list(possible_combination_tuple)
        new_sentence = command
        for p in range(params_per_command):
            if "year" in command_param_placeholders[p][2]:
                new_year = str(random.randint(1950, 2020))
                possible_combination[p] = new_year
                new_sentence = new_sentence.replace("${" + command_param_placeholders[p][2] + "}", new_year)
            else:
                new_sentence = new_sentence.replace("${" + command_param_placeholders[p][2] + "}", possible_combination[p])     
        every_possible_sentence.append((new_sentence, {"entities": entities_positions(new_sentence, possible_combination, parameters, [place_holder[-1] for place_holder in command_param_placeholders])}))
    return every_possible_sentence

def entities_positions(sentence, parameters, parameters_mapping, entities):
    positions = []
    start = 0
    for indx, parameter in  enumerate(parameters):
        start = sentence.find(parameter, start)
        end = start + len(parameter) - 1
        entity = parameters_mapping[entities[indx]].upper()
        positions.append((start, end, entity))
        start = end
    return positions

def produce_sentences(path=EOSS_COMMANDS_PATH):
    paths_list = [path + "/" + f_path for f_path in os.listdir(path)]
    for file_path in paths_list:
        print(file_path)
        commands_info = get_commands(file_path)
        try:
            parameters = {item[0] : item[1] for item in [text.split(" ") for text in commands_info["parameters"]]}
        except:
            pass
        commands = commands_info["commands"]
        output_path = file_path.replace(path, EOSS_SENTENCES_PATH).replace(".txt", ".json")
        with open(output_path, "w") as output_file:
            possible_sentences = []
            for command in commands:
                command_param_placeholders = get_command_placeholders_positions(command)
                if len(command_param_placeholders) > 0:
                    possible_sentences += sentence_combinations(command, command_param_placeholders, parameters)
                else:
                    possible_sentences.append([command, {"entities": []}])
            # Shuffle before dumping
            random.shuffle(possible_sentences)
            json.dump(possible_sentences, output_file, indent=2)

# This function opens the parameters files and retrieves them as a dictionary (<param_name>:<list_of_params>)
def obtain_parameters(path=PARAMS_PATH):
    paths_list = [path + "/" + f_path for f_path in os.listdir(path)]
    parameters = {}
    for file_path in paths_list:
        with open(file_path, "r") as current_param_file:
            parameters[file_path.split("/")[-1].replace(".txt", "")] = [param.strip("\n") for param in current_param_file.readlines()]
    # year exception for decreasing complexity
    parameters["year"] = ["nri"]
    return parameters

if __name__ == "__main__":
    produce_sentences()


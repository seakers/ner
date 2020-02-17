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

EOSS_COMMANDS_PATH = "data/EOSS"
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
    all_parameters = obtain_parameters()
    sorted_parameters = []
    for element in command_param_placeholders:
        sorted_parameters.append(all_parameters[parameters[element[2]]])
    every_possible_combination_of_parameters = [itertools.product(*sorted_parameters)]
    return every_possible_combination_of_parameters
    """
    TODO: 
        - retrive corresponding lists of parameters
        - put them in a sorted list, considering how they appear on the command
        - create every possible combination of them
        - turn every combination into a sentence and append it to a file
    """
    pass

def produce_sentences(path=EOSS_COMMANDS_PATH):
    paths_list = [path + "/" + f_path for f_path in os.listdir(path)]
    for file_path in paths_list:
        commands_info = get_commands(file_path)
        parameters = {item[0] : item[1] for item in [text.split(" ") for text in commands_info["parameters"]]}  # May be failing
        commands = commands_info["commands"]
        for command in commands:
            command_param_placeholders = get_command_placeholders_positions(command)
            possible_combinations = sentence_combinations(command, command_param_placeholders, parameters)
            #TODO: pasar las combinaciones a oraciones y almacenarlas en un archivo

# This function opens the parameters files and retrieves them as a dictionary (<param_name>:<list_of_params>)
def obtain_parameters(path=PARAMS_PATH):
    paths_list = [path + "/" + f_path for f_path in os.listdir(path)]
    parameters = {}
    for file_path in paths_list:
        with open(file_path, "r") as current_param_file:
            parameters[file_path.split("/")[-1].replace(".txt", "")] = [param.strip("\n") for param in current_param_file.readlines()]
    return parameters

if __name__ == "__main__":
    samp = "data/EOSS/4004.txt"
    print(get_commands(samp)["commands"][-1])
    print(get_command_placeholders_positions(get_commands(samp)["commands"][-1]))
    #produce_sentences()
    print(obtain_parameters().keys())


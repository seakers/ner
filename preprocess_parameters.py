import random
import re

def prep_instruments_parameters(input_path, output_path):
    PARAM_NAME = "instrument_parameter.txt"
    with open(input_path, "r") as ip_file:
        file_as_list = ip_file.readlines()
        exit_file_list = []
        for line in file_as_list:
            new_line = line.replace("#", str(random.randint(1, 10)))
            keep_hyphens = random.uniform(0, 1) > 0.5
            if not keep_hyphens:
                new_line = new_line.replace("-", " ")
            exit_file_list.append(new_line)
    with open(output_path + "/" + PARAM_NAME, "w") as output_file:
        output_file.write("".join(exit_file_list))
    print("Instrument Parameters have been preprocessed ...")

def prep_measurements(path):
    with open(path, "r") as m_file:
        file_as_list = m_file.readlines()
        exit_file_list = []
        for line in file_as_list:
            new_line = re.sub(r'\([^)]*\)', '', line)
            exit_file_list.append(new_line)
    with open(path, "w") as output_file:
        output_file.write("".join(exit_file_list))
    print("Measurements have been preprocessed ...")

if __name__ == "__main__":
    ENGINEERING_PARAMETERS_PATH = "data/engineer"
    PROCESSED_PARAMETERS_PATH = "data/processed_parameters"
    prep_instruments_parameters("{}/instrument_parameters.txt".format(ENGINEERING_PARAMETERS_PATH), PROCESSED_PARAMETERS_PATH)
    prep_measurements("{}/measurement.txt".format(PROCESSED_PARAMETERS_PATH))

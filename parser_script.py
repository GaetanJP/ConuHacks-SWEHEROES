import sys
import json


def parse(json_file1, json_file2, json_file3):
    parsed_information = {}
    data1 = None
    data2 = None
    data3 = None

    with open(json_file1, "r") as file:
        data1 = json.load(file)
        file.close()

    with open(json_file2, "r") as file:
        data2 = json.load(file)
        file.close()

    with open(json_file3, "r") as file:
        data3 = json.load(file)
        file.close()
        
    return [data1, data2, data3]

import sys
import json


def parse(json_file):
    parsed_information = {}
    with open(json_file, "r") as file:
        data = json.load(file)
        return data


if __name__ == "__main__":
    exchange_json = sys.argv[1]
    parse(exchange_json)

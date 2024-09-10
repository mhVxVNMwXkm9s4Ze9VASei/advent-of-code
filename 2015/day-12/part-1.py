import os
import json

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    output = json.load(f)

    def parse_numbers(json_input):
        total = 0

        if isinstance(json_input, int):
            return json_input

        if isinstance(json_input, str):
            return 0

        if isinstance(json_input, list):
            for item in json_input:
                total += parse_numbers(item)

        if isinstance(json_input, dict):
            for item in json_input.values():
                total += parse_numbers(item)

        return total

    print(parse_numbers(output))

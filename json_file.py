import json

def create_json_file(fileName):
    file = open(fileName, "w")
    file.write ("[\n]")
    file.close
import os
import argparse
import json

def json2annotation(filename, output):
    vhjson = None
    with open(filename, 'r') as f:
        vhjson = json.load(f)


    for sequence_name in vhjson.items():
        for behaviour in vhjson[sequence_name[0]].items():
            for action in vhjson[sequence_name][behaviour[0]]["segments"].items():
                action_name = action[0]
                timestamp = action[1]["timestamp"]
                output_line = behaviour[0] + "_E_" + 
                

if __name__ == "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--filename", nargs="?", type=str, default="", help="File json to generate the annotations")
    PARSER_.add_argument("--output", nargs="?", type=str, default="", help="Output file")

    ARGS_ = PARSER_.parse_args()


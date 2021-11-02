import json
import os
import argparse

if __name__ == "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--behaviours_ids", nargs="?", type=str, default="behaviour_names.json", help="Dictionary with behaviour names and their respective index.")
    PARSER_.add_argument("--output", nargs="?", type=str, default="set_categories.txt", help="Behaviours ids in txt format.")

    ARGS_ = PARSER_.parse_args()

    f = open(ARGS_.behaviours_ids, 'r')
    bh_json = json.load(f)
    f.close()

    output = ""
    for item in bh_json.items():
        output = "set: " + str(item[1]) + "; " + item[0]

    with open(ARGS_.output, 'w') as f:
        f.write(output)

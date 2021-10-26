import os
import argparse
import json

virtualhome_actions = {"WALK":0, "RUN":1, "WALKTOWARDS":2, "WALKFORWARD":3, "TURNLEFT":4, "TURNRIGHT":5, "SIT":6, "STANDUP":7, "GRAB":8, "OPEN":9, "CLOSE":10, "PUT":11, "PUTIN":12, "SWITCHON":13, "SWITCHOFF":14, "DRINK":15, "TOUCH":16, "LOOKAT":17, "PUTBACK":18}

def json2annotation(filename, output_file):
    vhjson = None
    with open(filename+".json", 'r') as f:
        vhjson = json.load(f)

    output = ""
    for sequence_name in vhjson.items():
        for behaviour in vhjson[sequence_name[0]].items():
            timestampb = behaviour[1]["timestamp"]
            for action in behaviour[1]["segments"].items():
                action_name = action[0]
                timestamp = action[1]["timestamp"]
                output_line = (behaviour[0] + 
                    "_E_" + str(int(timestampb[0])).zfill(6) + "_" + str(int(timestampb[1])).zfill(6) + 
                    "_A_" + str(int(timestamp[0])).zfill(4) + "_" + str(int(timestamp[1])).zfill(4) + 
                    " " + str(virtualhome_actions[action_name.split("_")[0]]))
                output = output + output_line + "\n"
    with open(output_file, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--filename", nargs="?", type=str, default="", help="File json to generate the annotations")
    PARSER_.add_argument("--output", nargs="?", type=str, default="", help="Output file")

    ARGS_ = PARSER_.parse_args()

    json2annotation(ARGS_.filename, ARGS_.output)

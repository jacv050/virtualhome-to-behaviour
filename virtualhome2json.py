import os
import argparse
import json

#virtualhome_actions = {"WALK":0, "RUN":1, "WALKTOWARDS":2, "WALKFORWARD":3, "TURNLEFT":4, "TURNRIGHT":5, "SIT":6, "STANDUP":7, "GRAB":8, "OPEN":9, "CLOSE":10, "PUT":11, "PUTIN":12, "SWITCHON":13, "SWITCHOFF":14, "DRINK":15, "TOUCH":16, "LOOKAT":17, "PUTBACK":18}
#behaviour_names = {"make-a-coffee":1}
"""

La salida del archivo tiene que tener un formato similar a finegym

Salida virtualhome:
0 WALK 0 16
1 WALK 17 28
1 GRAB 29 36
2 WALK 37 51
2 PUTBACK 52 59
3 WALK 60 79
4 WALK 80 112
5 WALK 113 154

{"behaviourname": {"eventname": {"event":,"segments":,"timestamps":[T1,T2]},...}}

"""

def save_json(json_object, output):
    with open(output, 'w') as f:
        json.dump(json_object, f)

def convert2json(filename, behaviourname, virtualhome_actions, behaviour_names):
    action_number = 0
    behaviour = {}
    behaviour[behaviourname] = {}
    with open(filename, 'r') as f:
        for line in f:
            splitted = line.split()
            action_name = "{}_{}".format(splitted[1], action_number)
            behaviour[behaviourname][action_name] = {}
            behaviour[behaviourname][action_name]["event"] = virtualhome_actions[splitted[1]]
            behaviour[behaviourname][action_name]["segments"] = None
            behaviour[behaviourname][action_name]["timestamps"] = [float(splitted[2]), float(splitted[3])] #In this case frames instead of seconds

            action_number = action_number + 1

    return behaviour

def convert2jsonV2(filenamep, behaviourname, virtualhome_actions, behaviour_names):

    route_splitted = filenamep.split("/")
    action_number = 0
    behaviour = {}
    id_file = behaviourname+"-"+route_splitted[2]
    behaviour[id_file] = {}
    bname = behaviourname#+"-"+"{}".format(0).zfill(2)
    with open(filenamep, 'r') as f:
        behaviour[id_file][bname] = {}
        behaviour[id_file][bname]["id"] = behaviour_names[behaviourname] # instead "event"
        behaviour[id_file][bname]["segments"] = {}
        lastframe = 0.0
        for line in f:
            splitted = line.split()
            action_name = "{}_{}".format(splitted[1], "{}".format(action_number).zfill(2))
            behaviour[id_file][bname]["segments"][action_name] = {}
            behaviour[id_file][bname]["segments"][action_name]["timestamp"] = [float(splitted[2]), float(splitted[3])]
            if float(splitted[3]) > lastframe:
                lastframe = float(splitted[3])

            action_number = action_number + 1
        behaviour[id_file][bname]["timestamp"] = [0.0, float(lastframe)]

    return behaviour

if __name__ == "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--filename", nargs="?", type=str, default="", help="File to be convert to json")
    PARSER_.add_argument("--behaviourname", nargs="?", type=str, default="", help="Name of behaviour")
    PARSER_.add_argument("--behaviours_ids", nargs="?", type=str, default="behaviour_names.json", help="Dictionary with behaviour names and their respective index.")
    PARSER_.add_argument("--virtualhome_actions", nargs="?", type=str, default="virtualhome_actions.json", help="Dictionary with actions in virtualhome.")
    PARSER_.add_argument("--output", nargs="?", type=str, default="", help="Output file")

    ARGS_ = PARSER_.parse_args()


    f = open(ARGS_.virtualhome_actions)
    vh_actions_json = json.load(f)
    f.close()
    f = open(ARGS_.behaviours_ids)
    beh_ids_names = json.load(f)
    f.close()

    behaviour_json = convert2jsonV2(ARGS_.filename, ARGS_.behaviourname, vh_actions_json, beh_ids_names)
    save_json(behaviour_json, ARGS_.output)


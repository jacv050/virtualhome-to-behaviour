import os
import argparse
import json
import virtualhome2json
import json2annotation

if __name__ is "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--dir", nargs="?", type=str, default="", help="Directory with virtualhome data")

    ARGS_ = PARSER_.parse_args()

    with os.scandir(ARGS_.dir) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            splitted = dir.split('-')
            os.system("python virtualhome2json.py --filename " + dir + " --behaviourname " + splitted[0] + " --output" + splitted[0])
            os.system("python json2annotation.py --filename " + splitted[0] + " --output " + splitted[0])

import os
import argparse
import json
import virtualhome2json
import json2annotation

if __name__ == "__main__":
    PARSER_ = argparse.ArgumentParser(description="Parameters")
    PARSER_.add_argument("--dir", nargs="?", type=str, default="", help="Directory with virtualhome data")

    ARGS_ = PARSER_.parse_args()

    main_annotation = ""
    main_json = {}

    #with os.scandir(ARGS_.dir) as ficheros:
    with os.scandir(ARGS_.dir) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        for behaviour in subdirectorios:
            route = ARGS_.dir + "/" + behaviour
            for dir in os.listdir(route):
                file_input = route + "/" + dir + "/ftaa_" + behaviour + ".txt"
                file_output= route + "/" + dir + "/ftaa_" + behaviour + ".json"
                file_annotation= route + "/" + dir + "/ftaa_" + behaviour + "-annotation.txt"
                
                os.system("python virtualhome2json.py --filename " + file_input + " --behaviourname " + behaviour + " --output " + file_output)
                os.system("python json2annotation.py --filename " + file_output + " --output " + file_annotation)
            
                with open(file_output, 'r') as f:
                    json_file = json.load(f)
                    for object in json_file.items():
                        main_json[object[0]] = object[1]

                with open(file_annotation, 'r') as f:
                    main_annotation = main_annotation + f.read()

        with open("virtualhome_annotations.json", 'w') as f:
            json.dump(main_json, f)
        with open("virtualhome_labels.txt", 'w') as f:
            f.write(main_annotation)

import os
import json

import functions as f


fun_amount = 6


def benchmark():
    # może tutaj tą funkcję z maina ?
    pass


def read_and_edit_file(file_path):
    if os.path.getsize(file_path) <= 1:
        size = 0
        data = {
            "benchmark": {
                "tests": []
            }
        }
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)


    file_content = data["benchmark"]["tests"]
    print(file_content)
    size = len(file_content)

    common = [] # tu trzeba będzie wklepać parametry ogólne


    new_content = {
        "test_id": size+1,
        "common parameters": common,
        "results": []
    }

    results = new_content["results"]

    for f_id in range(fun_amount):

        cur_result = {
            "f_id": f_id+1,
            "function_type": f.names(f_id+1),
            "inertia": []
        }

        for mode in range(3):

            # obsługa zmiany parametrów
            # wykonanie funckji z maina

            values = [1]
            times = [8]

            cur_test = {
                "mode": mode,
                "values": values,
                "time": times,
            }
            cur_result["inertia"].append(cur_test)
        results.append(cur_result)
    file_content.append(new_content)

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


read_and_edit_file('./results/param_json.json')

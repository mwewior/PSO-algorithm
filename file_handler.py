import os
import json
import yaml

import functions as f


def get_yaml_params(file_path: str, key=""):

    with open(file_path, 'r') as f:
        general_params = yaml.load(f, Loader=yaml.FullLoader)
    if key != "":
        return general_params[key.lower()]
    else:
        return general_params


def save_results(file_path, test_results, clear=True):

    # TODO
    # normalnie nie będzie tego clear, albo będzie domyślnie na False ale na razie dla wygody jest True

    if os.path.getsize(file_path) <= 1 or clear is True:
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
    size = len(file_content)


    common = get_yaml_params('./parameters/general_params.yaml', "common")

    new_content = {
        "test_id": size+1,
        "common parameters": common,
        "results": []
    }

    results_list = new_content["results"]

    # jakoś inaczej przekazałbym to fun_amount
    fun_amount = 6  #TODO
    for f_id in range(fun_amount):

        cur_result = {
            "f_id": f_id+1,
            "function_type": f.names(f_id+1),
            "inertia": []
        }

        for mode in range(3):

            # obsługa zmiany parametrów
            # wykonanie funckji z maina

            values = test_results["values"][f_id][mode]
            times = test_results["times"][f_id][mode]

            cur_test = {
                "mode": mode,
                "values": values,
                "time": times,
            }
            cur_result["inertia"].append(cur_test)

        results_list.append(cur_result)
    file_content.append(new_content)

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


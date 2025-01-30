import os
import json
import yaml

import functions as f


def get_yaml_params(file_path: str, key=""):

    with open(file_path, "r") as f:
        general_params = yaml.load(f, Loader=yaml.FullLoader)
    if key != "":
        return general_params[key.lower()]
    else:
        return general_params


def save_results(file_path, test_results, clear=True):

    if os.path.getsize(file_path) <= 1 or clear is True:
        size = 0
        data = {"benchmark": {"tests": []}}
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)

    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    file_content = data["benchmark"]["tests"]
    size = len(file_content)

    common = get_yaml_params("./parameters/general_params.yaml", "common")

    new_content = {
        "test_id": size + 1,
        "common parameters": common,
        "results": [],
    }

    results_list = new_content["results"]

    fun_amount = 6
    for f_id in range(fun_amount):

        cur_result = {
            "f_id": f_id + 1,
            "function_type": f.names(f_id + 1),
            "inertia": [],
        }

        for mode in range(4):

            values = test_results["values"][f_id][mode]
            mean = test_results["mean"][f_id][mode]
            deviation = test_results["standard deviation"][f_id][mode]
            percentage_deviation = test_results["percentage deviation"][f_id][
                mode
            ]
            times = test_results["times"][f_id][mode]
            histories_means = test_results["histories_means"][f_id][mode]
            worst_fitness = test_results["worst_fitness"][f_id][mode]
            best_fitness = test_results["best_fitness"][f_id][mode]

            cur_test = {
                "mode": mode,
                "mean": mean,
                "standard deviation": deviation,
                "percentage deviation": percentage_deviation,
                "values": values,
                "time": times,
                "histories_means": histories_means,
                "worst_fitness": worst_fitness,
                "best_fitness": best_fitness,
            }
            cur_result["inertia"].append(cur_test)

        results_list.append(cur_result)
    file_content.append(new_content)

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

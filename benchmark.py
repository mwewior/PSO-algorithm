import os
import json

import functions as f


fun_amount = 6

"""
{
    benchmark:
    {
        tests: [
            {
                id: 1,
                results: [
                    {
                        f_id: 1
                        funciton_type: "wielomian",         # nazwa funkcji celu
                        inertia: [
                            {
                                mode: 1
                                values: [0, 0.124, ...],    # wartości z każdego testu
                                time:   [14, 12, ...],      # czasy trwania
                            },
                            {
                                mode: 2
                                values: [0, 0.124, ...],    # wartości z każdego testu
                                time:   [14, 12, ...],      # czasy trwania
                            },
                            {
                                mode: 3
                                values: [0, 0.124, ...],    # wartości z każdego testu
                                time:   [14, 12, ...],      # czasy trwania
                            },
                        ]
                    },

                    ...

                ]
            },

            ...


        ]
    }
}

"""


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
            values = [1]
            times = [8]

            cur_test = {
                "mode": mode,
                "values": values,
                "time": times,
            }
            cur_result["inertia"].append(cur_test)
        results.append(cur_result)
        print(new_content)
    file_content.append(new_content)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

read_and_edit_file('./results/param_json.json')


# test_num = len(o)
# read_file('./results/param_json.json')

# def edit_file(file):
#     size = len(file)
#     new_data =



# import yaml


# def edytuj_parametry(plik_yaml, klucz, nowa_wartosc):
#     # Odczytaj zawartość pliku YAML
#     with open(plik_yaml, 'r') as plik:
#         dane = yaml.safe_load(plik)

#     # Edytuj parametr o określonym kluczu
#     dane[klucz] = nowa_wartosc

#     # Zapisz zmienione dane z powrotem do pliku
#     with open(plik_yaml, 'w') as plik:
#         yaml.dump(dane, plik)

# # Przykład użycia
# plik_yaml = 'param_test.yaml'
# klucz_do_edytowania = 'AAA'
# nowa_wartosc = {'1a': 1, 'dwa': 4, '3': 9, 4: 16}

# edytuj_parametry(plik_yaml, klucz_do_edytowania, nowa_wartosc)



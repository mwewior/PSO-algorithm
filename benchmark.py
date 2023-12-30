import json


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


def edit_file(file_path, test_result_dict):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)




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



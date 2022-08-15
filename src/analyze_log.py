import csv


def most_request_food_maria(data):
    request_foods_maria = list()
    foods_quantity_request = dict()
    for info in data:
        if info[0] == 'maria':
            request_foods_maria.append(info[1])
    for food in request_foods_maria:
        if food in foods_quantity_request:
            foods_quantity_request[food] += 1
        else:
            foods_quantity_request[food] = 1
    most_request = max(
        foods_quantity_request, key=lambda f: foods_quantity_request[f]
    )
    return most_request


def arnold_hamburger_requests(data):
    hamburguers = 0
    for info in data:
        if info[0] == 'arnaldo' and info[1] == 'hamburguer':
            hamburguers += 1
    return hamburguers


def foods_joao_never_request(data):
    requests_foods = set()
    joao_requests = set()
    for info in data:
        requests_foods.add(info[1])
        if info[0] == 'joao':
            joao_requests.add(info[1])
    foods_never_request = requests_foods.symmetric_difference(joao_requests)
    return foods_never_request


def days_joão_not_be_present(data):

    all_days = set()
    joao_days = set()
    for info in data:
        all_days.add(info[2])
        if info[0] == 'joao':
            joao_days.add(info[2])
    days_did_not_present = all_days.symmetric_difference(joao_days)
    return days_did_not_present


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as csv_file:
            file_data = csv.reader(csv_file)
            list_result = [data_element for data_element in file_data]
            string_result = (
                f"{most_request_food_maria(list_result)}\n"
                f"{arnold_hamburger_requests(list_result)}\n"
                f"{foods_joao_never_request(list_result)}\n"
                f"{days_joão_not_be_present(list_result)}"
            )
        with open('data/mkt_campaign.txt', 'w') as new_file:
            print(string_result, file=new_file)
    except FileNotFoundError:
        if not path_to_file.endswith('csv'):
            raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
        else:
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

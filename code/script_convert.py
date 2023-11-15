'''Small script to convert months to a json file'''

import json
import os

def write_to_file(json_result):
    file = "app/namnsdagar.json"

    if os.path.isfile(file):
        os.remove(file)

    with open(file, "w", encoding="utf-8") as to_file:
        to_file.write(json_result)


def translate_month(input_month):
    month = ''
    match input_month:
        case 'januari':
            month = "January"
        case 'februari':
            month = "February"
        case 'mars':
            month = "March"
        case 'april':
            month = "April"
        case 'maj':
            month = "May"
        case 'juni':
            month = "June"
        case 'juli':
            month = "July"
        case 'augusti':
            month = "August"
        case 'september':
            month = "September"
        case 'oktober':
            month = "October"
        case 'november':
            month = "November"
        case 'december':
            month = "December"
    return month

def catch_data():
    path = 'months/'
    months = list(os.listdir(path))

    month_data = {}

    for month in months:
        file = f'{path}/{month}'
        with open(file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            day, names = line.strip().split(' 	')
            month_data[day] = names
        formatted_data = []
        for day, names in month_data.items():
            day_number, day_month = day.split(" ")
            day_number = int(day_number)
            formatted_data.append({
                "month": translate_month(day_month),
                "day": day_number,
                "names": names
            })
        print(f"{month} has been converted into json")
    result = {"data": formatted_data}

    json_result = json.dumps(result, indent=2, ensure_ascii=False)
    write_to_file(json_result)


if __name__ == "__main__":
    catch_data()
    print("### Script executed ###")

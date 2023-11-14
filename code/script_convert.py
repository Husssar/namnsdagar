import json
import os


def write_to_file(json_result):
    file = "../app/namnsdagar.json"

    if os.path.isfile(file):
        os.remove(file)

    f = open(file, "w")
    f.write(json_result)
    f.close()


def translate_month(input_month):
    match input_month:
        case 'januari':
            return "January"
        case 'februari':
            return "February"
        case 'mars':
            return "March"
        case 'april':
            return "April"
        case 'maj':
            return "May"
        case 'juni':
            return "June"
        case 'juli':
            return "July"
        case 'augusti':
            return "August"
        case 'september':
            return "September"
        case 'oktober':
            return "October"
        case 'november':
            return "November"
        case 'december':
            return "December"


def catch_data():
    path = '../months'
    months = [f for f in os.listdir(path)]

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

    result = {"data": formatted_data}

    json_result = json.dumps(result, indent=2, ensure_ascii=False)
    write_to_file(json_result)


if __name__ == "__main__":
    catch_data()

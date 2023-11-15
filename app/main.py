''' webserver script to show namesdays '''
import calendar
import datetime
import json

import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world!"}


@app.get("/today")
def namesday():
    with open('namesday/app/namnsdagar.json', 'r', encoding="utf-8") as name:
        to_json = json.loads(name.read())

    date_now = datetime.datetime.now()
    month = calendar.month_name[date_now.month]
    today = date_now.day
    names = [day for day in to_json['data'] if day['month'] == month and day['day'] == today]

    return {"Day": today, "Month": month, "namesday": names[0]['names']}


@app.get("/all")
def namesday_all():
    with open('namesday/app/namnsdagar.json', 'r', encoding="utf-8") as name:
        return json.loads(name.read())


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)

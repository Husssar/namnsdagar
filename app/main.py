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
    name = open('app/namnsdagar.json', 'r').read()
    to_json = json.loads(name)
    date_now = datetime.datetime.now()
    this_month = calendar.month_name[date_now.month]
    this_day = date_now.day
    today = [day for day in to_json['data'] if day['month'] == this_month and day['day'] == this_day]

    return {"Day": this_day, "Month": this_month, "namesday": today[0]['names']}


@app.get("/all")
def namesday_all():
    name = open('app/namnsdagar.json', 'r').read()

    return json.loads(name)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)



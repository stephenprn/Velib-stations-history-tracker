import requests
import db
import schedule
import time

from models.station import Station

STATIONS_STATUS_URL = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"


def init_db():
    db.meta.create_all()


def scrap_api():
    response = requests.get(STATIONS_STATUS_URL)

    [
        db.session.add(Station.from_dict(station_dict))
        for station_dict in response.json()["data"]["stations"]
    ]

    db.session.commit()


def schedule_scrap_api():
    schedule.every(15).minutes.do(scrap_api)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    init_db()
    scrap_api()
    schedule_scrap_api()

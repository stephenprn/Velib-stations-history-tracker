from sqlalchemy import Column
from sqlalchemy.types import Integer, BigInteger, String, Boolean, JSON

from typing import Dict
from models._shared import ModelBase


class Station(ModelBase):
    __tablename__ = "station"

    station_code = Column(String(128), nullable=False)
    station_id = Column(BigInteger, nullable=False)

    is_installed = Column(Boolean, nullable=False)
    is_renting = Column(Boolean, nullable=False)
    is_returning = Column(Boolean, nullable=False)

    last_reported = Column(BigInteger, nullable=False)

    num_bikes_available = Column(Integer, nullable=False)
    num_docks_available = Column(Integer, nullable=False)
    num_bikes_available_types = Column(JSON, nullable=False)

    @staticmethod
    def from_dict(data: Dict) -> "Station":
        station = Station()

        station.station_code = data["stationCode"]
        station.station_id = data["station_id"]

        station.is_installed = data["is_installed"]
        station.is_renting = data["is_renting"]
        station.is_returning = data["is_returning"]

        station.last_reported = data["last_reported"]

        station.num_bikes_available = data["num_bikes_available"]
        station.num_docks_available = data["num_docks_available"]

        num_bikes_available_types = {}

        for type_ in data["num_bikes_available_types"]:
            num_bikes_available_types = {**num_bikes_available_types, **type_}

        station.num_bikes_available_types = num_bikes_available_types

        return station

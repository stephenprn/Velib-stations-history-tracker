from sqlalchemy import Column, func
from sqlalchemy.types import Integer, DateTime, String

from db import Base
from utils import generate_uuid


class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=generate_uuid, unique=True, nullable=False)

    creation_date = Column(DateTime, default=func.current_timestamp())
    update_date = Column(
        DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

from sqlalchemy import Table, Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.sqltypes import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional, Tuple, List, Dict

Base = declarative_base()


class SurfLine(Base):
	# Surfline data

	# DateTime
	# Location (Lat, Long)
	# Forecasted height
	# ...

class Buoy(Base)
	# Buoy Data

	# Lots of columns, can grab from existing DB


class Tide(Base)
	# Tide data

	__tablename__ = "tidevals"

	id = Column(Integer, primary_key=True, unique=True)
	buoy_id = Column(Integer, nullable=False)
	location = Column(String(50), nullable=False)
	datetime = Column(Date, nullable=False)
	predicted = Column(Float, nullable=False)
	highlow = Column(String(2), nullable=False)

	# Set up REPR


class Weather(Base)
	# Weather data
	
	__tablename__ = "NOAAHourlyForecast"

	id = Column(Integer) ## Need to autoincrement
	buoy_id = Column(Integer, primary_key=True)
	starttime = Column(DateTime, primary_key=True)
	temp = Column(Integer)
	windspeed = Column(Integer)
	winddir = Column(String)
	forecast = Column(String)

	# Set up REPR


	# DateTime
	# Location (Lat, Long)

	### Use prediction for forward looking, update previous with observed


class Sat(Base)
	# SAT DATA
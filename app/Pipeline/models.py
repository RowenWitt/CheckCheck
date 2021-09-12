from sqlalchemy import Table, Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.sqltypes import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional, Tuple, List, Dict

Base = declarative_base()


# class SurfLine(Base):
# 	# Surfline data

# 	# DateTime
# 	# Location (Lat, Long)
# 	# Forecasted height
# 	# ...

class Buoy(Base):
	# Buoy data

	__tablename__ = 'buoy_data'

	id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
	buoy_id = Column(Integer)
	date = Column(DateTime, primary_key=True)
	wdir = Column(Integer)
	wspd = Column(Float)
	gst = Column(Float)
	wvht = Column(Float)
	dpd = Column(Integer)
	apd = Column(Float)
	mwd = Column(Integer)
	pres = Column(Float)
	atmp = Column(Float)
	wtmp = Column(Float)
	dewp = Column(String)
	vis = Column(String)
	ptdy = Column(String)
	tide = Column(String)

	# Set up REPR


class Tide(Base):
	# Tide data -- not currently used

	__tablename__ = "tide_vals"

	id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
	buoy_id = Column(Integer, nullable=False)
	location = Column(String(50), nullable=False)
	datetime = Column(Date, nullable=False)
	predicted = Column(Float, nullable=False)
	highlow = Column(String(2), nullable=False)

	# Set up REPR


class Weather(Base):
	# Weather data
	
	__tablename__ = "noaa_hourly_forecast"

	id = Column(Integer, unique=True, autoincrement=True) ## Need to autoincrement
	buoyid = Column(Integer, primary_key=True)
	starttime = Column(DateTime, primary_key=True)
	temp = Column(Integer)
	windspeed = Column(Integer)
	winddir = Column(String)
	forecast = Column(String)

	# Set up REPR

	### Use prediction for forward looking, update previous with observed


# class Sat(Base)
# 	# SAT DATA
# 	pass
from sqlalchemy import Table, Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint
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

	# DateTime
	# Location (Lat, Long)
	# Predicted tide by NOAA
	# Other tide predictions?


class Weather(Base)
	# Weather data

	# DateTime
	# Location (Lat, Long)

	### Use prediction for forward looking, update previous with observed


class Sat(Base)
	# SAT DATA
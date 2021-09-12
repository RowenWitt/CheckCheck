from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import json, os
from typing import Tuple, List, Dict

from sqlalchemy import create_engine, select, insert, update, func, inspect, and_
from sqlalchemy.orm import sessionmaker, scoped_session

from app.Pipeline.models import SurfLine, Tide, Buoy, Weather, Sat
 ## Make sure to switch all imports over when that happens

 db_url = os.getenv("DB_URL")


# Will need to get data from S3 for training and prediction

# Will need a function to weave together S3 data and DB data to feed to wave_dance
# Memory will be a concern, build with batching in mind, do some benchmarking to see what batch size is reasonable
# What is the size of an unpacked grib file in active memory?  Ideally I can package data at least in sets of days... a week would be great
# A week of GRIB data would be 4 * 7 = 28 GRIB files worth of data, vague recollection says each file is ~7 MBs, 28 * 7 is 196 MBs, maybe half weeks?
# The size of the data that can be represented will determine the size of the model batches/epochs, I'd like to have the biggest possible epoch

## Because data will be weaved together here and passed directly to the wave_dance file, Fourier Analysis should occur here

### Considering two files, read_DB and write_DB for loaded memory optimization

### Fourier Fill needs to have a specific application for each required use, BUOY, TIDE, SAT_DAT, SURFLINE
### Should somehow weight available neighboring datapoints by temporal distance

class Database(object):

	def __init__(self):
		self.engine = create_engine(
			db_url,
			pool_recycle=3600,
			pool_size=10,
			echo=False,
			pool_pre_ping=True
		)

		self.Sessionmaker = scoped_session(
			sessionmaker(
				autoflush=False,
				autocommit=False,
				bind=self.engine
			)
		)


		self.table_names = {
						"surfline":SurfLine,
						"tide":Tide,
						"buoy":Buoy,
						"weather":Weather,
						}
		# Setup S3 connected class
		# Setup DB connection parameters from .env
		# Define data model self.WEATHER_schema
		# Define data model self.BUOY_schema
		# Define data model self.TIDE_schema
		# Define data model self.SURFLINE_schema
		

	# WEATHER functions

		# Validate input against self.WEATHER_schema

		def insert_weather(data: List[Dict]):
			"""
			Insert data to WEATHER table, accepts output of get_weather_update(correct_grid_calls) from buoy_tide_weather.py as input
			"""
			with self.Sessionmaker() as session:
				for obs in data:
					step = Weather(**obs)
					session.merge(step)  # May need to go back to old functionality
				s.commit()

		# Update data WEATHER table by location and DateTime
		# Get all data WEATHER table (for past year)
		# Get all data WEATHER table from location
		# Get data WEATHER table from specific time range (with default period)
		# Get data WEATHER table from specific time range for location (with default period)


	# BUOY functions

		# Call get new data function (list of locations and URLs, data.py) from buoy_tide_weather.py

		# Validate input against self.BUOY_schema

		# Insert data to BUOY table
		# Update data BUOY table by buoyID and DateTime
		# Get all data BUOY table YEAR
		# Get all data BUOY table from location YEAR
		# Get data BUOY table from specific time range (with default period)
		# Get data BUOY table from specific time range for location (with default period)

		# Fourier Fill BUOY data, return FF


	# TIDE functions

		# Call get new data function (list of locations and URLs, data.py) from buoy_tide_weather.py

		# Validate input against self.TIDE_schema

		def insert_tide(data: List[Dict]):
			"""
			Insert data to TIDE table
			"""
			processed_data = []
			for rows in data:
				entry = {'buoyid':rows[3], 'location':rows[4], 'datetime':rows[0], 'predicted':rows[1], 'highlow':rows[2]}
				processed_data.append(entry)

			with self.Sessionmaker() as session:
				for datum in processed_data:
					obj = Tide(**datum)
					session.add(obj)
					session.commit()

		# Update data TIDE table by location and DateTime
		# Get all data TIDE table YEAR
		# Get all data TIDE table from location YEAR
		# Get all data TIDE table from specific time range (with default period)
		# Get all data TIDE table from specific time range for location (with default period)

		# Fourier Fill TIDE data, return FF

	# SURFLINE functions

		# Call get new data function (list of locations and URLs, data.py) from surfline.py

		# Validate input against self.SURFLINE_schema

		# Insert data to SURFLINE table
		# Update data SURFLINE table by Location and DateTime
		# Get add data SURFLINE table YEAR
		# Get all data SURFLINE table from location YEAR
		# Get all data SURFLINE table from specific time range (with default period)
		# Get all data SURFLINE table from specific time range for location (with default period)

		# Fourier Fill TIDE data, return FF


	# SAT_S3 functions

		# Call get new data function (list of locations and URLs, data.py, build URL possibility) from sat_dat.py

		# Insert data to S3 Bucket (possibilty to rename) from sat_dat.py

		# Get data from S3 Bucket (should be able to deterministically reference files) from sat_dat.py

		# Fourier Fill (cool name right) for given list of GRIB files, return FF





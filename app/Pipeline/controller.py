from app.Pipeline.db import Database
from app.Pipeline.buoy_tide_weather import BTW

from app.Pipeline.buoy_tide import buoy_tide as buoy
from app.Pipeline.sat_dat import sat_dat as sat
from app.Pipeline.surfline import surfline as surf
# Once classes done for all above, will be able to just import one class per file

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import requests, time, json, re
import os, logging
from typing import Tuple, List, Dict


# Controller will contain summation functions to get new data from API's validate, and put into DB & S3 bucket

# How do you use an S3 bucket?

class Controller(object):

	def __init__():
		self.DB = app.Pipeline.db.Database()
		self.BTW = app.Pipeline.buoy_tide_weather.BTW()







	def get_two_hundred_years_tides():
		""" runs get_historical_tide() from buoy_tide_weather.py passes to insert_tide() from db.py """
		data = self.BTW.get_historical_tide()
		self.DB.insert_tide(data)



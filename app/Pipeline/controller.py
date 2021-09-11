from app.Pipeline.db import db as db
from app.Pipeline.models import models as models
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



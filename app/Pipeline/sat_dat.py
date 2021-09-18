from app.Pipeline.fourier import fourier
from app.Pipeline.data import times
import json
import os
import requests
import datetime
import time
import re
from datetime import date
from typing import Tuple, List, Dict


# Fourier infilling probably shouldn't happen here if I'm storing the files
# in GRIB format, unless I want to update GRIB files which seems tricky

# Therefore this file will simply contain the following functions within class


class Satellite(object):

    def __init__(self):
        self.times = times
        self.t_keys = list(times.keys())
        self.root_url = 'https://nomads.ncep.noaa.gov/dods/wave/gfswave/{}{}{}/gfswave.epacif.0p16_{}z'

    def check_make_zero_pad(self, data: int) -> str:
        """
        Checks if int is single digit, zero pads if true
        """
        if len(str(data)) < 2:
            return '0' + str(data)
        else:
            return data

    def gribbet(self, retro=7):
        """
        Attempts to download 4 timesteps for today,
        4 timesteps for retro iterations before today
        Only works for netCDF4 format grib has 4 files per one netCDF4 file
        """
        today = date.today()
        r_day = today.day
        r_month = self.check_make_zero_pad(today.month)
        r_year = today.year

        for day in range(retro):
            for i in range(len(self.t_keys)):
                c_day = check_make_zero_pad(r_day - day)
                url = root_url.format(
                    r_year, r_month, c_day, self.times[self.t_keys[i]])

    def upload_s3(self, data: List):
        """
        function to upload file to S3 bucket using Boto3
        """
        pass

# Get files from NOAA

    # Maybe build link to get files based on time and link format for NOAA

# Upload files to S3 bucket

    # Maybe rename files for easier future access

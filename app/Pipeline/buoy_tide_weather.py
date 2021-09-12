from app.Pipeline.data import tide_station_list, historicInfill


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import json, os
from typing import Tuple, List, Dict

import requests





class BTW(object):




















	def get_historical_buoy():
		""" Gets historical data dump from buoy page """


		pass


	def get_historical_tide() -> List[List]:
		""" 
	    Makes calls for each buoy on list for year intervals on list.  Stores in one big array.
	    Only about 130k records so one big array is fine.  Not sure point at which that needs to 
	    be broken up.
	    """
	    KPList = list(historicInfill.values())[0]
	    keyList = [list(i.keys())[0] for i in KPList]
	    station_list_keys = list(tide_station_list.keys())
	    station_list_values = list(tide_station_list.values())
	    bigList = []
	    for j in range(len(station_list_keys)):
	        id = station_list_values[j]
	        idName = station_list_keys[j]
	        for i in range(len(keyList)):
	            start = list(KPList[i].values())[0]['start']
	            end = list(KPList[i].values())[0]['end']
	            call = requests.get(f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={start}&end_date={end}&station={id}&product=predictions&datum=STND&time_zone=gmt&interval=hilo&units=english&application=Waves_data&format=json")
	            try:
	                response = call.json()['predictions']
	            except KeyError:
	                print("Failed at {idName}".format)
	                return bigList
	            oneStep = [list(i.values()) for i in response]
	            print(id, idName, start, end)
	            [i.extend([id, idName]) for i in oneStep]
	            bigList.extend(oneStep)
	            if (i + 1) % 5 == 0:
	                print("Buoy {} API call {} / {} complete, sleeping 45".format(id, i+1, len(keyList)))
	                time.sleep(45)

	    return bigList
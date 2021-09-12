from app.Pipeline.data import tide_station_list, historicInfill, lat_long, buoy_list


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import json, os, requests, datetime, time, re
from typing import Tuple, List, Dict




class BTW(object):


	def fix_nulls(str) -> str:
		"""
		Fixes nulls to be -1 instead of string
		"""
		if type(data) == str:
			return data.replace('MM','-1')



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



		def get_updated_buoy_data(input):
			""" gets updated buoy data for all buoys in tuple (id, lat/long) input """
			output_list = []
			for j in input: 
				a = requests.get('https://www.ndbc.noaa.gov/data/realtime2/{}.txt'.format(j[0])) # remove slice for prod
				# Data goes back for 45 days
				b = a.text.split('\n')
				c = [" ".join(re.split(r'\s+', i)) for i in b]
				d = [i.split() for i in c]
				d = d[2:-1]
				h = []
				try:
					for i in d:
						bid = j[0]
						dt= i[0]+'/'+i[1]+'/'+i[2]+' '+i[3]+':'+i[4]+':'+'00'
						dt = datetime.datetime.strptime(dt, '%Y/%m/%d %H:%M:%S')
						wdir = self.fix_nulls(i[5])
						wspd = self.fix_nulls(i[6])
						gst = self.fix_nulls(i[7])
						wvht = self.fix_nulls(i[8])
						dpd = self.fix_nulls(i[9])
						apd = self.fix_nulls(i[10])
						mwd = self.fix_nulls(i[11])
						pres = self.fix_nulls(i[12])
						atmp = self.fix_nulls(i[13])
						wtmp = self.fix_nulls(i[14])
						dewp = self.fix_nulls(i[15])
						vis = i[16]
						ptdy = i[17]
						tide = i[18]
						b = {'buoy_id':bid, 'date':dt, 'wdir':wdir, 'wspd':wspd, 'gst':gst, 'wvht':wvht, 'dpd':dpd, 'apd':apd, 'mwd':mwd, 'pres':pres, 'atmp':atmp, 'wtmp':wtmp, 'dewp':dewp, 'vis':vis, 'ptdy':ptdy, 'tide':tide}
						output_list.append(b)
				except IndexError:
						pass
			return output_list



		def get_buoy_links() -> List:
			"""
			Gets correct links for nearest buoy to Lat/Long
			"""
			call_list = []

			for a,b in lat_long:
				first_header = 'https://api.weather.gov/points/{},{}'.format(a, b)
				first_resp = requests.get(first_header).json()
				second_header = first_resp['properties']['forecastHourly']
				call_list.append(second_header)

			return call_list



		def get_weather_update(calls) -> :
			output_list = []
			slumb = 0
			for j in calls:
				slumb += 1
				if slumb % 5 == 0:
					time.sleep(30)
				a = requests.get(j[0]).json()
				try:
					a = a['properties']['periods']
					# print(a[0])
				except KeyError:
					print(a) # LOG
					pass

				for i in a:
					try:
						bid = j[1]
						tar = i['startTime'][:i['startTime'].rindex('-')].replace('T', ' ')
						dt = datetime.datetime.strptime(tar, "%Y-%m-%d %H:%M:%S")
						te = i['temperature']
						ws = re.sub("[^0-9]", '', i["windSpeed"])
						wd = i['windDirection']
						sf = i['shortForecast']
						b = {'buoyid':bid, 'starttime':dt, 'temp':te, 'windspeed':ws, 'winddir':wd, 'forecast':sf}
						output_list.append(b)
					except (TypeError, KeyError) as e:
						pass # LOG
			return output_list

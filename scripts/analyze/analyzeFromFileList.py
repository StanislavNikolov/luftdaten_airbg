#!/bin/env python3

import sys, time, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mpldates

minute = 60
time_step = 30 * minute

buckets = {}
bucketIds = [] # gets sorted later on (no sort on dicts), which is important for plotting

def add(record):
	bucketId = int(record[1] / time_step)
	if bucketId not in bucketIds:
		bucketIds.append(bucketId)
		buckets[bucketId] = []

	buckets[bucketId].append(record)

recordsParsed = 0

for filename in sys.stdin.read().split('\n'):
	if "sds011" not in filename: continue
	with open(filename) as f:
		for recordstr in f.readlines()[1:]:
			try:
				record = recordstr.split(';')
				sid = record[0]

				unix_time = int(time.mktime(time.strptime(record[5], '%Y-%m-%dT%H:%M:%S')))

				pm10 = float(record[6])
				pm25 = float(record[9])

				lat = float(record[3])
				lon = float(record[4])

				add((sid, unix_time, pm10, pm25, lat, lon))
				recordsParsed += 1
			except:
				print('error', filename, record, file=sys.stderr)

print(recordsParsed, 'records parsed', file=sys.stderr)

bucketIds.sort()

def getAverage():
	averages = []
	times = []

	print('time,average p25,samples')
	for buckI in bucketIds:
		buck = buckets[buckI]
		human_time = datetime.datetime.fromtimestamp(buckI * time_step).strftime('%Y-%m-%dT%H:%M:%S')
		#mpl_time = datetime.datetime.fromtimestamp(buckI * time_step)
		#times.append(mpl_time)

		p25sum = sum(x[3] for x in buck)
		average = p25sum / len(buck)
		#averages.append(average)

		print(human_time, ',', "{:.2f}".format(average), ',', len(buck))

	'''
	fig, ax = plt.subplots()
	plt.plot(times, averages)
	plt.title('Average PM2.5 µg/m3 in Sofia')
	#formatter = mpldates.DateFormatter('%y-%m-%d\n%H:%M:%S')
	formatter = mpldates.DateFormatter('%y-%m-%d')
	ax.xaxis.set_major_formatter(formatter)
	plt.show()
	'''

def getWorstStations():
	print('id, name,lat,lon,cnt')

	locPerId = {}
	cntPerId = {}

	for buckI in bucketIds:
		buck = buckets[buckI]

		human_time = datetime.datetime.fromtimestamp(buckI * time_step).strftime('%Y-%m-%dT%H:%M:%S')

		p25sum = sum(x[3] for x in buck)
		average = p25sum / len(buck)

		sumPerId = {}
		for r in buck:
			if r[0] not in sumPerId:
				sumPerId[r[0]] = (0, 0)
				locPerId[r[0]] = (r[4], r[5])
			s, c = sumPerId[r[0]]
			s += r[3]
			c += 1
			sumPerId[r[0]] = (s, c)

		averagesForStation = []
		for id in sumPerId:
			averagesForStation.append((sumPerId[id][0] / sumPerId[id][1], id))

		averagesForStation.sort(reverse=True)
		cnt = 0
		for avr in averagesForStation:
			id = avr[1]
			if id not in cntPerId: cntPerId[id] = 0
			cntPerId[id] += 1
			cnt += 1
			if cnt >= 3: break

	for id in cntPerId:
		print(id, ',', 'no name', ',', locPerId[id][0], ',', locPerId[id][1], ',', cntPerId[id])


#getAverage()
getWorstStations()

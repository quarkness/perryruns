import json
import requests
from config import access_token

headers = {
	'Content-Type': 'application/vnd.com.runkeeper.NewFitnessActivity+json',
	'Authorization':' Bearer %s' % access_token,
}

data = {
   "type": "Running",
   "equipment": "Treadmill",
   "start_time": "Sat, 8 Apr 2013 01:15:00",
   "notes": "My second late-night run",
   "post_to_facebook": False,
   "post_to_twitter": False
}
rotation_distance = .31
ts = 0
total_distance = 0
distance = []
dts = [0.32, 0.33, 0.4, 0.48, 0.56, 0.65, 0.75] * 150
for dt in dts:
	ts += dt
	total_distance += rotation_distance
	distance.append({
		'timestamp': round(ts, 2),
		'distance': round(total_distance, 2)
		})

data['distance'] = distance
data['total_distance'] = round(total_distance, 2)
data['duration'] = round(sum(dts), 2)
print data
r = requests.post('https://api.runkeeper.com/fitnessActivities', data=json.dumps(data), headers=headers)

print r.status_code
print r.content

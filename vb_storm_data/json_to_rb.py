import json
f = open('/Users/Ben/Downloads/vb_storm/storm_catch.json', 'r')
o = open('/Users/Ben/Downloads/vb_storm/storm_catch.rb', 'w')
count = 0
for line in f:
	if 'coordinates' in line:
		count += 1
		j = json.loads(line)
		lng = j['geometry']['coordinates'][0][0]
		lat = j['geometry']['coordinates'][0][1]
		str = 'Thing.create(city_id: {}, lng: {}, lat: {})\n'.format(count, lng, lat)
		o.write(str)

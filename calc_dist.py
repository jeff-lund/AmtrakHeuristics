import math

# opening files
f_cities = open('cities', 'r')
f_ll = open('cities_long_lat', 'r')
fout = open('amtrak_euc', 'w')

# writing city list - cities
buf = f_cities.readlines()
cities = [x.rstrip() for x in buf]
f_cities.close()

def haversines(la1, la2, lo1, lo2):
	p = math.pi/180
	a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
	return 12742 * asin(sqrt(a)) #2*R*asin...

# writing long-lat list - long-lat
buf = f_ll.readlines()
long_lat = []
for x in buf:
	x = x.rstrip()
	long_lat.append(x.strip(' '))
for x in long_lat:
	x[1] = float(x[1])
	x[2] = float(x[2])
# Haversines
for x in cities:
	for y in cities:
		if x == y:
			continue
		dist = haversines(x[1], y[1], x[2], y[2])
		print(x, y, dist, file=fout)

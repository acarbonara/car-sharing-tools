import os
import sys
import itertools
import datetime
from carmodule import *
from math import radians, cos, sin, asin, sqrt

def convert_from_timestamp(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    t_s = str(date).split(" ")
    return t_s[1]

lines = []
cars = []

h1 = int(sys.argv[1])
h2 = int(sys.argv[2])

new_file = 'allvehicles.csv'
f = open(new_file, 'r')
content = f.read().splitlines()
f.close()

for c in content:
    lines.append(c.split(" "))

# filling the list of cars with the lines of the allvehicles.csv file
for l in lines:
    car = CarInfo(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
    cars.append(car)

new_file = sys.argv[3]
f = open(new_file, 'r')
content = f.read().splitlines()
f.close()

lines = []
lists = []

for c in content:
    if "alpha" not in c:
        lines.append(c.split(" "))

for l in lines:
    list_size = l[0]
    car_id = l[1]
    lists.append((list_size, car_id))

new_file.replace(".csv", "")
file_string = 'heatmap' + new_file + '-' + h1 + '-' + h2 + '.csv'
file_string = file_string.replace("matched-cars-final", "")

f = open(file_string, 'w')
for e in lists:
    list_size = e[0]
    id1 = e[1]
    for car in cars:
        id2 = car.getCarId()
        if id1 == id2:
            start_time = car.getStartTime()
            long_start = car.getLongStart()
            lat_start = car.getLatStart()
            time = convert_from_timestamp(int(start_time))
            t = time.split(":")
            h = int(t[0])
            m = int(t[1])
            if h >= h1 and (h < h2 or (h == h2 and m <= 0)):
                out_string = long_start + " " + lat_start + " " + list_size + "\n"
                f.write(out_string)
                print "Writing: ", out_string
                break
f.close()

'''print "Filtering heatmap file"
lines = []
f = open(file_string, 'r')
content = f.read().splitlines()
f.close()

for c in content:
    lines.append(c)

f = open(file_string, 'w')
lines.sort()

for l in lines:
    out_string = l + '\n'
    f.write(out_string)
f.close()'''

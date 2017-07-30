import os
import sys
import shutil
from datetime import datetime
from carmodule import CarInfo

f_in = sys.argv[1] + '/' + sys.argv[2]

f = open(f_in, 'r')
content = f.read().splitlines()
f.close()

lines = []

for c in content:
    lines.append(c.split(" "))

print f_in

lf = lines[0]
ll = lines[-1]

car_id = lf[0]
starttime = lf[1]
long_start = lf[2]
lat_start = lf[3]
stoptime = ll[1]
long_stop = ll[2]
lat_stop = ll[3]
#car_info = CarInfo(car_id, starttime, stoptime, long_start, lat_start, long_stop, lat_stop)

f = open('allvehicles.csv', 'a')
if long_start != long_stop and lat_start != lat_stop:
    out_string = car_id + " " + starttime + " " + stoptime + " " + long_start + " " + lat_start + " " + long_stop + " " + lat_stop + "\n"
    f.write(out_string)

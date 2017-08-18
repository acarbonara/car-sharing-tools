import os
import sys
import itertools
from collections import defaultdict
from math import radians, cos, sin, asin, sqrt
from carmodule import *

# auxiliary function which calculates the distance between two points
# relying to longitude and latitude (the returning result is expressed in meters)
def calculatedistance(lat1, lat2, long1, long2):
    lat1, lat2, long1, long2 = map(radians, [lat1, lat2, long1, long2])
    dlat = lat2 - lat1
    dlong = long2 - long1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
    c = 2 * asin(sqrt(a))
    # 6367 is the Earth radius
    km = 6367 * c
    return abs(float(km*1000))

lines = []
cars = []
T = int(sys.argv[1])
D = int(sys.argv[2])
alpha = float(sys.argv[3])
beta = float(sys.argv[4])
N = int(sys.argv[5])
city_dir = sys.argv[6]


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

# cars.sort(key=lambda c: c.getStartTime(), reverse=True)

starting_cars = len(cars)
print "Starting Cars: ", starting_cars

files = os.listdir(city_dir)
files.sort()
check_file = None

if alpha == beta:
    for fd in files:
        name = os.path.splitext(fd)[0]
        if "matched-cars-final" in name:
            f_s = fd.split("-")
            time = int(f_s[3])
            distance = int(f_s[4])
            n = int(f_s[5])
            if (time <= T or distance <= D) and (n == N):
                f = city_dir + fd
                check_file = open(f, "r")

lines = []
cars_lists = []
print "Checking files between runs"
if check_file is not None:
    content = check_file.read().splitlines()
    check_file.close()
    for c in content:
        if "alpha" not in c:
            lines.append(c.split(" "))

    for l in lines:
        size = int(l[0])
        cars_l = []
        if size == N:
            for i in range(1, len(l)-1):
                cars_l.append(l[i])
        if len(cars_l) > 0:
            cars_lists.append(cars_l)


file_string = "matched-cars-final-" + str(T) + "-" + str(D) + "-" + str(N) + "-" + str(alpha) + "-" + str(beta) + ".csv"
f = open(file_string, "w")
total_matched = 0
for cars_l in cars_lists:
    for c_id in cars_l:
        for car in cars:
            if c_id == car.getCarId():
                cars.remove(car)

for cars_l in cars_lists:
    total_matched += len(cars_l)
    out_string = str(len(cars_l)) + " "
    for c_id in cars_l:
        out_string = out_string + c_id + " "
    out_string += "\n"
    f.write(out_string)
f.close()

print "Preparing time buckets"
cars.sort(key=lambda c: c.getStartTime())
time_buckets = {}
first_time = int(cars[0].getStartTime())
last_time = int(cars[-1].getStopTime())

while first_time <= last_time:
    for car in cars:
        starttime = int(car.getStartTime())
        stoptime = int(car.getStopTime())
        if ((starttime >= first_time - T or starttime >= first_time + T) and (starttime <= first_time + 1800 - T or starttime <= first_time + 1800 + T)) or ((stoptime >= first_time - T or stoptime >= first_time + T) and (stoptime <= first_time + 1800 - T or stoptime <= first_time + 1800 + T)):
            time_buckets.setdefault((first_time, first_time + 1800), []).append(car)
    first_time += 1800

f = open("buckets.txt", "w")
for k, v in time_buckets.items():
    out_string = "Bucket size: " + str(len(v)) + " -> " + str(k) + ":\n"
    f.write(out_string)
    out_string = ""
    for c in v:
        out_string += c.getCarId() + ", "
    out_string += "\n"
    f.write(out_string)
f.close()
print "End time buckets"

u_values_matrix = {}

# matching cars by time and distance limits determined by input params
print "Cars len: ", len(cars)
for cars in time_buckets.values():
    for i in range(len(cars)):
        id_1 = cars[i].getCarId()
        starttime1 = cars[i].getStartTime()
        stoptime1 = cars[i].getStopTime()
        long_start1 = cars[i].getLongStart()
        lat_start1 = cars[i].getLatStart()
        long_stop1 = cars[i].getLongStop()
        lat_stop1 = cars[i].getLatStop()
        for j in range(len(cars)):
            print i, j
            id_2 = cars[j].getCarId()
            starttime2 = cars[j].getStartTime()
            stoptime2 = cars[j].getStopTime()
            long_start2 = cars[j].getLongStart()
            lat_start2 = cars[j].getLatStart()
            long_stop2 = cars[j].getLongStop()
            lat_stop2 = cars[j].getLatStop()
            d_i = calculatedistance(float(lat_start1), float(lat_start2), float(long_start1), float(long_start2))
            d_f = calculatedistance(float(lat_stop1), float(lat_stop2), float(long_stop1), float(long_stop2))
            if id_1 != id_2 and abs(float(starttime1) - float(starttime2)) <= T and abs(float(stoptime1) - float(stoptime2)) <= T and d_i <= D and d_f <= D:
                u = ((d_i / D) * alpha) + ((abs(float(starttime1) - float(starttime2)) / T) * beta)
                e = (id_2, u)
                u_values_matrix.setdefault(id_1, []).append(e)

print "Writing u-values matrix"
f = open("u-values-matrix.txt", "w")
for k, v in u_values_matrix.items():
    print >> f, k, ":", v
f.close()

######################################################################################################################################
##########################################              STARTING FILTER    ###########################################################
######################################################################################################################################
print "Starting matching cars based on u-values"
matched_cars = []
visited = set()
i = 0
for k, v in u_values_matrix.items():
    v.sort(key=lambda e: e[1])
    m_list = []
    print "item: ", i
    if k not in visited:
        m_list.append(k)
        visited.add(k)
        for e in v:
            if e[0] not in visited:
                if len(m_list) < N:
                    m_list.append(e[0])
                    visited.add(e[0])
                else:
                    break
        if len(m_list) > 0:
            matched_cars.append(m_list)
    i += 1
print "matching cars finished"

f = open(file_string, "a")
matched_cars.sort(key=lambda l: len(l), reverse=True)
for l in matched_cars:
    if len(l) > 1:
        total_matched += len(l)
    out_string = str(len(l)) + " "
    for car_id in l:
        out_string = out_string + car_id + " "
    out_string += "\n"
    f.write(out_string)
'''out_string_end = "alpha: " + str(alpha) + " beta: " + str(beta) + " N: " + str(N) + "\n"
f.write(out_string_end)'''
f.close()
final_cars = starting_cars - total_matched

f1 = 'car-pooling-a' + str(alpha) + '-b' + str(beta) + '.dat'
f = open(f1, 'a')
out_string = str(T) + " " + str(D) + " " + str(alpha) + " " + str(beta) + " " + str(N) + " " + str(final_cars) + "\n"
f.write(out_string)
f.close()

script = "mv " + file_string + " " + city_dir
os.system(script)

print "All done!!! Matched:", final_cars

import os
import sys
import shutil
from utility import Util

fstring = sys.argv[1]
method = int(sys.argv[2])

f = open(fstring, 'r')
content = f.read().splitlines()
f.close()

lines = []
infos = []

for c in content:
    lines.append(c.split(" "))

for l in lines:
    time = float(l[0])
    distance = float(l[1])
    alpha = float(l[2])
    beta = float(l[3])
    N = float(l[4])
    finalCars = float(l[5])
    starting_cars = float(l[6])
    info = Util(time, distance, alpha, beta, N, finalCars, starting_cars)
    infos.append(info)

# N variation
if method == 0:
    info_tmp = infos[0]
    n_tmp = info_tmp.getN()
    tuples = []
    cars = info_tmp.getFinalCars()
    count = 1

    for i in range(1, len(infos)):
        if n_tmp == infos[i].getN():
            cars += infos[i].getFinalCars()
            count += 1
        else:
            avg = infos[i].getStartingCars() - (cars / count)
            perc = (avg * 100) / infos[i].getStartingCars()
            tuples.append((n_tmp, perc))
            n_tmp = infos[i].getN()
            cars = infos[i].getFinalCars()
            count = 1

    #last element problem
    info_tmp = infos[-1]
    n_tmp = info_tmp.getN()
    cars = 0
    count = 0

    for i in infos[::-1]:
        if n_tmp == i.getN():
            cars += i.getFinalCars()
            count += 1
        else:
            avg = i.getStartingCars() - (cars / count)
            perc = (avg * 100) / i.getStartingCars()
            tuples.append((n_tmp, perc))
            break

    fstring = fstring.split("-")
    fstring = fstring[3].split("_")
    day_string = fstring[2].replace("/car", "")

    fstring = "car-pooling-N-stats-" + day_string + ".dat"
    f = open(fstring, "w")
    header = '\'' + day_string + '\'\n'
    f.write(header)
    for t in tuples:
        out_string = str(t[0]) + ' ' + str(t[1]) + '\n'
        f.write(out_string)
    f.close()
# time variation
elif method == 1:
    infos.sort(key=lambda i: i.getTime())
    info_tmp = infos[0]
    t_tmp = info_tmp.getTime()
    tuples = []
    cars = info_tmp.getFinalCars()
    count = 1

    for i in range(1, len(infos)):
        if t_tmp == infos[i].getTime():
            cars += infos[i].getFinalCars()
            count += 1
        else:
            avg = infos[i].getStartingCars() - (cars / count)
            perc = (avg * 100) / infos[i].getStartingCars()
            tuples.append((t_tmp, perc))
            t_tmp = infos[i].getTime()
            cars = infos[i].getFinalCars()
            count = 1

    #last element problem
    info_tmp = infos[-1]
    t_tmp = info_tmp.getTime()
    cars = 0
    count = 0

    for i in infos[::-1]:
        if t_tmp == i.getTime():
            cars += i.getFinalCars()
            count += 1
        else:
            avg = i.getStartingCars() - (cars / count)
            perc = (avg * 100) / i.getStartingCars()
            tuples.append((t_tmp, perc))
            break

    fstring = fstring.split("-")
    fstring = fstring[3].split("_")
    day_string = fstring[2].replace("/car", "")

    fstring = "car-pooling-T-stats-" + day_string + ".dat"
    f = open(fstring, "w")
    header = '\'' + day_string + '\'\n'
    f.write(header)
    for t in tuples:
        out_string = str(t[0]) + ' ' + str(t[1]) + '\n'
        f.write(out_string)
    f.close()
# distance variation
elif method == 2:
    infos.sort(key=lambda i: i.getDistance())
    info_tmp = infos[0]
    d_tmp = info_tmp.getDistance()
    tuples = []
    cars = info_tmp.getFinalCars()
    count = 1

    for i in range(1, len(infos)):
        if d_tmp == infos[i].getDistance():
            cars += infos[i].getFinalCars()
            count += 1
        else:
            avg = infos[i].getStartingCars() - (cars / count)
            perc = (avg * 100) / infos[i].getStartingCars()
            tuples.append((d_tmp, perc))
            d_tmp = infos[i].getDistance()
            cars = infos[i].getFinalCars()
            count = 1

    #last element problem
    info_tmp = infos[-1]
    d_tmp = info_tmp.getDistance()
    cars = 0
    count = 0

    for i in infos[::-1]:
        if d_tmp == i.getDistance():
            cars += i.getFinalCars()
            count += 1
        else:
            avg = i.getStartingCars() - (cars / count)
            perc = (avg * 100) / i.getStartingCars()
            tuples.append((d_tmp, perc))
            break

    fstring = fstring.split("-")
    fstring = fstring[3].split("_")
    day_string = fstring[2].replace("/car", "")

    fstring = "car-pooling-D-stats-" + day_string + ".dat"
    f = open(fstring, "w")
    header = '\'' + day_string + '\'\n'
    f.write(header)
    for t in tuples:
        out_string = str(t[0]) + ' ' + str(t[1]) + '\n'
        f.write(out_string)
    f.close()
# alpha/beta variation
elif method == 3:
    #infos.sort(key=lambda i: (i.getAlpha(), i.getBeta()))
    info_tmp = infos[0]
    alpha_tmp = info_tmp.getAlpha()
    beta_tmp = info_tmp.getBeta()
    tuples = []
    cars = info_tmp.getFinalCars()
    count = 1

    for i in range(1, len(infos)):
        if alpha_tmp == infos[i].getAlpha() and beta_tmp == infos[i].getBeta():
            cars += infos[i].getFinalCars()
            count += 1
        else:
            avg = infos[i].getStartingCars() - (cars / count)
            perc = (avg * 100) / infos[i].getStartingCars()
            tuples.append((alpha_tmp, beta_tmp, perc))
            alpha_tmp = infos[i].getAlpha()
            beta_tmp = infos[i].getBeta()
            cars = infos[i].getFinalCars()
            count = 1

    #last element problem
    info_tmp = infos[-1]
    alpha_tmp = info_tmp.getAlpha()
    beta_tmp = info_tmp.getBeta()
    cars = 0
    count = 0

    for i in infos[::-1]:
        if alpha_tmp == i.getAlpha() and beta_tmp == i.getBeta():
            cars += i.getFinalCars()
            count += 1
        else:
            avg = i.getStartingCars() - (cars / count)
            perc = (avg * 100) / i.getStartingCars()
            tuples.append((alpha_tmp, beta_tmp, perc))
            break

    fstring = fstring.split("-")
    fstring = fstring[3].split("_")
    day_string = fstring[2].replace("/car", "")

    fstring = "car-pooling-a-b-stats-" + day_string + ".dat"
    f = open(fstring, "w")
    header = '\'' + day_string + '\'\n'
    f.write(header)
    for t in tuples:
        out_string = str(t[0]) + ' ' + str(t[1]) + ' ' + str(t[2] )+ '\n'
        f.write(out_string)
    f.close()
# beta variation
'''elif method == 4:
    infos.sort(key=lambda i: i.getBeta())
    info_tmp = infos[0]
    beta_tmp = info_tmp.getBeta()
    tuples = []
    cars = info_tmp.getFinalCars()
    count = 1

    for i in range(1, len(infos)):
        if beta_tmp == infos[i].getBeta():
            cars += infos[i].getFinalCars()
            count += 1
        else:
            avg = 51900 - (cars / count)
            perc = (avg * 100) / 51900
            tuples.append((beta_tmp, perc))
            beta_tmp = infos[i].getBeta()
            cars = infos[i].getFinalCars()
            count = 1

    #last element problem
    info_tmp = infos[-1]
    beta_tmp = info_tmp.getBeta()
    cars = 0
    count = 0

    for i in infos[::-1]:
        if beta_tmp == i.getBeta():
            cars += i.getFinalCars()
            count += 1
        else:
            avg = 51900 - (cars / count)
            perc = (avg * 100) / 51900
            tuples.append((beta_tmp, perc))
            break

    fstring = fstring.split("-")
    fstring = fstring[3].split("_")
    day_string = fstring[2].replace("/car", "")

    fstring = "car-pooling-b-stats-" + day_string + ".dat"
    f = open(fstring, "w")
    header = '\'' + day_string + '\'\n'
    f.write(header)
    for t in tuples:
        out_string = str(t[0]) + ' ' + str(t[1]) + '\n'
        f.write(out_string)
    f.close()'''

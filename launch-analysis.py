import os
import sys
import shutil

t = [600,900,1800]
d = [300,400,500,1000]
N = 5
#N = [5, 10, 15, 20, 25, 30]
alpha = 0.5
beta = 0.5
#alpha = [0.25, 0.50, 1.0]
#beta = [0.25, 0.50, 1.0]

city = sys.argv[1]

for i in range(len(t)):
    for j in range(len(d)):
        city_dir = "matched-cars-final-" + city + "/"
        if not os.path.exists(city_dir):
            os.makedirs(city_dir)
        script = 'python car-analysis.py ' + str(t[i]) + ' ' + str(d[j]) + ' ' + str(alpha) + ' ' + str(beta) + ' ' + str(N) + ' ' + city_dir
        os.system(script)

script = 'mv *.dat ' + city_dir
os.system(script)

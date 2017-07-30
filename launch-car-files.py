import os
import sys
import shutil

# checking input params
if len(sys.argv) != 2:
    err_string = "You have to specify only the CITY_DIR"
    print err_string
    sys.exit()

CITY_DIR = sys.argv[1]

files = os.listdir(CITY_DIR)

# launching 'car-writer' script for every file contained into CITY_DIR
for f in files:
    script = 'python car-writer.py ' + CITY_DIR + ' ' + f
    os.system(script)

print "All done... car-matched.csv writed"

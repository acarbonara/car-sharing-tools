#!/bin/bash

#rm *.dat
rm allvehicles.csv

python launch-car-files.py ${1}

python launch-analysis.py ${1}

#!/usr/bin/python
import numpy
import math
import sys
import xml.etree.ElementTree as ET

numTilesx = 200
numTilesy = numTilesx

print "Opening file for tiling"
ff = open(sys.argv[1],'r')
minX = sys.maxint
maxX = -sys.maxint -1
minY = sys.maxint
maxY = -sys.maxint -1
for line in ff.readlines():
	x = float(line.split(' ')[0])
	y = float(line.split(' ')[1])
	if x < minX:
		minX = x
	if x > maxX:
		maxX = x
	if y < minY:
		minY = y
	if y > maxY:
		maxY = y

print minX, maxX, minY, maxY

deltax = (maxX - minX)/numTilesx
deltay = (maxY - minY)/numTilesy
grid = numpy.zeros((numTilesx+1,numTilesy+1))
counter = numpy.zeros((numTilesx+1,numTilesy+1))


print deltax, deltay, counter

for i in range(numTilesx):
	for j in range(numTilesy):
		grid[i][j] = 0

ff.close()
ff = open(sys.argv[1],'r')
for line in ff.readlines():
	x = float(line.split(' ')[0])
	y = float(line.split(' ')[1])
	c = float(line.split(' ')[2])

	nx = int((x-minX)/deltax)
	ny = int((y-minY)/deltay)

	grid[nx][ny] = grid[nx][ny] + c
	counter[nx][ny] = counter[nx][ny] + 1

ff.close()

ff = open(sys.argv[1],"w")
for i in range(numTilesx):
	for j in range(numTilesy):
		if counter[i][j] > 0:
			ff.write(str(i * deltax + minX) + " " + str(j * deltay + minY) + " " + str((grid[i][j] * 1.0)) + "\n")
        #else:
        #    ff.write(str(i * deltax + minX) + " " + str(j * deltay + minY) + " " + str(40) + "\n")

ff.close()

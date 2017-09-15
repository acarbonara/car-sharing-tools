class Util:
    def __init__(self, time, distance, alpha, beta, N, finalCars, startingCars):
        self.time = time
        self.distance = distance
        self.alpha = alpha
        self.beta = beta
        self.N = N
        self.finalCars = finalCars
        self.startingCars = startingCars

    def getTime(self):
        return self.time

    def getDistance(self):
        return self.distance

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

    def getN(self):
        return self.N

    def getFinalCars(self):
        return self.finalCars

    def getStartingCars(self):
        return self.startingCars

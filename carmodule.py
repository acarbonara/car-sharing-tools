class CarInfo:
    def __init__(self, car_id, starttime, stoptime, long_start, lat_start, long_stop, lat_stop):
        self.car_id = car_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.long_start = long_start
        self.lat_start = lat_start
        self.long_stop = long_stop
        self.lat_stop = lat_stop

    def getCarId(self):
        return self.car_id

    def getStartTime(self):
        return self.starttime

    def getStopTime(self):
        return self.stoptime

    def getLongStart(self):
        return self.long_start

    def getLatStart(self):
        return self.lat_start

    def getLongStop(self):
        return self.long_stop

    def getLatStop(self):
        return self.lat_stop

class CarOccurrence:
    def __init__(self, car_id, occurrences):
        self.car_id = car_id
        self.occurrences = occurrences

    def getCarId(self):
        return self.car_id

    def getOccurrences(self):
        return self.occurrences

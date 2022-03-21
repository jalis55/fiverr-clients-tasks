import random as r


class Train:
    def __init__(self, name, station, color, direction):
        self.name = str(name)
        self.color = color
        self.station = station
        self.direction = direction

    def __str__(self):
        return "Train " + self.name + " on " + self.color + " line is at station " + self.station.name + " heading " + self.direction

    def delay(self):
        if r.random() <= self.station.p:
            return True
        else:
            return False


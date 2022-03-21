class Connection:
    def __init__(self, from_station, to_station, color, direction):
        self.from_station = from_station
        self.to_station = to_station
        self.color = color
        self.direction = direction

    def __str__(self):
        return self.from_station.name + " " + self.to_station.name + " " + self.color + " " + self.direction

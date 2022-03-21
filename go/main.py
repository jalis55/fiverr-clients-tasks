from Train import *
from Station import *
from Connection import *
import random as r


def read_indata(f):
    objects = []
    with open(f, "r", encoding="utf-8") as data:
        for line in data:
            line = line.split(",")
            foo = Station(*line)
            objects.append(foo)
    return objects


def make_graph(stations, f):
    with open(f, "r", encoding="utf-8") as data:
        for line in data:
            line = line.split(",")
            for station in stations:
                if station.name == line[0]:
                    from_station = station
            for station in stations:
                if station.name == line[1]:
                    if line[3].strip() == "S":
                        from_station.connections.append(Connection(from_station, station, line[2], "S"))
                    else:
                        from_station.connections.append(Connection(from_station, station, line[2], "N"))


def spawn_trains(n, stations):
    colors = set()                   # make it a set so we don't get duplicates.
    for station in stations:
        for conn in station.connections:
            colors.add(conn.color)
    trains = []
    while len(trains) <= n - 1:
        random_station = r.sample(stations, 1)[0]
        try:
            random_connection = r.sample(random_station.connections, 1)[0]
            trains.append(Train(len(trains) + 1, random_station, random_connection.color, random_connection.direction))
        except ValueError:
            pass
    return trains


def simulation(trains):
    for train in trains:
        for conn in train.station.connections:
            if conn.color == train.color:
                train.station = conn.to_station
            if len(train.station.connections) == 0:
                train.direction = "N"


def train_info(choice, trains):
    if trains[choice - 1].delay():
        print(trains[choice - 1], "(DELAY)")
    else:
        print(trains[choice - 1])


def main():

    # stations_file = input("Enter the name of station file: ")
    # connections_file = input("Enter the name of connections file: ")
    # n_trains = int(input("Enter the number of simulated trains: "))

    stations = read_indata("stations.txt")
    make_graph(stations, "connections.txt")
    trains = spawn_trains(3, stations)

    menu = True

    while menu:
        print("Continue simulation [1], train info [2], exit [3].")
        user_input = input("Select an option: ")
        if user_input == "1":
            simulation(trains)
        elif user_input == "2":
            choice = int(input("Which train [1 - 3]: "))
            train_info(choice, trains)
        elif user_input == "3":
            break


main()

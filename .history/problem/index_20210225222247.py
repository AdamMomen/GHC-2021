from collections import defaultdict


class Street:
    intersections = defaultdict(list)
    street_scores = {}

    def __init__(self, line):
        parameters = line.strip().split()
        self.start = int(parameters[0])
        self.end = int(parameters[1])
        self.name = parameters[2]
        self.length = int(parameters[3])
        Street.intersections[self.end].append(self.name)
        Street.street_scores[self.name] = 0

    def __repr__(self):
        return f"{self.name}\t Start: {self.start}, End: {self.end}, Length: {self.length}\n"


class Car:
    def __init__(self, line):
        self.nb_of_roads = line.strip().split()[0]
        self.path = line.strip().split()[1:]

    def __repr__(self):
        return f"Car with {self.nb_of_roads} roads\n"

    def drive(self, cars_list):
        for car in cars_list:
            for road in car.path:
                if road in Street.street_scores:
                    Street.street_scores[road] += 1


class Simulation:
    def __init__(self, cars, streets, duration, bonus, intersections):
        self.cars = cars
        self.street = streets
        self.duration = duration
        self.bonus = bonus
        self.intersections = intersections

    def sort_cars(self):
        pass

    def begin_simulation(self):
        for i in range(self.duration):
            pass


def exportFile(intersections, fileName):
    lines = []
    for intersectionId, streetNames in intersections.items():
        for street in streetNames:
            if Street.street_scores[street] == 0:
                streetNames.remove(street)

    lines.append(f"{len(intersections)}\n")
    for intersectionId, streetNames in intersections.items():
        lines.append(f"{intersectionId}\n")
        lines.append(f"{len(streetNames)}\n")
        for street in streetNames:
            lines.append(f"{street} 2\n")
    lines[-1] = lines[-1].replace("\n", "")

    with open(fileName, "w") as f:
        f.writelines(lines)


def importFile(filename):
    carsList = []
    streetList = []
    duration = 0
    intersections = 0
    streets = 0
    vehicles = 0
    bonus_points = 0

    with open(filename, "r") as f:
        line = f.readline()
        parameters = line.strip().split()
        duration = int(parameters[0])
        intersections = int(parameters[1])
        streets = int(parameters[2])
        vehicles = int(parameters[3])
        bonus_points = int(parameters[4])

        for x in range(streets):
            streetList.append(Street(f.readline()))

        for y in range(vehicles):
            carsList.append(Car(f.readline()))
    #print(carsList, streetList)
    # print(Street.intersections)


def process(file):
    importFile(file+".txt")
    exportFile(Street.intersections, file+".out")
    Street.intersections = defaultdict(list)


if __name__ == "__main__":
    files = ["a", "b", "c", "d", "e", "f"]
    for file in files:
        process(file)

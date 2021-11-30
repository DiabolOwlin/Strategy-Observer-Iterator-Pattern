import math
from Strategy import *
from Iterator import *


class Unit(ABC):
    @abstractmethod
    def make_alert(self):
        pass


class SKKM:
    def __init__(self):
        self.fire_service_units = set()
        self.nearest_unit = None
        self.list_of_occasions = []

    def attach(self, unit):
        self.fire_service_units.add(unit)

    def detach(self, unit):
        self.fire_service_units.remove(unit)

    def sort_from_nearest_to_farthest(self, problem_x_coord, problem_y_coord):
        distance_dict = {}
        for unit in self.fire_service_units:
            distance = math.sqrt(
                ((problem_x_coord - unit.coordinates[0]) ** 2) + ((problem_y_coord - unit.coordinates[1]) ** 2))
            distance_dict[unit] = distance

        sorted_distance_dict = sorted(distance_dict.items(), key=lambda item: item[1])
        self.nearest_unit = (sorted_distance_dict[0])[0]

    def notify(self):
        for unit in self.fire_service_units:
            if unit.fire_station_id == self.nearest_unit:
                unit.make_alert()


class FireServiceUnit(Unit):
    def __init__(self, fire_station_id, coordinates, list_of_vehicles: list):
        self.fire_station_id = fire_station_id
        self.coordinates = coordinates
        self.vehicles = list_of_vehicles

    def __iter__(self):
        return Iterator(self.vehicles)

    def make_alert(self):
        print(f"{self.fire_station_id} was alerted of new accident.")

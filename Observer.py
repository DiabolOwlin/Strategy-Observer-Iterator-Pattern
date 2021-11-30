import math
from abc import ABC, abstractmethod
from State import FreeState, OccupiedState
from Iterator import *
from Strategy import *


#
#
# class CameraSystem:
#     def __init__(self):
#         self.__observers = set()
#
#     def attach(self, observer):
#         self.__observers.add(observer)
#
#     def detach(self, observer):
#         self.__observers.remove(observer)
#
#     def notify(self):
#         for observer in self.__observers:
#             observer.make_photo()
#
#

class Unit(ABC):
    @abstractmethod
    def make_alert(self):
        pass


#
# class Camera(AbstractObserver):
#     def __init__(self, name):
#         self.name = name
#
#     def make_photo(self):
#         print('{} makes a photo'.format(self.name))

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
        # for unit in self.__fire_service_units:
        #     if unit.fire_station_id == self.nearest_unit:
        #         vehicles_needed = 0
        #         it = Iterator(unit.vehicles)
        #         if vehicles_needed < 3:
        #             car = next(it)
        #             if car is FreeState:
        #                 car.change_state(OccupiedState)
        #                 vehicles_needed += 1
    # def check_time(self):
    #     for unit in self.fire_service_units:
    #         for vehicle in unit.vehilces:
    #             if vehicle.


class FireServiceUnit(Unit):
    def __init__(self, fire_station_id, coordinates, list_of_vehicles: list):
        self.fire_station_id = fire_station_id
        self.coordinates = coordinates
        self.vehicles = list_of_vehicles

    # def show_coordinates(self):
    #     print("___________________________\n"
    #           "Coordinates of the station {}:\nX: {}, Y: {}"
    #           "\n___________________________"
    #           .format(self.fire_station_id, self.coordinates[0], self.coordinates[1]))

    def make_alert(self):
        print(f"{self.fire_station_id} została poinformowana o nowym przypadku.")






from abc import abstractmethod, ABC

from State import *


class BaseProblem(ABC):  # Strategy interface

    @abstractmethod
    def do_work(self, fire_station, number_of_vehicles_needed, problem_id):
        pass


class FireProblem(BaseProblem):
    def __init__(self, vehicle_id_1=None, vehicle_id_2=None, vehicle_id_3=None):
        self.vehicle_id_1 = vehicle_id_1
        self.vehicle_id_2 = vehicle_id_2
        self.vehicle_id_3 = vehicle_id_3

    def do_work(self, fire_station, number_of_vehicles_needed, problem_id):
        print("Problem needs 3 vehicles!")
        counter = 0
        # print('here at do_work_local')
        for element in fire_station.vehicles:
            if counter == number_of_vehicles_needed:
                break
            if type(element._state) is FreeState:
                element.change_state(OccupiedState())
                counter += 1
        # print(counter)
        print(f"{counter} vehicles from {fire_station.fire_station_id}"
              f" are on the way on the site with problem number {problem_id}")

        diff = number_of_vehicles_needed - counter
        return diff


class LocalThreadProblem(BaseProblem):
    def __init__(self, vehicle_id_1=None, vehicle_id_2=None):
        self.vehicle_id_1 = vehicle_id_1
        self.vehicle_id_2 = vehicle_id_2

    def do_work(self, fire_station, number_of_vehicles_needed, problem_id):
        print("Problem needs 2 vehicles!")
        counter = 0
        # print('here at do_work_local')
        for element in fire_station.vehicles:
            if counter == number_of_vehicles_needed:
                break
            if type(element._state) is FreeState:
                element.change_state(OccupiedState())
                counter += 1
        # if counter >= number_of_vehicles_needed:
        print(f"{counter} vehicles from {fire_station.fire_station_id}"
              f" are on the way on the site with problem number {problem_id}")

        diff = number_of_vehicles_needed - counter
        return diff


class Problem:
    def __init__(self, x_coord, y_coord, problem_id):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.problem_id = problem_id
        self.strategy = None

    def set_strategy(self, strategy: BaseProblem):
        self.strategy = strategy

    def solve(self, fire_station_id, number_of_vehicles_needed, problem_id):
        diff = self.strategy.do_work(fire_station_id, number_of_vehicles_needed, problem_id)
        return diff
        # print(
        #     f'{number_of_vehicles_needed} vehicles is on the way to the site with coords {self.x_coord}, {self.y_coord}')

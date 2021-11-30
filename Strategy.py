import random
import time
from abc import ABC

from State import *


class BaseProblem(ABC):  # Strategy interface

    @abstractmethod
    def do_work(self, fire_station, number_of_vehicles_needed, problem_id, attached_vehicles_id):
        pass


class FireProblem(BaseProblem):

    def do_work(self, fire_station, number_of_vehicles_needed, problem_id, attached_vehicles_id):

        counter = 0

        for element in fire_station.vehicles:
            if counter == number_of_vehicles_needed:
                break
            if type(element._state) is FreeState:
                element.change_state(OccupiedState())
                attached_vehicles_id.append(element)
                counter += 1

        if counter != 0:
            print(f"New! {counter} vehicles from {fire_station.fire_station_id}"
                  f" are on the way on the site with problem #{problem_id}")

        diff = number_of_vehicles_needed - counter
        return diff


class LocalThreadProblem(BaseProblem):

    def do_work(self, fire_station, number_of_vehicles_needed, problem_id, attached_vehicles_id):

        counter = 0

        for element in fire_station.vehicles:
            if counter == number_of_vehicles_needed:
                break
            if type(element._state) is FreeState:
                element.change_state(OccupiedState())
                attached_vehicles_id.append(element)
                counter += 1

        if counter != 0:
            print(f"New! {counter} vehicles from {fire_station.fire_station_id}"
                  f" are on the way on the site with problem #{problem_id}")

        diff = number_of_vehicles_needed - counter

        return diff


class Problem:
    def __init__(self, x_coord, y_coord, problem_id):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.problem_id = problem_id
        self.strategy = None
        self.attached_vehicles_id = []
        self.start_time = time.process_time()

        self.path_time = random.randint(0, 4)
        self.solve_time = random.randint(5, 26)

        self.is_fake = False
        is_fake = random.randint(1, 21)
        if is_fake == 1:
            self.is_fake = True
            self.solve_time = 0

        self.solve_progress = 1
        # path_time = random.randint(0, 4)
        # solve_time = random.randint(5, 26)
        # self.diff_time = 2 * path_time + solve_time
        #
        # self.is_fake = False
        # is_fake = random.randint(1, 21)
        # if is_fake == 1:
        #     self.is_fake = True
        #     self.diff_time = 2 * path_time


    def set_strategy(self, strategy: BaseProblem):
        self.strategy = strategy

    def solve(self, fire_station_id, number_of_vehicles_needed, problem_id, attached_vehicles_id):
        diff = self.strategy.do_work(fire_station_id, number_of_vehicles_needed, problem_id, attached_vehicles_id)
        return diff

    def check_time(self):
        # print("here i am")
        if self.solve_progress == 1:
            # print("I`m here in check_time_part_1")
            if time.process_time() - self.start_time >= self.path_time:
                print(f"---->Vehicles has arrived on the site of the problem #{self.problem_id}.")
                self.solve_progress = 2

        elif self.solve_progress == 2:
            # print("I`m here in check_time_part_2")
            if self.is_fake == 1:
                print(f'---->Nothing is happening. Fortunately, problem #{self.problem_id} is fake.')
                self.solve_progress = 3
            else:
                if time.process_time() - (self.start_time + self.path_time) >= self.solve_time:
                    print(f"---->Our units successfully dealt with the problem #{self.problem_id}")
                    self.solve_progress = 3

        elif self.solve_progress == 3:
            # print("I`m here in check_time_part_3")
            if time.process_time() - (self.start_time + self.path_time + self.solve_time) >= self.path_time:
                print(f"---->Vehicles has returned from the problem #{self.problem_id} at their disposal.")
                for vehicle in self.attached_vehicles_id:
                    vehicle.change_state(FreeState())

                return True
        return False

        # if time.process_time() - self.start_time >= self.diff_time:
        #     for vehicle in attached_vehicles_id:
        #         vehicle.change_state(FreeState())



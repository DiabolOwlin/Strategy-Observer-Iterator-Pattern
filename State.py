from abc import ABCMeta, abstractmethod


class VehicleState(metaclass=ABCMeta):

    @abstractmethod
    def move_to_the_site(self) -> str:
        pass


class FreeState(VehicleState):
    def __init__(self):
        self.problem_id = None

    def move_to_the_site(self) -> str:
        return 'is free now'


class OccupiedState(VehicleState):
    def __init__(self, problem_id=None):
        self.problem_id = problem_id

    def move_to_the_site(self) -> str:
        return f'is dealing with problem {self.problem_id} already, so you can`t use it'


class FireFighterVehicle:

    def __init__(self, state: VehicleState) -> None:
        self._state = state
        # self._fire_station = fire_station_id  # id of the station which vehicle belongs to
        # self._problemID = problem_id  # id of the problem that this vehicle was sent to deal with

    def change_state(self, state: VehicleState) -> None:
        self._state = state

    def move_to_the_site(self) -> None:
        self._execute('move_to_the_site')

    def _execute(self, operation: str) -> None:
        try:
            func = getattr(self._state, operation)
            print(func)
            print('Vehicle {}.'.format(func()))
        except AttributeError:
            print('Vehicle can`t do it.')


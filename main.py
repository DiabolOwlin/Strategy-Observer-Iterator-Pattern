# import random
# import time
# from State import *
# from Strategy import *
# import time
import sys

from Observer import *
from threading import Timer

running = True


# list_of_occasions = []

# cam1 = Camera('Cam #1')
# cam2 = Camera('Cam #2')
# cam3 = Camera('Cam #3')
#
#
# cam_system = CameraSystem()
#
# cam_system.attach(cam1)
# cam_system.attach(cam2)
# cam_system.attach(cam3)
#
# cam_system.notify()

# class StateFireServiceUnit:
#     def __init__(self, x_coord, y_coord):
#         self.x_coord = x_coord
#         self.y_coord = y_coord
#
#         self.__vehicles


# class FireServiceUnit:
#     def __init__(self, fire_station_id, coordinates, list_of_vehicles: list):
#         self.fire_station_id = fire_station_id
#         self.coordinates = coordinates
#         self.vehicles = list_of_vehicles
#
#     def show_coordinates(self):
#         print("___________________________\n"
#               "Coordinates of the station {}:\nX: {}, Y: {}"
#               "\n___________________________"
#               .format(self.fire_station_id, self.coordinates[0], self.coordinates[1]))

# def show_stats(fsu):
#     for unit in fsu.fire_service_units:
#         print(unit.fire_station_id)
#         for element in unit.vehicles:
#             print(element._state)
#         print('---------------------------------------------')


def generate_occasion():
    global running
    try:
        problem_id = random.randint(1, 1001)
        if random.randint(1, 11) < 4:

            tmp = Problem(random.uniform(50.15456401334173, 49.95855025648944),
                          random.uniform(19.68829248274239, 20.0247027586890), problem_id)
            tmp.set_strategy(FireProblem())

            number = 3
        else:

            tmp = Problem(random.uniform(50.15456401334173, 49.95855025648944),
                          random.uniform(19.68829248274239, 20.0247027586890), problem_id)
            tmp.set_strategy(LocalThreadProblem())

            number = 2

        National_Fire_Service.list_of_occasions.append(tmp)
        National_Fire_Service.sort_from_nearest_to_farthest(tmp.x_coord, tmp.y_coord)
        National_Fire_Service.notify()
        diff = tmp.solve(National_Fire_Service.nearest_unit, number, problem_id, tmp.attached_vehicles_id)
        if diff != 0:
            dismiss_list = []
            while diff != 0:
                n = diff
                dismiss_list.append(National_Fire_Service.nearest_unit)

                National_Fire_Service.detach(National_Fire_Service.nearest_unit)

                National_Fire_Service.sort_from_nearest_to_farthest(tmp.x_coord, tmp.y_coord)

                National_Fire_Service.notify()

                diff = tmp.solve(National_Fire_Service.nearest_unit, n, problem_id, tmp.attached_vehicles_id)
            for el in dismiss_list:
                National_Fire_Service.attach(el)
    except IndexError:
        print(
            "\n\n\n==========We cannot handle so many accidents! We need HELP ASAP!!!!==========\n\n\n")
        running = False
        sys.exit(1)

    # National_Fire_Service.check_time()
    # show_stats(National_Fire_Service)
    # print("========================================================================================")

    # if random.randint(1, 21) == 1:
    #     print("Alert is fake!")
    # else:
    #     print("Alert is not fake!")
    #     print("Alert is not fake!")
    #     print("Alert is not fake!")
    #     print("Alert is not fake!")
    #     print("Alert is not fake!")

    random_time_generation = random.randint(3, 16)
    Timer(random_time_generation, generate_occasion).start()


if __name__ == '__main__':
    free = FreeState()
    occupied = OccupiedState()

    FSU1 = FireServiceUnit('JRG-1', (50.060018243005125, 19.943072222897737),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU2 = FireServiceUnit('JRG-2', (50.03344864229099, 19.935874969834686),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU3 = FireServiceUnit('JRG-3', (50.075734877638816, 19.887319816655477),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU4 = FireServiceUnit('JRG-4', (50.09227447039893, 19.922143717582486),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU5 = FireServiceUnit('JRG-5', (50.03778720217305, 20.005776297146628),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU6 = FireServiceUnit('JRG-6', (50.01660583392493, 20.015535970527537),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU7 = FireServiceUnit('JRG-7', (50.09416504223102, 19.977369624577882),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU8 = FireServiceUnit('JRG SA', (50.07710568530913, 20.032666112621154),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU9 = FireServiceUnit('JRG Skawina', (49.96839555246994, 19.79950743685496),
                           [FireFighterVehicle(free) for _ in range(5)])
    FSU10 = FireServiceUnit('LSP Lotnisko Balice', (50.07327154994574, 19.785872680169714),
                            [FireFighterVehicle(free) for _ in range(5)])

    National_Fire_Service = SKKM()
    National_Fire_Service.attach(FSU1)
    National_Fire_Service.attach(FSU2)
    National_Fire_Service.attach(FSU3)
    National_Fire_Service.attach(FSU4)
    National_Fire_Service.attach(FSU5)
    National_Fire_Service.attach(FSU6)
    National_Fire_Service.attach(FSU7)
    National_Fire_Service.attach(FSU8)
    National_Fire_Service.attach(FSU9)
    National_Fire_Service.attach(FSU10)

    # National_Fire_Service.message_to_all()
    generate_occasion()
    while running:
        # print("here")
        for element in National_Fire_Service.list_of_occasions:
            # print(element.attached_vehicles_id)

            finish = element.check_time()
            if finish:
                National_Fire_Service.list_of_occasions.remove(element)
            # Timer(0.05, element.check_time(element.attached_vehicles_id)).start()
        # print("Length of list_of_occasions:", len(National_Fire_Service.list_of_occasions))
    sys.exit(1)
    # JRG-1 : 50.060018243005125, 19.943072222897737
    # JRG-2 : 50.03344864229099, 19.935874969834686
    # JRG-3 : 50.075734877638816, 19.887319816655477
    # JRG-4 : 50.09227447039893, 19.922143717582486
    # JRG-5 : 50.03778720217305, 20.005776297146628
    # JRG-6 : 50.01660583392493, 20.015535970527537
    # JRG-7 : 50.09416504223102, 19.977369624577882
    # JRG SA : 50.07710568530913, 20.032666112621154
    # JRG Skawina: 49.96839555246994, 19.79950743685496
    # LSP Lotnisko Balice: 50.07327154994574, 19.785872680169714

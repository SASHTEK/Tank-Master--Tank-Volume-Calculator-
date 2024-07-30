import math
from colorama import init
import datetime

class FuelBalanceChecker:
    def __init__(self, tank_radius=1.06, tank_length=2.7):
        self.tank_radius = tank_radius
        self.tank_length = tank_length
        self.tank_capacity = round((math.pi * self.tank_radius ** 2 * self.tank_length)*1000, 2)
        init()

    def get_pole_mark(self):
        while True:
            try:
                pole_mark = float(input("> Please feed Pole Mark: "))
                print(" ")
                if pole_mark > self.tank_radius * 2:
                    print('\033[33m' + "Wrong input. Please check the Pole Mark again!" + '\033[0m')
                    print(" ")
                else:
                    return pole_mark
            except:
                print('\033[31m' + "Please enter a valid number" + '\033[0m')
                print(" ")

    def calculate_fuel_balance(self, pole_mark):
        r = self.tank_radius
        l = self.tank_length
        p = pole_mark

        available_fuel_liters = ((math.pi * r ** 2 - r ** 2 * math.acos((r - p)/r) + (r-p) * math.sqrt(2*r*p - p ** 2)) * l) * 1000

        if available_fuel_liters > self.tank_capacity:
            print('\033[33m' + "Please check the Pole Mark again!" + '\033[0m')
            print(" ")
        else:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print('\033[32m' + ">> Available fuel balance in the tank is approximately", round(available_fuel_liters, 2), "liters" + '\033[0m')
            print(">> ",formatted_time)
            print(" ")

    def run(self):
        print("TankMaster")
        print("Default Tank Size - Width",self.tank_radius*2,"m, Length ",self.tank_length,"m")
        print("Tank Capacity approx. ",self.tank_capacity, "Ltrs.")
        print(" ")
        print("Please feed all values in Miters (m)")
        print(" ")
        print("-"*3)
        print(" ")
        while True:
            user_input = input("Enter 'q' to quit or any other key to continue: ")
            if user_input.lower() == 'q':
                break
            pole_mark = self.get_pole_mark()
            self.calculate_fuel_balance(pole_mark)
            print("---")
            print(" ")

if __name__ == "__main__":
    checker = FuelBalanceChecker()
    checker.run()


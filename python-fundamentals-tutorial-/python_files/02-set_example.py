'''
Example problem set for the set module
'''

"""
CAR CRASH! There has been a accident and EMS are 
asking you to see which cars from what road have crashed and where they have crashed, so
they can better assess what has happened.
"""

import random

class Crash():
    """
    This class will hold all of the functions pertaining to a crash that could
    happen at any 2 roads.
    """

    def __init__(self):
        """
        Intializes the roads to be used and the set of cars involved in the crash
        """
        self.road_1 = " "
        self.road_2 = " "
        self.crashed_cars_road_1 = set()
        self.crashed_cars_road_2 = set()
    def calling_ems(self):
        """
        This is when you see the accident and are calling in to tell dispatch on what
        happened. They will ask you a series of questions that will include giving the roads
        the accident occurred on, and what vehicles were involved in the crash. They will 
        ask which cars are on the first road, and what cars are in the intersection, if there
        are any. They will then ask you to combine both lists to get an accurate count to see
        how much help should be sent.
        """
        print("Thank you for calling EMS Services! We heard you have seen a crash and we just have a few questions for you.")
        self.ems_questions_and_answers()
        self.ems_situation_assessment()
    def intersection(self):
        """
        This function is to calculate what cars are in the intersection.
        """
        return self.crashed_cars_road_1 & self.crashed_cars_road_2
    def combine_sets(self):
        """
        This function will have you combine the two sets, elimanting the duplicates(hint: using the
        union functionality.).
        """
        return self.crashed_cars_road_1 | self.crashed_cars_road_2
    def ems_questions_and_answers(self):
        """
        Series of questions that EMS will ask everytime a crash is reported. The user calling in will give
        their answers as well.
        """
        #Gets the roads for where the accident occurred
        self.road_1 = input("What is the name of one of the roads involved in the accident? ")
        print()
        self.road_2 = input("What is the name other road that was involved? ")
        print()

        #Iterates through how many cars have crashed and asks about each vehicle and adds it to the corresponding set
        num_cars_crashed_r_1 = int(input("How many cars have crashed on the first road mentioned? "))
        for c in range(0, num_cars_crashed_r_1):
            car = input("What kind of car is in the accident? ")

            self.crashed_cars_road_1.add(car)
        print()

        #Iterates through how many cars have crashed and asks about each vehicle and adds it to the corresponding set
        num_cars_crashed_r_2 = int(input("How many cars have crashed on the second road mentioned? "))
        for v in range(0, num_cars_crashed_r_2):
            vehicle = input("What kind of car is in the accident? ")

            self.crashed_cars_road_2.add(vehicle)
        
        print()
        print("What cars are in the intersection of both roads? ")
        #Checks to see if the set is empty. If it is, it returns that there is nothing in the intersection
        if len(self.intersection()) == 0:
            print("No cars are in the intersection.")
        #If there is something in the intersection, which means that the car is in both roads, it returns it.
        else:
            for x in self.intersection():
                print(x)
        print()

        # Gets all the cars involved in the crash, and uses an increment number to make the list look nice.
        print("What is the list of all the cars involved in the accident? ")
        inc_num = 1
        for y in self.combine_sets():
            print(f"{inc_num}. {y}")
            inc_num += 1

        print("=============================")
        print("Thank you for your help, we will calculate an assessment of the crash and report it back to you.")
        print("=============================")
        print()
        
    def ems_situation_assessment(self):
        """
        What EMS will tell us after all the information is gathered. Random is used to give a new report evertime.
        """
        ETA = random.randint(0, 10)
        ambulances = random.randint(1,3)
        paramedics = random.randint(1,15)

        print("The crash assessment is ready.")
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("CRASH REPORT: ")
        print(f"NUMBER OF PARAMEDICS NEEDED: {paramedics}")
        print(f"NUMBER OF AMBULANCES NEEDED: {ambulances}")
        print(f"ESTIMATED TIME OF ARRIVAL: {ETA}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")

        print("Thank you again for telling us all that we needed! Have a good day!")
        print("*EMS has disconnected from the line*")

# Start of the program
bad_crash = Crash()
bad_crash.calling_ems()
"""
Mason Schenk
Queue Problem to Solve
"""

class Water_Fountain_Line():
    """
    This will maintain the water fountain line that was talked about
    in the example mentioned in the module previously. It will have 
    the options for kids to drink water, join the line, see the size
    of the line, and see if the line is empty.

    A kid will not join the line if the line is too long. If the line
    exceeds 5 kids, the kid will say "Forget it" and leave without joining
    the line. Also, the kid who is drinking from the water fountain can't
    come back and get more, they are limited to one turn at the fountain. 
    Finally, the water can't be drank unless a kid is there, so if there
    are no kids in line, and the water goes off, there should be a message
    that is displayed to the effect of "The water is running!".
    """

    def __init__(self):
        """
        Intializes the line as an empty list and keeps a checklist
        to make sure the kids aren't getting seconds.
        """
        self.line = []
        self.checklist = []
    
    def drink_water(self):
        """
        When a kid drinks water, he/she leaves the line, and tells the teacher his/her name.

        Also checks if there are kids in the line. If there is not, an error
        message should be displayed to tell someone of the water running.
        """
        if self.line_empty():
            print("Teacher: The water is running!")
        else:
            kid = self.line[0]
            print(f"My name is {kid}!")

    def join_line(self, value):
        """
        Checks to make sure a kid can join the line. If their name is on the checklist,
        they should recieve a warning. If not, they should be added to the back of the 
        line to wait their turn just like everyone else.

        Also, it checks to make sure the line size is either 5 or below. If not, the kids
        will pass on getting water.

        If both of these conditions are met and the kid can join the line, he/she joins the line
        and their name is added to the checklist.
        """

        if self.more_than_once(value):
            print(f"Teacher: {value.upper()}, GET OVER HERE RIGHT NOW!")
        
        if self.line_size() > 5:
            print(f"{value}: Not worth my time.")

        else:
            self.line.append(value)
            self.checklist.append(value)

    def line_size(self):
        """
        Checks to see the line size.
        """
        return len(self.line)

    def line_empty(self):
        """
        Checks to see if the line is empty.
        """
        if len(self.line) == 0:
            return True
        else:
            return False

    def more_than_once(self, value):
        """
        Receives a value from the user to check and make
        sure the kids aren't getting extra water. If they are, 
        be aware of who they are. If not, they are free
        to join the line as the choose to.
        """
        if value in self.checklist:
            return True
        else:
            return False

# Test Case 1: Kid joins the line and drinks his/her water.
# Expected Result: "My Name is Alex!"
print()
print("TEST CASE I")
print("=========================")
test_line = Water_Fountain_Line()
test_line.join_line("Alex")
test_line.drink_water()
#Errors encountered:

# Test Case 2: Multiple kids join the line and drink their water.
# Expected Result: "My Name is Catherine! My name is Hannah!"
print()
print("TEST CASE II")
print("=========================")
test_line.join_line("Catherine")
test_line.join_line("Hannah")
test_line.drink_water()
test_line.drink_water()
#Errors encountered:

# Test Case 3: Line is too long.
# Expected Result: "Mark: Not worth my time."
print()
print("TEST CASE III")
print("=========================")
test_line.join_line("Meredith")
test_line.join_line("Cristina")
test_line.join_line("Lexi")
test_line.join_line("Bailey")
test_line.join_line("Derrick")
test_line.join_line("Mark")
#Errors encountered:

# Test Case 4: Kid tries to get water more than once.
# Expected Result: "Teacher: ALEX, GET OVER HERE RIGHT NOW!"
print()
print("TEST CASE IV")
print("=========================")
test_line.join_line("Alex")
#Errors encountered:

# Test Case 5: All of the kids drink their water and leave the line.
# Expected Result: "My name is Meredith! My name is Cristina! 
# My name is Lexi! My name is Bailey! My name is Derrick!"
print()
print("TEST CASE V")
print("=========================")
test_line.drink_water()
test_line.drink_water()
test_line.drink_water()
test_line.drink_water()
test_line.drink_water()


# Test Case 6: Line is empty.
# Expected Result: "The water is running!"
print()
print("TEST CASE 6")
print("=========================")
test_line.drink_water()

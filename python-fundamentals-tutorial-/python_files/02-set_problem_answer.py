"""
Mason Schenk
Grocery Store Set
"""

class Grocery_Store_Set():
    """
    This is a Python rendition of the example explained previously in the module. In this 
    class, you will be able to add, remove, see the size, and check to see if a item is 
    present on the list.
    """
    def __init__(self):
        """
        Intializes all of the variables needed throughout the class.
        """
        self.store_set = set()

    def add_item(self, value):
        """
        Adds an item to the set in question.
        """
        return self.store_set.add(value)

    def remove_item(self, value):
        """
        Removes a certain item from the set in question.
        """
        return self.store_set.remove(value)

    def size_of_set(self):
        """
        Checks to see the size of the set.
        """
        return len(self.store_set)

    def item_in_set(self, value):
        """
        Checks to see if an item is in a set. If it is, it returns true.
        Otherwise, returns false.
        """
        if value in self.store_set:
            return True
        else:
            return False

    def set_return(self):
        """
        Returns the set to be used by the tests.
        """
        return self.store_set

# These functions are included outside of the class per dealing with more than one set
def combine_2_sets(set1, set2):
    """
    Combines two sets to form one set.
    """
    #Declartion of the new set
    union_set = set()
    #Double for loops to go through all data
    for ele1 in set1:
        for ele2 in set2:
            #Adds all the elements to the new set(won't add duplicates because of set data type)
            union_set.add(ele1)
            union_set.add(ele2)
    #Returns the set for the tests
    return union_set

def similarties_between_two_sets(set1, set2):
    """
    Checks to see the similarties between two sets
    """
    #Declares the new set
    intersect_set = set()

    #Double for loops to loop through all of data
    for element in set1:
        for element2 in set2:
            #If one of the elements from one set equals another, it adds it to the new set
            if element == element2:
                intersect_set.add(element)
    #If the list length is 0, it returns a statement
    if len(intersect_set) == 0:
        print("There are no similarties between the two sets.")
    #Returns the set for the tests
    return intersect_set

# Test Case 1: Add and remove an item from the set
# Expected Result: "Limes, Grapes" but it doesn't have to be in that order
print()
print("TEST CASE I")
print("=========================")
walmart_list = Grocery_Store_Set()
walmart_list.add_item("Apple")
walmart_list.add_item("Grapes")
walmart_list.add_item("Limes")
walmart_list.remove_item("Apple")

for x in walmart_list.set_return():
    print(x)
#Errors encountered: Change intialization of store set to a set instead of a dictionary.

# Test Case 2: Check to see if an item is in the set
# Expected Result: True, False, True
print() 
print("TEST CASE II")
print("=========================")
print(walmart_list.item_in_set("Grapes"))
print(walmart_list.item_in_set("Apple"))
print(walmart_list.item_in_set("Limes"))
#Errors encountered: Switch the true and false in the check statements.

# Test Case 3: Check to see the size of the set
# Expected Result: "Size of set: 6"
print()
print("TEST CASE III")
print("=========================")
walmart_list.add_item("Milk")
walmart_list.add_item("Eggs")
walmart_list.add_item("Cheese")
walmart_list.add_item("Bacon")
print(f"Size of set: {walmart_list.size_of_set()}")

#Errors encountered:

# Test Case 4: Combine two lists
# Expected Result: {'Eggs', 'Grapes', 'Pizza', 'Limes', 'Mac and Cheese', 'Cheese', 'Bacon', 'Lasagna', 'Milk'}
print()
print("TEST CASE IV")
print("=========================")
costco_list = Grocery_Store_Set()
costco_list.add_item("Eggs")
costco_list.add_item("Lasagna")
costco_list.add_item("Pizza")
costco_list.add_item("Mac and Cheese")

print(combine_2_sets(walmart_list.set_return(), costco_list.set_return()))
#Errors encountered:

# Test Case 5: Similarties bewteen two sets
# Expected Result: {'Eggs'}
print()
print("TEST CASE V")
print("=========================")
print(similarties_between_two_sets(walmart_list.set_return(), costco_list.set_return()))
#Errors encountered: The check needs to see if the elements equal each other, not not equal.

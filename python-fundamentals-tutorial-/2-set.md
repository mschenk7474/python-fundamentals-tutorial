# Python Fundamentals Tutorial: **Set**

## Table of Contents
[Welcome](0-welcome.md)

[Set](2-set.md)
* [Introduction](#introduction)
* [Grocery Store Set (List)](#grocery-store-set-list)
* [Using Sets Over Lists, Stacks, and Queues](#using-sets-over-lists-stacks-and-queues)
* [Python Syntax for Sets](#python-syntax-for-sets)
* [Example](#example)
* [Problem to Solve](#problem-to-solve)

### Introduction
A <span style="color:yellow">set</span> is a data structure that can hold data like a list, stack, and queue. The 3 main things that differentiates a set from all of the rest is that the data within the set has no order, the data is unchangeable, and cannot be duplicates of one another.

### Grocery Store Set (List)
An example that comes to mind when I think of using <span style="color:yellow">sets</span> in normal every day life comes when we go to the grocery store. Every time we go, we create a list, or <span style="color:yellow">set</span> in this case, to remember what we need to get. When we go to the store, this list doesn't change. There may be some things added or removed, but the list mainly stays the same. Normally, there is no order to our list either, it is kind of jumbled up because we put things on store lists when we need them, and what we need may change depending on what is going on in our lives at the moment. Finally, we normally don't put the same thing on a grocery store list. We usually just add x2 of something, but to put the same thing over again seems redundant.

![Figure 2 - Grocery Store Set Picture](images/Grocery-list.jpg)

### Using Sets Over Lists, Stacks, and Queues
Some advantages of using <span style="color:yellow">sets</span> over lists, stacks, and queues:
* Automatically removes duplicates 
* Makes mathmatical operations like combining lists very easy
* Very easy to check if something is within the set

Some disadvantages of using <span style="color:yellow">sets</span> are:
* Not able to access specific indexes
* Not able to modify using slice methods
* No order and can come in different ways every time you print the set

### Python Syntax for Sets
<span style="color:yellow">Set</span> is actually a built-in method in Python and a <span style="color:yellow">set</span> can be intialized in one to two ways.

The first way is shown below:
```python
blank_set = set()
```
Why we couldn't just set equal the blank_set variable to just curly brackets, which is what a normal <span style="color:yellow">set</span> looks like, is because Python has another data structure called a dictionary that uses the curly brackets.

The second and final way to intialize a <span style="color:yellow">set</span>  is shown below:
```python
car_brand_set = {'Ford', 'Chevy', 'Toyota'}
```

With <span style="color:yellow">sets</span>, there are six main functions that are used, with many more being found in documentation [here](https://www.w3schools.com/python/python_sets_methods.asp). Those six main functions are add, remove, size, member, union, and intersect. Those functions will be shown below and the syntax for them will be beside them.

**Set Primary Functions**   | **Python Syntax**
--------------------------- | ----------------------
Add                         |  ``` grocery_list.add(new_value) ```
Remove                      |  ``` grocery_list.remove(remove_value) ```         
Size                        |  ``` g_list_length = len(grocery_list)```
Member                      |  ``` if cereal in grocery_list: ```
Union                       |  ``` both_grocery_lists = union(g_list_1, g_list_2)``` OR ``` both_grocery_lists = g_list_1 \| g_list_2 ```
Intersect                   |  ``` overlap = intersection(g_list_1, g_list_2) ``` OR ``` overlap = g_list_1 & g_list_2 ```
### Example
This week's example problem comes in the form of a car crash seen by a eyewitness. The program begins with the user calling EMS to report the accident, and the bulk of the program is EMS asking questions about what has happened on scene.

To start, we will be going over what the Union and Intersect functions do, and why they are nice to have.

Let's begin with the Union function.
```python
 def combine_sets(self):
        """
        This function will have you combine the two sets, elimanting the duplicates(hint: using the
        union functionality.).
        """
        return self.crashed_cars_road_1 | self.crashed_cars_road_2
```
This is the union function from this week's example. We use the union function to combine the two sets, and since they are sets, they automatically get rid of the duplicates in-between the two sets. This is nice in this certain example because there may be a lot of cars on both of roads, and to get an overview, we will want to see both road sets, and you would use the Union functionality to do so.

Now, let's talk about the Intersect function.
```python
def intersection(self):
        """
        This function is to calculate what cars are in the intersection.
        """
        return self.crashed_cars_road_1 & self.crashed_cars_road_2
```
We use the Intersect function here to see what cars are on both roads, thus being in the intersection between the two roads. This function is useful for other examples when you want to find similarities between two sets you are working with.

Now, Emergency Services will be asking you a few questions because you are calling in the accident. The questions will be as follows:
```python
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
        
```

As we can see at the begininng, EMS will ask for both the roads and all the cars on each of them. We will use the add functionality here to put the cars on sets for EMS. The order doesn't matter here, so that is why we use sets instead of another data structure.

After EMS gets all the cars involved, they are going to want to know which cars are in the intersection, if there any in there in the first place. If there is, we will use the intersection function spoken of before, and find all of the cars that are in the intersection of the two streets. If there isn't any cars in the intersection, the user responds to the dispatch that nothing was in the intersection.

EMS will also want to know a total amount of cars in the accident, so we will use the combine_sets function mentioned above to find that out for EMS. 

After all the information, EMS will generate a report on all that will be coming to the scene, and then hang up.

To see the whole example, click [here](python_files/02-set_example.py).
### Problem to Solve
#### Instructions
This assignment is to be completed individually to make sure you fully understand the concepts taught in this module. 

Download the <a href="python_files/02-set_problem.py" download="02-set_problem.py">02-set_problem.py</a> problem file and do your best to solve the problems with the test cases.

There will be three problems with the file, and each of the test cases provided will give you better insight on what those problems are.

After you are finished finding all the problems, compare your answers to the <a href="python_files/02-set_problem_answer.py" download="02-set_problem_answer.py">answer sheet</a> and see where and what you can improve on.
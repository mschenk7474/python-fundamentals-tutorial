# Mason Schenk

class Queue:
    ''' Creation of the Queue class that will hold all of the functions needed to perform the
    needs of the data structure '''
    def __init__(self):
        ''' Intializing of the Queue in the form of a list '''
        self.queue = []

    def enqueue(self, value):
        ''' Sets up the enqueue function to add a value to the back of the queue '''
        self.queue.append(value)

    def dequeue(self):
        ''' Performs the dequeue functionality, being that it removes the first 
            value of the queue'''
        if self.empty():
            print('Nothing to dequeue!')
        else:
            value = self.queue[0]
            del self.queue[0]
            return value

    def size(self):
        ''' Checks to see the size of the queue '''
        return print(len(self.queue))

    def empty(self):
        ''' Checks to see if the queue is empty '''
        if len(self.queue) == 0:
            return True
        else:
            return False


# Test Case 1: Enqueue and dequeue the same value
# Expected Result: 20
print()
print("TEST CASE I")
print("------------------")
test_queue = Queue()
test_queue.enqueue(20)
test_value = test_queue.dequeue()
print(test_value)

# Test Case 2: Add multiple in the queue, dequeue some, and check size throuhgout
#Expected Result: 6, 3, 0
print()
print("TEST CASE II")
print("------------------")
test_queue.enqueue(5)
test_queue.enqueue(10)
test_queue.enqueue(23)
test_queue.enqueue(45)
test_queue.enqueue(54)
test_queue.enqueue(63)
test_queue.size() 
test_queue.dequeue()
test_queue.dequeue()
test_queue.dequeue()
test_queue.size()
test_queue.dequeue()
test_queue.dequeue()
test_queue.dequeue()
test_queue.size()

# Test Case 3: Try to dequeue when there is nothing in the queue
# Expected Result: Throw an error message per there being nothing to remove
print()
print("TEST CASE III")
print("------------------")
test_queue.dequeue()
print()
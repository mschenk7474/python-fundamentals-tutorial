"""
Mason Schenk
Family Tree
"""
class Family_Tree:
    """
    Creates a Family Tree, like one you would see on Acestry.com, FamilySearch.com, or any other genealogy website.
    It has a relative class included with the family tree because without the context of the Family_Tree class, 
    the functionality wouldn't work on its own. The class has a couple different purposes. It is to add people
    to the tree by birth, check to see if a relative is in the tree, and to get the height of the entire tree.
    """
    class Relative:
        """
        Intializes the data associated with the relative, and both sides that come from that relative.
        """
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    def __init__(self):
        """
        Intializes the Family Tree root to be nothing until someone starts the tree by being born into it.
        """
        self.root = None
    def birth(self, data):
        """
        Someone is born into the Family Tree! If there is no one, and this is the very first person in the tree,
        the person is made the beginning, or the root, of the tree. If the person is not the first person to be added,
        the new person is added to the tree.
        """
        if self.root is None:
            self.root = Family_Tree.Relative(data)
        else:
            self._birth(data, self.root)
    def _birth(self, data, node):
        """
        Where the magic begins. We will going through and using the BST logic to make sure whenever someone is born,
        they are placed on the correct side of the family.
        """
        # No duplicates, if duplicate detected, recursion is terminated
        if data == node.data:
            return
        if data < node.data:
             # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = Family_Tree.Relative(data)
            else:
                # Need to keep looking.  Call _birth
                # recursively on the left sub-tree.
                self._birth(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = Family_Tree.Relative(data)
            else:
                # Need to keep looking.  Call _birth
                # recursively on the right sub-tree.
                self._birth(data, node.right)
        pass
    def if_relative(self, data):
        """
        Checks to see if the relative given is in the Family Tree. It first starts at the root
        and then continues on through the tree.
        """
        return self._if_relative(data, self.root)
    def _if_relative(self, data, node):
        """
        This is how the program continues on through the Family Tree. It will check for duplicates, and 
        return True if there is a duplicate. If not, it will continue to go through the tree until it finds it. 
        If the relative is not found in the tree, False is returned.
        """
        # If number is found, return true
        if data == node.data:
            return True
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot, return false
                return False
            else:
                # Need to keep looking.  Returns 
                # the function recursively with new node
                return self._if_relative(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot, return false
                return False
            else:
                # Need to keep looking.  Returns 
                # the function recursively with new node
                return self._if_relative(data, node.right)
    def generation_check(self):
        """
        Used to check how many generations back the Family Tree goes. If the root of the tree is empty,
        the generation is 0 because there is no one in the tree. If there is someone at the root of the
        tree, the calculation starts there and continues to find how far the tree goes back.
        """
        if self.root is None:
            return 0
        else:
            return self.get_generations(self.root) 
    def get_generations(self, node):
        """
        Calculation of how many generations there are in a Family Tree. If the current node is nothing, then
        0 is returned as the generation number. If not, it goes on both sides of the tree and adds up how many
        times it goes back, and whichever number is bigger is the number that is used as the generation number.
        """
         # Base Case
        if node is None:
            return 0

        # Check to see the height
        else:
            # Function calls for each side of the tree
            height_left = self.get_generations(node.left)
            height_right = self.get_generations(node.right)

            # Adds one if the left side is bigger to account for node that
            # we are currently on.
            if height_left > height_right:
                return height_left + 1

            # Adds one if the right side is bigger to account for node that
            # we are currently on.
            else:
                return height_right + 1
    """
    This is only included to iterate through the BST, not for the actually functionality of the class. Taken
    from the example in this module.
    """
    def traverse_down(self):
        """
        Also known as traversing forward, it starts at the root node and goes 
        to the left subtree to find the smallest value, and 'yields' that value 
        for it to be printed out to the user. It will continue to do this until 
        all of the nodes, smallest to largest have been 'yieled' to be printed out.
        """
        yield from self.real_traverse_down(self.root)

    def real_traverse_down(self, node):
        """
        Where the magic begins. If the current subtree is not none, it will yield the 
        smallest value, and will continue to yield smallest to largest until it has gone 
        through all the nodes.
        """
        if node is not None:
            yield from self.real_traverse_down(node.left)
            yield node.data
            yield from self.real_traverse_down(node.right)

# Test Case 1: Add names and make sure they are in order
# Expected Result: "Adam, Gary, Harry, Leonardo, Xavier"
print()
print("TEST CASE I")
print("=========================")
davis_fam_tree = Family_Tree()
davis_fam_tree.birth("Leonardo")
davis_fam_tree.birth("Gary")
davis_fam_tree.birth("Adam")
davis_fam_tree.birth("Adam")
davis_fam_tree.birth("Harry")
davis_fam_tree.birth("Xavier")

for ele in davis_fam_tree.traverse_down():
    print (ele)
#Errors encountered: Didn't check for multiples

# Test Case 2: Check to see if relative is present in the tree
# Expected Result: 
print() 
print("TEST CASE II")
print("=========================")
print(davis_fam_tree.if_relative("Adam"))
print(davis_fam_tree.if_relative("George"))
print(davis_fam_tree.if_relative("Bob"))
print(davis_fam_tree.if_relative("Leonardo"))
#Errors encountered: Switch the left and right nodes on the _if_relative recursion function calls

# Test Case 3: Check how many generations back the tree goes
# Expected Result: This family tree goes back 5 generations.
print()
print("TEST CASE III")
print("=========================")
davis_fam_tree.birth("Bob")
davis_fam_tree.birth("Jackson")
davis_fam_tree.birth("Alex")
davis_fam_tree.birth("Walter")
davis_fam_tree.birth("Jim")

print(f"This family tree goes back {davis_fam_tree.generation_check()} generations.")
#Errors encountered: Doesn't keep adding the generations


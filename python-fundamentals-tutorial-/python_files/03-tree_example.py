"""
Mason Schenk
BST Example
Written based on 09-prove_trees.py, which was written partly by me.
"""


class BST:
    """
    Creats a Binary Search Tree in Python. We include the Node 
    class within the BST class per it being directly coorelated 
    to a BST, meaning if it stood on its own, it would have no 
    purpose. 
    """
    class Node:
        """
        Each one of the nodes will have data attached to them, 
        whether that be numbers or words, and will have a left 
        and right parent node to start of subtrees.
        """
        def __init__(self, data):
            """
            Intializes the node to the data provided, and 
            intializes the left and right parent nodes.
            """
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Intializes the BST, which means setting root to nothing.
        """
        self.root = None

    def insert(self, data):
        """
        Insets a node and its data in its right spot on the BST. 
        Checks to see if there is a root and if there is not, it 
        will make the data inputted the new root node. If there 
        already is a root, it will go through the list and see 
        where the data node belongs.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self.real_insert(data, self.root)

    def real_insert(self, data, node):
        """
        Where the real magic happens. This function receives the 
        current subtree from the other insert function, and uses the 
        logic of a BST to place the data wherever it needs to go.
        """
        # No duplicates, if duplicate detected, recursion is terminated
        if data == node.data:
            return
        if data < node.data:
             # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call real_insert
                # recursively on the left sub-tree.
                self.real_insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call real_insert
                # recursively on the right sub-tree.
                self.real_insert(data, node.right)
    def member(self, data):
        """
        Checks to see if the value you are looking for is a member of the BST.
        """
        return self.real_member(data, self.root)

    def real_member(self, data, node):
        """
        Where the real magic begins. This function will go throuhgout the 
        entire BST looking for the data variable. Again, the subtree being 
        used is represented by node.
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
                return self.real_member(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot, return false
                return False
            else:
                # Need to keep looking.  Returns 
                # the function recursively with new node
                return self.real_member(data, node.right)
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
    def traverse_up(self):
        """
        Also known as traversing backward, it starts at the root node and goes 
        to the right subtree to find the biggest value, and 'yields' that value 
        for it to be printed out to the user. It will continue to do this until 
        all of the nodes, largest to smallest have been 'yieled' to be printed out.
        """
        yield from self.real_traverse_up(self.root)

    def real_traverse_up(self, node):
        """
        Where the magic begins. If the current subtree is not none, it will yield the 
        largest value, and will continue to yield largest to smallest until it has gone 
        through all the nodes.
        """
        # To reverse, all you need to do is swap the order, so go
        # right to left instead of left to right.
        if node is not None:
            yield from self.real_traverse_up(node.right)
            yield node.data
            yield from self.real_traverse_up(node.left)

    def height(self):
        """
        Determines the height at a given node. Checks to see if there is a root and if 
        there is not, the height is returned to be 0 per the BST being empty. If there is
        a root, the get_height function is called with the root passed into it.
        """
        if self.root is None:
            return 0
        else:
            return self.get_height(self.root)  

    def get_height(self, node):
        """
        Where the magic happens. Checks to see if the current node is none, and if it is,
        the height is returned as 0. Otherwise, the function goes through and traverses 
        the tree, adding up both sides of the current tree to see which side is bigger.
        Whichever side is bigger is returned and is deemed the height of the tree.
        """
        # Base Case
        if node is None:
            return 0

        # Check to see the height
        else:
            # Function calls for each side of the tree
            height_left = self._get_height(node.left)
            height_right = self._get_height(node.right)

            # Adds one if the left side is bigger to account for node that
            # we are currently on.
            if height_left > height_right:
                return height_left + 1

            # Adds one if the right side is bigger to account for node that
            # we are currently on.
            else:
                return height_right + 1

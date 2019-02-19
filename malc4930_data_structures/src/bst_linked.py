"""
-------------------------------------------------------
bst_linked.py
Linked version of the BST ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy

class _BSTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _BSTNode(value)
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes a BST node containing value. Child pointers are None,
            height is 1.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Postconditions:
            _height is 1 plus the maximum of the node's (up to) two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._data)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty bst.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - data to be inserted into the bst (?)
        Postconditions:
            returns
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _data into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - a bst node (_BSTNode)
            value - data to be inserted into the node (?)
        Postconditions:
            returns
            node - the current node (_BSTNode)
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            node = _BSTNode(value)
            self._count += 1
            inserted = True
            
        elif node._data > value:
            node._left, inserted = self._insert_aux(node._left, value)
            
        elif node._data < value:
            node._right, inserted = self._insert_aux(node._right, value)
            
        else:
            inserted = False

        if inserted:
            node._update_height()
            
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot retrieve from an empty BST"

        node = self._root
        value = None

        while node is not None and value is None:

            if node._data > key:
                node = node._left
            elif node._data < key:
                node = node._right
            elif node._data == key:
                value = deepcopy(node._data)
                
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value matching key if found,
            otherwise returns None. Update structure of bst as required.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove from an empty BST"

        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
            node - a bst node to search for key (_BSTNode)
            key - data to search for (?)
        Postconditions:
            returns
            node - the current node or its replacement (_BSTNode)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._data:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._data:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._data
            # Replace this node with another node.
            if node._left is None:
                # node has no left child or has no children.
                node = node._right
                
            elif node._right is None:
                node = node._left

            else:
                # Node has two children
                if node._left._right is None:
                    # left child is replacement node
                    repl_node = node._left
                else:
                    # find replacement node in right subtree of left node
                    repl_node = self._delete_node_left(
                        node._left, node._left._right)
                    repl_node._left = node._left

                repl_node._right = node._right
                node = repl_node
                node._update_height()

            self._count -= 1

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
            
        return node, value
    

    def _delete_node_left(self, parent, child):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
            child - the right node of parent (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """
        if child._right is None:
            repl_node = child
            parent._right = child._left
            
        else:
            repl_node = self._delete_node_left(child, child._right)
        
        return repl_node
            
        parent._update_height()
    
    def balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.balanced()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._root is None:
            is_balanced = True
        else:
            is_balanced = self.balanced_aux(self._root)
        return is_balanced
        
#     def balanced_aux(self, n1, n2):
#         if n1 is None and n2 is None:
#             result = True
#             
#         elif n1 is None or n2 is None:
#             result = False
#             
#         elif abs(n1._height - n2._height) > 0: 
#             result = False
#             
#         else:
#             result = self.balanced_aux(n1._left, n1._right) and self.balanced_aux(n2._left,n2._right)
#             
#         return result
    def balanced_aux(self, node):
        if node:
            l = node._left
            r = node._right
            if l and r:
                bal = abs(l._height - r._height) <= 1
                
                if l._left:
                    l = self.balanced_aux(l)
                if r._right:
                    r = self.balanced_aux(r)
            elif l or r:
                bal = False
            else:
                bal = True
        else:
            bal = True
        return bal
    
    
    def valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.valid()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        is_valid = self.valid_aux(self._root)
        return is_valid
    
    def valid_aux(self, curr):
        
        if curr is None or curr._right is None or curr._left is None:
            is_valid = True
        elif curr._left._data <= curr._data and curr._data <= curr._right._data:
            is_valid = self.valid_aux(curr._left) and self.valid_aux(curr._right)        
        else:
            is_valid = False
                
        return is_valid
    
    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another bst (BST)
        Postconditions:
            returns
            is_identical - True if this bst contains the same values
            in the same order as rs, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        is_identical = self.identical_aux(self._root, rs._root)
        return is_identical
    
    def identical_aux(self,n, nr):
        if n is None and nr is None:          
            is_identical = True
        
        elif n is not None and nr is not None:
            if n._data != nr._data:
                is_identical = False
            else:
                is_identical = self.identical_aux(n._right, nr._right) and self.identical_aux(n._left, nr._left)
        else:
            is_identical = False
               
        return is_identical
    
    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Postconditions:
            returns
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero, one, two = self.node_counts_aux(self._root)
        return zero, one, two
    
    def node_counts_aux(self, node):
        
        if node is not None:
            zero_r, one_r, two_r = self.node_counts_aux(node._right)
            zero_l, one_l, two_l = self.node_counts_aux(node._left)    
            zero = zero_r + zero_l
            one = one_r + one_l
            two = two_r + two_l
    
            if node._left is not None and node._right is not None:  
                two  = two + 1
                
            elif node._left is None and node._right is None:
                zero = zero + 1
                
            else:
                one = one + 1
                
        else:
            zero = 0 
            one = 0
            two = 0
             
        return zero, one, two
    
    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in a BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root
        
        if node == None:
            value = None
        else:
            value = self.min_r_aux(node)

        return value._data
    
    def min_r_aux(self, node):
        
        if node._left == None:
            value = node
        else:
            value = self.min_r_aux(node._left)
            
        return value
        
        
    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root
        
        if node == None:
            value = None
        else:
            value = self.max_r_aux(node)

        return value._data
    
    
    def max_r_aux(self, node):
        
        if node._right == None:
            value = node
        else:
            value = self.max_r_aux(node._right)
            
        return value
    
    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: bst.inorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = self.inorder_aux(self._root)
        return a
    
    def inorder_aux(self,n):
        a = []
        if n:
            a = self.inorder_aux(n._left)
            a.append(n._data)
            a = a + self.inorder_aux(n._right)
    
        return a
    
    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: bst.preorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = self.preorder_aux(self._root)
        return a
    
    def preorder_aux(self,n):
        a = []
        if n:
            a.append(n._data)
            a = a + self.preorder_aux(n._left)          
            a = a + self.preorder_aux(n._right)
    
        return a
    
    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: bst.postorder()
        -------------------------------------------------------
        Postconditions:
            returns
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = self.postorder_aux(self._root)
        return a
    
    def postorder_aux(self,n):
        a = []
        if n:         
            a = self.postorder_aux(n._left)          
            a = a + self.postorder_aux(n._right)
            a.append(n._data)
    
        return a
    
    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Postconditions:
            returns
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        a = []
       
        if self._root is not None:
            node = self._root
            c = []
            c.append(node)
            while len(c) != 0:   
                n = []   
                for v in c:
                    a.append(v._data)
                    if v._left is not None:
                        n.append(v._left)
                    if v._right is not None:
                        n.append(v._right)
                c = n
           
        return a

    
    def __iter__(self):
        """
        -------------------------------------------------------
         Generates a Python iterator. Iterates through a BST node
         in level order.
         Use: for v in bst:
        -------------------------------------------------------
         Postconditions:
             yields
             value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                node = queue.pop(0)
                yield node._data

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
                    
        
    def count_apply(self, func):
        """
        ---------------------------------------------------------
        Returns the number of values in a BST where func(value) is True.
        Use: number = bst.count_apply(func)
        -------------------------------------------------------
        Preconditions:
            func - a function that given a value in the bst returns
                True for some condition, otherwise returns False.
        Postconditions:
            returns
            number - count of nodes in tree where func(value) is True (int)
        ----------------------------------------------------------
        """
        count = [0]

        if self._root is not None:
            self._count_apply_aux(self._root, func, count)
            
        return count[0]
        
        
    def _count_apply_aux(self, node, func, count):
        if func(node._data):
            count[0] += 1
        if node._left:
            self._count_apply_aux(node._left, func, count)
        if node._right:
            self._count_apply_aux(node._right, func, count)
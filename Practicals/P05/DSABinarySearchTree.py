import DSAQueue

class _DSATreeNode:
    def __init__(self, in_key, in_value):          
        self._key = in_key
        self._value = in_value
        self._left = None
        self._right = None
    
    def __iter__(self):
        if self._left:
            for elt in self._left:         
                yield elt
        yield (self._key, self._value)
        
        if self._right:
            for elt in self._right:
                yield elt

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def get_left(self):
        return self._left

    def set_left(self, new_left):
        self._left = new_left

    def get_right(self):
        return self._right

    def set_right(self, new_right):
        self._right = new_right
        
class DSABinarySearchTree:
    def __init__(self):
        self._root = None
    
    def __iter__(self):
        class EmptyIterator:
            def next(self):
                raise StopIteration
            
        if self._root:
            return iter(self._root)
        else:
            return EmptyIterator()
    
    def find(self, key):
        return self._find(key, self._root)
    
    def _find(self, key, cur):
        value = None
        if cur == None: 
            raise ValueError("Key " + key + " not found")
        elif key == cur.get_key(): 
            value = cur.get_value()
        elif key < cur.get_key():  
            value = self._find(key, cur.get_left())
        else: 
            value = self._find(key, cur.get_right())
        return value
    
    def insert(self, key, data):
        self._insert(key, data, self._root)
        
    def _insert(self, key, data, curr):
        update_node = curr
        if curr is None:
            update_node = _DSATreeNode(key, data)
            if self._root is None:
                self._root = update_node
        elif key == curr.get_key():
            raise Exception("Duplicate key.")
        elif key < curr.get_key():
            curr.set_left(self._insert(key, data, curr.get_left()))
        else:
            curr.set_right(self._insert(key, data, curr.get_right()))
        return update_node
    
    def delete(self, key):
        self._delete(key, self._root)
    
    def _delete(self, key, curr):
        update_node = curr
        if curr is None:
            raise Exception("Key " + key + " not found")
        elif key == curr.get_key():
            update_node = self.delete_node(key, curr)
        elif key < curr.get_key():
            curr.set_left(self._delete(key, curr.get_left()))
        else:
            curr.set_right(self._delete(key, curr.get_right()))
        return update_node
    
    def delete_node(self, key, node_del):
        update_node = None
        if node_del is None and node_del.get_right() is None:
            update_node = None
        elif node_del.get_left() is not None and node_del.get_right() is None:
            update_node = node_del.get_left()
        elif node_del.get_left() is None and node_del.get_right() is not None:
            update_node = node_del.get_right()
        else:
            update_node = self.promote_successor(node_del.get_right())
            if update_node != node_del.get_right():
                update_node.set_right(node_del.get_right())
            update_node.set_left(node_del.get_left())
        return update_node
        
    def promote_successor(self, curr):
        if curr.get_left() is not None:
            successor = self.promote_successor(curr.get_left())
            if successor == curr.get_left():
                curr.set_left(successor.get_right())
        return successor
                 
    # Uses Traverse Inorder
    def display(self):
        inorder_queue = DSAQueue.DSAQueue()
        self._traverse_inorder(self._root, inorder_queue)
        
        for i in inorder_queue:
            print(i)
        
    ##### Min, Max, Height #####
    def calc_min(self):
        return self._calc_min(self._root)
    
    def _calc_min(self, curr_node):
        if (curr_node.get_left() != None):
            min_key = self._calc_min(curr_node.get_left()) 
        else:
            min_key = curr_node.get_key()
        return min_key
    
    def calc_max(self):
        return self._calc_max(self._root)
    
    def _calc_max(self, curr_node):
        if (curr_node.get_right() != None):
            max_key = self._calc_max(curr_node.get_right()) 
        else:
            max_key = curr_node.get_key()
        return max_key
    
    def height(self): 
        return self._height(self._root)
    
    def _height(self, curr_node):
        if curr_node == None: 
            curr_height = -1
        else:
            left_height = self._height(curr_node.get_left()) 
            right_height = self._height(curr_node.get_right()) 
    
            if left_height > right_height:
                curr_height = left_height + 1
            else:
                curr_height = right_height + 1
        return curr_height
    
    def balance(self):
        if self._root is None:
            balance = 1
        else:
            left_height = self._height(self._root.get_left())    
            right_height = self._height(self._root.get_right()) 
            root_height = self.height()   
            diff = abs(left_height - right_height)
            balance = 1 - (float(diff) / float(root_height))
        return balance    
        
    ##### Traversals #####
    def traverse_preorder(self):
        preorder_queue = DSAQueue.DSAQueue()
        self._traverse_preorder(self._root, preorder_queue)
        return preorder_queue
    
    # Wrapper method for preorder traversal
    def _traverse_preorder(self, root, queue):
        if root is not None:
            queue.enqueue(root.get_value())
            self._traverse_preorder(root.get_left(), queue)
            self._traverse_preorder(root.get_right(), queue)
    
    def traverse_inorder(self):
        inorder_queue = DSAQueue.DSAQueue()
        self._traverse_inorder(self._root, inorder_queue)
        return inorder_queue
    
    # Wrapper method for inorder traversal
    def _traverse_inorder(self, root, queue):
        if root is not None:
            self._traverse_inorder(root.get_left(), queue)
            queue.enqueue(root.get_value())
            self._traverse_inorder(root.get_right(), queue)

    def traverse_postorder(self):
        postorder_queue = DSAQueue.DSAQueue()
        self._traverse_postorder(self._root, postorder_queue)
        return postorder_queue        
    
    # Wrapper method for postorder traversal
    def _traverse_postorder(self, root, queue):
        if root is not None:
            self._traverse_postorder(root.get_left(), queue)
            self._traverse_postorder(root.get_right(), queue)
            queue.enqueue(root.get_value())

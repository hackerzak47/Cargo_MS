from node import *
def comp(a, b):
    return a - b

class AVLTree:
    def __init__(self, compare_function=comp):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if not node:
            return None


        while node.left is not None:
            node = node.left
        return node
    
    def insert(self, key, value=None):
        if not self.root:
            self.root = Node(key)
            self.root.value = value
            self.size = self.size + 1
            return self.root

        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            new_node = Node(key)
            new_node.value = value
            self.size = self.size + 1
            return new_node

        comparison = self.comparator(key, node.key)

        if comparison < 0:
            node.left = self._insert(node.left, key, value)
        elif comparison > 0:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.comparator(key, node.left.key) < 0:
            return self.right_rotate(node)
        if balance < -1 and self.comparator(key, node.right.key) > 0:
            return self.left_rotate(node)
        if balance > 1 and self.comparator(key, node.left.key) > 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.comparator(key, node.right.key) < 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if not node or node.key == key:
            return node

        comparison = self.comparator(key, node.key)

        if comparison < 0:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, node, key):
        self.root = self._delete(node, key)
        
    def _delete(self, node, key):
        if not node:
            return None 

        comparison = self.comparator(key, node.key)

        if comparison < 0:
            node.left = self._delete(node.left, key)
        elif comparison > 0:
            node.right = self._delete(node.right, key)
        else:
 
            if not node.left:
                self.size = self.size -  1  
                return node.right
            elif not node.right:
                self.size = self.size - 1 
                return node.left

 
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value  
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))


        balance = self.get_balance(node)


        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node
        
    def _get_min_value_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if not node:
            return None

        while node.right is not None:
            node = node.right
        return node
    def find_max_greater_or_equal(self, key):
        return self._find_max_greater_or_equal(self.root, key)

    def _find_max_greater_or_equal(self, node, key):
        if not node:
            return None


        if node.key >= key:
            desired = self._find_max_greater_or_equal(node.right, key)
            return desired if desired is not None else node
        else:

            return self._find_max_greater_or_equal(node.right, key)

    def find_min_greater_or_equal(self, key):
        return self._find_min_greater_or_equal(self.root, key)

    def _find_min_greater_or_equal(self, node, key):
        if not node:
            return None

        if node.key >= key:

            desired = self._find_min_greater_or_equal(node.left, key)
            return desired if desired is not None else node
        else:

            return self._find_min_greater_or_equal(node.right, key)
        
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
            
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    
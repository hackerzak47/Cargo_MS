from avl import *

class Bin:
    def __init__(self, Bin_ID, capacity):
        self.objects_tree = AVLTree()
        self.capacity = capacity
        self.Bin_ID = Bin_ID
        self.current_capacity = capacity

    def add_object(self, object):
        self.objects_tree.insert(object.object_id, object)
        
    def remove_object(self, object_id):
        self.objects_tree.delete(self.objects_tree.root, object_id)
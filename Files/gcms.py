from avl import *
from object import *
from exceptions import *
from bin import *

class GCMS:
    def __init__(self):
        self.Bin_capacity_tree_with_key_id_topo_sort = AVLTree()
        self.object_id_tree = AVLTree()
        self.Layered_Bin_Object_tree = AVLTree()

    def add_bin(self, Bin_ID, capacity):
        new_bin = Bin(Bin_ID, capacity)
        self.Layered_Bin_Object_tree.insert(Bin_ID, new_bin)
        if self.Bin_capacity_tree_with_key_id_topo_sort.root is None:
            id_tree = AVLTree()
            id_tree.insert(Bin_ID, new_bin)
            self.Bin_capacity_tree_with_key_id_topo_sort.insert(capacity, id_tree)
            return
        node = self.Bin_capacity_tree_with_key_id_topo_sort._search(self.Bin_capacity_tree_with_key_id_topo_sort.root, capacity)
        if node:
            node.value.insert(Bin_ID, new_bin)
        else:
            id_tree = AVLTree()
            id_tree.insert(Bin_ID, new_bin)
            self.Bin_capacity_tree_with_key_id_topo_sort.insert(capacity, id_tree)

    def add_object(self, object_id, size, color):
        object = Object(object_id, size, color)
        if object.color == Color.BLUE:
            temp = self.Bin_capacity_tree_with_key_id_topo_sort.find_min_greater_or_equal(object.size)
            if temp:
                id_tree = temp.value
                best_place_for_cargo=id_tree.find_min().value
            else:
                raise NoBinFoundException
        if object.color == Color.YELLOW:
            temp = self.Bin_capacity_tree_with_key_id_topo_sort.find_min_greater_or_equal(object.size)
            if temp:
                id_tree = temp.value
                best_place_for_cargo=id_tree.find_max().value
            else:
                raise NoBinFoundException
        if object.color == Color.RED:
            temp = self.Bin_capacity_tree_with_key_id_topo_sort.find_max_greater_or_equal(object.size)
            if temp:
                id_tree = temp.value
                best_place_for_cargo=id_tree.find_min().value
            else:
                raise NoBinFoundException
        if object.color == Color.GREEN:
            temp = self.Bin_capacity_tree_with_key_id_topo_sort.find_max_greater_or_equal(object.size)
            if temp:
                id_tree = temp.value
                best_place_for_cargo=id_tree.find_max().value
            else:
                raise NoBinFoundException
        best_place_for_cargo.add_object(object)
        self.object_id_tree.insert(object.object_id, best_place_for_cargo)
        node = self.Bin_capacity_tree_with_key_id_topo_sort.search(best_place_for_cargo.current_capacity)
        if node.value.size == 1:
            self.Bin_capacity_tree_with_key_id_topo_sort.delete(self.Bin_capacity_tree_with_key_id_topo_sort.root, best_place_for_cargo.current_capacity)
        else:
            node.value.delete(node.value.root, best_place_for_cargo.Bin_ID)
        best_place_for_cargo.current_capacity -= object.size

        node = self.Bin_capacity_tree_with_key_id_topo_sort.search(best_place_for_cargo.current_capacity)
        if node:
            node.value.insert(best_place_for_cargo.Bin_ID, best_place_for_cargo)
        else:
            instance = AVLTree()
            instance.insert(best_place_for_cargo.Bin_ID, best_place_for_cargo)
            self.Bin_capacity_tree_with_key_id_topo_sort.insert(best_place_for_cargo.current_capacity, instance)

    def delete_object(self, object_id):
        temp_1 = self.object_id_tree.search(object_id)

        if temp_1:
            bin_node = temp_1.value
            temp_2 = bin_node.objects_tree.search(object_id)
            object = temp_2.value
            bin_node.remove_object(object_id)
            self.object_id_tree.delete(self.object_id_tree.root, object_id)
            current_capacity_node = self.Bin_capacity_tree_with_key_id_topo_sort.search(bin_node.current_capacity)
            if current_capacity_node.value.size == 1:
                self.Bin_capacity_tree_with_key_id_topo_sort.delete(self.Bin_capacity_tree_with_key_id_topo_sort.root, bin_node.current_capacity)
                bin_node.current_capacity += object.size
            else:
                current_capacity_node.value.delete(current_capacity_node.value.root, bin_node.Bin_ID)
                bin_node.current_capacity += object.size
            updated_capacity_node = self.Bin_capacity_tree_with_key_id_topo_sort.search(bin_node.current_capacity)
            if updated_capacity_node:
                updated_capacity_node.value.insert(bin_node.Bin_ID, bin_node)
            else:
                instance = AVLTree()
                instance.insert(bin_node.Bin_ID, bin_node)
                self.Bin_capacity_tree_with_key_id_topo_sort.insert(bin_node.current_capacity, instance)
        else:
            return None

    def bin_info(self, Bin_ID):
        node = self.Layered_Bin_Object_tree.search(Bin_ID)
        if node:
            bin_node = node.value
            return (bin_node.current_capacity, bin_node.objects_tree.inorder_traversal())
        else:
            return None

    def object_info(self, object_id):
        node = self.object_id_tree.search(object_id)
        if node:
            bin_node = node.value
            return bin_node.Bin_ID
        else:
            return None
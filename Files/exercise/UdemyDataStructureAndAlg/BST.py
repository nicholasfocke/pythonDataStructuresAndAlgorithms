class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None   

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
  
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True

                temp = temp.right

    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False
        


my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)

print(my_bst.contains(10))
print(my_bst.contains(82))


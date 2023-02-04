class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def remove(self, data):

        if self.root:
            if data == self.root.data:
                return self.remove_node(self.root)

            if data < self.root.data:
                if self.root.left:
                    return self.remove_node(self, data, self.root.left)
            elif self.root.right:
                return self.remove_node(self, data, self.root.right)

    def remove_node(self, data, node):
        if data == node.data:
            if not node.parent:
                pass
            else:
                if node.right:
                    node.parent.right = node.right
                elif node.left:
                    pass
                else:
                    if node.parent.data < data:
                        node.parent.right = None
                    else:
                        node.parent.left = None
        else:
            if node.left:
                remove_node()

    def insert(self, data):
        # first node in the BST
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                # the left node exists (so we keep going)
                self.insert_node(data, node.left)
            else:
                # there is no left child
                node.left = Node(data, node)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left:
            return self.get_min_value(node.left)

        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right:
            return self.get_max_value(node.right)

        return node.data

    def traverse(self):
        # in order
        if self.root:
            self.in_order(self.root)

    def in_order(self, node):

        if node.left:
            self.in_order(node.left)

        print(node.data)

        if node.right:
            self.in_order(node.right)

    def pre_order(self, node):
        print(node.data)

        if node.left:
            self.in_order(node.left)

        if node.right:
            self.in_order(node.right)

    def post_order(self, node):

        if node.left:
            self.in_order(node.left)

        if node.right:
            self.in_order(node.right)

        print(node.data)


b = BinarySearchTree()

b.insert(32)
b.insert(10)
b.insert(1)
b.insert(19)
b.insert(16)
b.insert(23)
b.insert(55)
b.insert(79)

b.traverse()

print(b.get_max())
print(b.get_min())

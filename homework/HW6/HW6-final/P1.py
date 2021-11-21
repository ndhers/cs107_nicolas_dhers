from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def _removemin(self, node):
        if not node.left:
            return node.right
        else:
            node.left = self._removemin(self, node.left)
            node.size = self._size(node.left) + self._size(node.right) + 1
            return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key {key} not found.')
        elif key == node.key:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            t = node
            node = t.right
            while node.left:
                node = node.left
            node.right = self._removemin(t.right)
            node.left = t.left
        elif key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    @staticmethod
    def _size(node):
        return node.size if node else 0


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree
        self.nodes = []
        self.index = 0
        self.traversalType = traversalType

        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            node = self.nodes[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return node

    def inorder(self, bst: BSTTable):
        if bst:
            self._inorder_traverse(bst._root)

    def preorder(self, bst: BSTTable):
        if bst:
            self._preorder_traverse(bst._root)

    def postorder(self, bst: BSTTable):
        if bst:
            self._postorder_traverse(bst._root)

    # Helper Functions
    def _inorder_traverse(self, bst: BSTNode):
        if not bst:
            return
        self._inorder_traverse(bst.left)
        self.nodes.append(bst)
        self._inorder_traverse(bst.right)

    def _preorder_traverse(self, bst: BSTNode):
        if not bst:
            return
        self.nodes.append(bst)
        self._preorder_traverse(bst.left)
        self._preorder_traverse(bst.right)

    def _postorder_traverse(self, bst: BSTNode):
        if not bst:
            return
        self._postorder_traverse(bst.left)
        self._postorder_traverse(bst.right)
        self.nodes.append(bst)


if __name__ == "__main__":

    # tree = BSTTable()
    # tree.put(0, 'd')
    # tree.put(2, 'c')
    # tree.put(5, 'a')
    # tree.put(1, 'b')
    # print(tree._root)
    # print(tree._removemin(tree._root))

    # tree = BSTTable()
    # tree.put(5, 'a')
    # tree.put(1, 'b')
    # tree.put(2, 'c')
    # tree.put(0, 'd')
    # print(tree)
    # tree.remove(5)
    # print(tree)
    # tree.remove(1)
    # print(tree)


    # input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
    # bst = BSTTable()
    # for key, val in input_array:
    #     bst.put(key, val)
    # traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
    # for node in traversal:
    #     print(str(node.key) + ', ' + node.val)

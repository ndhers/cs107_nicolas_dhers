from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array)  # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            # buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                self.to_string(new_prefix, self.left(idx), True) + \
                self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        if idx >= self.size:
            return
        left_node = self.left(idx)
        right_node = self.right(idx)
        current = idx
        if left_node < self.size and self.compare(self.elements[current], self.elements[left_node]):
            current = left_node
        if right_node < self.size and self.compare(self.elements[current], self.elements[right_node]):
            current = right_node
        if idx != current:
            self.swap(idx, current)
            self.heapify(current)

    def build_heap(self) -> None:
        for i in range(floor(self.size/2 - 1), -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        self.filterup(self.elements.index(key))

    def filterup(self, idx: int) -> None:
        if idx:
            parent = self.parent(idx)
            if self.compare(self.elements[parent], self.elements[idx]):
                self.swap(parent, idx)
                self.filterup(parent)

    def heappop(self) -> int:
        if self.size == 0:
            raise IndexError('Cannot pop: outside of index.')
        else:
            popped = self.elements[0]
            self.swap(0, self.size - 1)
            self.elements.pop()
            self.size -= 1
            self.heapify(0)
            return popped


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a > b:
            return True
        else:
            return False


class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a < b:
            return True
        else:
            return False


# if __name__ == "__main__":
#     # The heap tree will be built during initialization
#     mn = MinHeap([1,2,3,4,5])
#     # mx = MaxHeap([1,2,3,4,5])

#     print(mn)
#     # print(mx)

#     mn.heappush(0)
#     print(mn)

#     minimum = mn.heappop()
#     print(minimum)

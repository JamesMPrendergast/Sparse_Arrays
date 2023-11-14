from numpy import random
from typing import TypeVar, Tuple

T = TypeVar("T")
Node = Tuple[int, T, T]


class SparseArray:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, width: int, height: int, num_items):
        self.width = width
        self.height = height
        self.sparse_array = None

        self.fillRandomly(num_items)

    def fill_randomly(self, num):
        for i in range(num):
            self.add(random.randint(self.width),
                     random.randint(self.height),
                     self.letters[random.randint(len(self.letters))])



    def add(self, x: int, y: int, value: T) -> bool:
        """
        adds a node with the provided value to the coordinates (x, y)
        if there is a preexisting value at (x, y) then it overrides it
        :param x:
        :param y:
        :param value:
        :return: True if successfully incremented the total number of items; False if it replaced a value
        """
        b = self.sparse_array
        p = b
        while p is not None:
            if p[0] == y:
                b = p
                p = p[1]
                while p is not None:
                    if p[0] == x:
                        p[1] = value
                        return False
                    elif p[0] > y:
                        p = Node(x, value, p)
                        b[2] = p
                        return True
                    else:
                        b = p
                        p = p[2]
                b[1] = Node(x, value, None)
                return True
            elif p[0] > y:
                p = Node(y, None, p)
                b[2] = p
            else:
                b = p
                p = p[2]
        p = Node(y, Node(x, value, None), None)
        b[2] = p
        return True

    def __str__(self):
        b = self.sparse_array
        p = b
        while p is not None:
            print(f"{p[0]}:", end="\t")
            q = b[1]
            while q is not None:
                print(f"({q[0]}, {q[1]})", end="\t")
            b = p
            p = b[2]



from numpy import random
from typing import TypeVar, Tuple

T = TypeVar("T")
Node = Tuple[int, T, T]


def create_node(index, value, next) -> Node:
    return [index, value, next]


class SparseArray:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, width: int, height: int, num_items):
        self.width = width
        self.height = height
        self.sparse_array = None

        self.fill_randomly(num_items)

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
                b_within = False
                while p is not None:
                    if p[0] == x:
                        p[1] = value
                        return False
                    elif p[0] > x:
                        p = create_node(x, value, p)
                        if b_within:
                            b[2] = p
                        else:
                            b[1] = p
                        return True
                    else:
                        b = p
                        p = p[2]
                        b_within = True
                p = create_node(x, value, None)
                if b_within:
                    b[2] = p
                else:
                    b[1] = p
                return True
            elif p[0] > y:
                if b is p:
                    p = create_node(y, None, p)
                    self.sparse_array = p
                    b = p
                else:
                    p = create_node(y, None, p)
                    b[2] = p
            else:
                b = p
                p = p[2]
        p = create_node(y, create_node(x, value, None), None)
        if b is None:
            self.sparse_array = p
        else:
            b[2] = p
        return True

    def __getitem__(self, x):
        i = 0
        p = self.sparse_array
        while p is not None:
            q = p[1]
            while q is not None:
                if i == x:
                    return q[1]
                i += 1
                q = q[2]
            p = p[2]
        return None

    def get_value_at_coordinates(self, x, y):
        p = self.sparse_array
        while p is not None:
            if p[0] == y:
                q = p[1]
                while q is not None:
                    if q[0] == x:
                        return q[1]
                    elif q[0] > x:
                        return None
                    q = q[2]
            elif p[0] > y:
                return None
            p = p[2]
        return None

    def find_coordinates_of_value(self, value: str):
        p = self.sparse_array
        while p is not None:
            q = p[1]
            while q is not None:
                if q[1] == value:
                    return [q[0], p[0]]
                q = q[2]
            p = p[2]
        return None

    def find_index_of_value(self, value: str):
        i = 0
        p = self.sparse_array
        while p is not None:
            q = p[1]
            while q is not None:
                if q[1] == value:
                    return i
                i += 1
                q = q[2]
            p = p[2]

    def __str__(self):
        print("gathering __str__")
        output = ""
        b = self.sparse_array
        p = b
        while p is not None:
            output += f"{p[0]}:\t"
            q = p[1]
            while q is not None:
                output += f"({q[0]}, {q[1]})\t"
                q = q[2]
            output += "\n"
            b = p
            p = b[2]
        return output

    def tree(self) -> str:
        return self.__str__()

    def grid(self) -> str:
        p = self.sparse_array
        if p is None:
            return "Sparse Array is None"
        output = "\t"
        for x in range(self.width):
            output += f"{x}\t"
        output += "\n"
        for y in range(self.height):
            output += f"{y}\t"
            if y == p[0]:
                q = p[1]
                for x in range(self.width):
                    if x == q[0]:
                        output += q[1]
                        q = q[2]
                        if q is None:
                            break
                    output += "\t"
                p = p[2]
                if p is None:
                    break
            output += "\n"
        return output

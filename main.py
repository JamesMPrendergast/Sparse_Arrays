from SparseArrayFile import SparseArray


def ask_for_coordinates():
    print("\n----------")
    x = int(input("x coordinate: "))
    y = int(input("y coordinate: "))
    value = sa.get_value_at_coordinates(x, y)
    print(f"value = {value}")


def ask_for_value():
    print("\n----------")
    value = input("find value: ")
    print(f"coordinates = {sa.find_coordinates_of_value(value)}")
    print(f"index = {sa.find_index_of_value(value)}")

def ask_for_index():
    print("\n----------")
    i = int(input("index: "))
    value = sa[i]
    print(f"value = {value}")


if __name__ == '__main__':
    sa = SparseArray(20, 20, 70)
    print(sa.tree())
    print("\n---------------------\n")
    print(sa.grid())
    while True:
        ask_for_index()
        ask_for_coordinates()
        ask_for_value()

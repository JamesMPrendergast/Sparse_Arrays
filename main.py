from SparseArrayFile import SparseArray

if __name__ == '__main__':
    sa = SparseArray(20, 20, 25)
    print(sa.tree())
    print("\n---------------------\n")
    print(sa.grid())

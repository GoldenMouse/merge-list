def merge_lists(l1, l2):
    zipped = zip(l1,l2)

    return [i for tup in zipped for i in tup]


l1 = [1,2,3,4]
l2 = ['a','b','c','d','e']

print(merge_lists(l1,l2))

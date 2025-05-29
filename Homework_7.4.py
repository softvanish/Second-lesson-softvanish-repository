# Пошук спільних елементів

def common_elements():
    a = list(range(0, 100, 3))
    b = list(range(0, 100, 5))
    a_set = set(a)
    b_set = set(b)
    intersection_set = a_set.intersection(b_set)
    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Everything is right")


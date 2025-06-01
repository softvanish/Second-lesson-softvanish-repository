# Унікальне число

def find_unique_value(some_list):
    new_list = []
    for i in some_list:
        if some_list.count(i) == 1:
            new_list.append(i)
    if len(new_list) == 1:
        return new_list[0]
    return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([1, 1, 3, 4, 5, 5]) == None, 'Test4'

print("ОК")

def difference(*args):

    if (args):
        min_num = min(*args)
        max_num = max(*args)
        result = max_num - min_num

        return result

    else:
        return 0



assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
print('OK')

# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference() == 0, 'Test4'


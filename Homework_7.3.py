# Пошук підрядка

def second_index(text, some_str):
  indexes = []
  start = 0
  while True:
    position = text.find(some_str, start)
    if position == -1:
      break
    indexes.append(position)
    start = position + 1
  if len(indexes) >= 2:
    return indexes[1]
  return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# Клас "Цифровий лічильник"

class Counter:

###

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

###

   def set_current(self, start):
       if self.min_value <= start <= self.max_value:
           self.current = start
       else:
           raise ValueError("Your number is bigger or less than the acceptable limits.")

###

   def set_max(self, max_max):
       if max_max < self.min_value:
           raise ValueError("This cannot be the max value because it's less than min value.")
       if self.current > max_max:
           raise ValueError("This cannot be the max value because it's less than current value.")
       self.max_value = max_max

###

   def set_min(self, min_min):
       if min_min > self.max_value:
           raise ValueError("This cannot be the min value because it's more than max value.")
       if self.current < min_min:
           raise ValueError("This cannot be the min value because it's more than current value.")
       self.min_value = min_min

###

   def step_up(self):
       if self.current == self.max_value:
           raise ValueError("You cannot raise it up, current value is already max.")
       else:
           self.current += 1

###

   def step_down(self):
       if self.current == self.min_value:
           raise ValueError("You cannot reduce it, current value is already min.")
       else:
           self.current -= 1

###

   def get_current(self):
       return self.current

##########################################


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'

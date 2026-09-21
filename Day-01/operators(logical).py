has_membership = True
gym_open = False

can_enter = has_membership and gym_open
print(can_enter)   # False

gym_open = False
home_setup = True

can_workout = gym_open or home_setup
print(can_workout)   # True


raining = False
print(not raining)   # True

age = 20
has_id = True

print(age >= 18 and has_id)






# for better understanding 
x = 7
print(x > 5 and x < 10)
print(x > 5 and x > 10)
print(x < 5 or x == 7)
print(not (x > 5))
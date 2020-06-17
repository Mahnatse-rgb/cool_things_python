import random

def lottery():
    #Print 7 rendom numbers between 1 and 49
    for i in range(7):
        yield random.randint(1,49)

for random_number in lottery():
    print(f"random number is ...: {random_number}")

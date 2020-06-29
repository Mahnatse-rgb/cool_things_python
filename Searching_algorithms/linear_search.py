# find the position of 7 in the array of 10 numbers

array = [7,9,4,7,3,56,78,94,10,44]
target =  7

print(f"In an arrary of {array} :")
found = False
def linear_sort(array, target):
    for i in range(len(array)):
        if array[i] == target:
            found = True
            print(f"{target} is on position {i}")

    if not found:
        print(f"{target} not found")

linear_sort(array, target)

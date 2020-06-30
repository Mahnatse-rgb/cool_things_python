def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

lst = [90,7,83,290,632,1,0,20]
print(f"The list contains the following numbers : {lst}")
bubble_sort(lst)
print(f"The Sorted list is as follows: {lst}")

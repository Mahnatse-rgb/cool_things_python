def fib():
    a,b = 1,1
    while 1:
        yield a
        a,b = b,a + b

#test function type
import types
if type(fib()) == types.GeneratorType:
    print("Awesome, this function is a generator")

    counter = 0
    for value in fib():
        print(value)

        counter +=1
        if counter == 10:
            break

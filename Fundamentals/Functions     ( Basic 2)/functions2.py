#Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number
#  (as the 0th element) down to 0 (as the last element).

def fun1(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list
y=fun1(10)
print(y)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def fun2(arr):
    print(arr[0])
    return arr[1]
fun2([2,3])

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def fun3(arr):
    y=arr[0]+len(arr)
    print(y)
    return y
fun3([1,2,3,4,5])

# Values Greater than Second - 
# Write a function that accepts a list and creates a new list containing only the values 
# from the original list that are greater than its 2nd value.
#  Print how many values this is and then return the new list. If the list has less than 2 elements, 
#  have the function return False

def fun4(arr):
    new=[]
    if(len(arr)<2):
        return False
    for i in range(0,len(arr),1):
        if(arr[i]>arr[1]):
            new.append(arr[i])
    print(len(new))
    return new
print(fun4([2]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.

def fun5(size,value):
    new=[]
    for i in range(0,size,1):
        new.append(value)
    return new
fun5(6,2)

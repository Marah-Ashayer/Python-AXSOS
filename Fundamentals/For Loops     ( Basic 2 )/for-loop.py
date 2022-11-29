# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big"

def fun1(arr):
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            arr[i]="big"
    print(arr)
fun1([-1,4,6,-4,-3])

# Count Positives - Given a list of numbers,
#  create a function to replace the last value with the number of positive values.
#   (Note that zero is not considered to be a positive number).

def fun2(arr):
    count=0
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            count=count+1
    arr[len(arr)-1]=count
    print (arr)
fun2([2,4,7,-2,-3,5,-1])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.

def fun3(arr):
    sum=0
    for i in range(0,len(arr),1):
        sum=sum+arr[i]
    print(sum)
    return sum
fun3([1,2,3,4])

# Average - Create a function that takes a list and returns the average of all the values.x

def fun4(arr):
    sum=0
    for i in range(0,len(arr),1):
        sum=sum+arr[i]
    return(sum/len(arr))
fun4([1,2,3,4])

# Length - Create a function that takes a list and returns the length of the list.

def fun5(arr):
    return len(arr)
fun5([2,8,0,-4,-2])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.

def fun6(arr):
    min=arr[0]
    for i in range(1,len(arr),1):
        if(arr[i]<min):
            min=arr[i]
    if(arr==[]):
        return False
    return min
fun6([])

# Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.

def fun7(arr):
    max=arr[0]
    for i in range(1,len(arr),1):
        if(max<arr[i]):
            max=arr[i]
    if(arr==[]):
        return False
    return max
fun7([2,0,-4,3,10,5])

# Ultimate Analysis - Create a function that takes a list 
# and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def fun8(arr):
    new={}
    sum=0
    min=arr[0]
    max=arr[0]
    for i in range(0,len(arr),1):
        sum=sum+arr[i]
        if(arr[i]<min):
            min=arr[i]
        if(max<arr[i]):
            max=arr[i]
    new['sum']= sum
    new['avg']= sum/len(arr)
    new['min']=min
    new['max']= max
    new['len(arr)']= len(arr)
    return new

print(fun8([1,2,3,4]))

# Reverse List - Create a function that takes a list and return that list with values reversed.

def fun9(arr):
    for i in range(0,int(len(arr)/2),1):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    return arr
print(fun9([2,0,7,3]))






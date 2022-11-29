import random
def randInt(min=0,max=1000):
    num=int(random.random() * (max-min) + min)
    return num
print(randInt(0,1))
print(randInt(min=0,max=50))
print(randInt(min=50,max=100))
print(randInt(min=50,max=500))

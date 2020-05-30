import random
a = list(range(10))
b = [random.randint(-5,5) for x in a]
c = random.randrange(1,10)

thisIsAList = a[:]


print("This is just a test!")
a1 = [ x * x for x in a]
print(a)
print(a[0:4:2])
print(a1)
random.shuffle(a)
print("Random shuffle function on 'a'",a)
print(b)
print(c)
print(random.sample(range(1,100),5))
print(thisIsAList)

import random
a = list(range(5))
b = [random.randint(-5,5) for x in a]
c = random.randrange(1,10)
a1 = [ x * x for x in a]
thisIsAList = a[:]


print("This is just a test!")
print("Normal list(a):", a )
print("Item 1 and 3 of list(a):", a[0:4:2])
print("List(a) squared:", a1)
random.shuffle(a)
print("Random shuffle function on 'a'",a)
print(b)
print(c)
print(random.sample(range(1,100),5))
print(thisIsAList)

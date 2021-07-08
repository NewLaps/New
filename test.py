from heapq import merge
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
print(thisIsAList *2)

print ("Hello")
# merge two arrays


#print merged array
def listMerge(array1,array2):
    a = list(merge(array1,array2))
    print(a)


alist1 = [0,1,2,3]
blist1 = [6,7,8,9]
listMerge(alist1, blist1)

listMerge(a1, b)

print(a,b,c)


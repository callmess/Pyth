li = list(range(1,11))
#print(li)
li2=[ x*x for x in range(10)]
li3=( x*x for x in range(10))
print(next(li3));
#print(next(li3));
for a in li3:
    print(a)
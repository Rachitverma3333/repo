l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(0, len(l)):
    if l[i]%2==0:
        l[i] = l[i]**2
    else:
        l[i] = l[i]**3
print(l)        
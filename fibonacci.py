a = int(input("Enter no. of terms : "))
n = 0
n1 = 1
count = 0
while count <a:
    print(n)
    s = n + n1
    n = n1
    n1 = s
    count += 1
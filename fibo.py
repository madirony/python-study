n = int(input())
number = [0,1]
def fibo(n):
    i=0
    for i in range(0,n,1):
        number.append(number[i]+number[i+1])
        i+=1

fibo(n)
t=0
while t<2:
    number.pop(n)
    t+=1
print(number)

select=[9,5,3,4,8,1,0,2,6,7]
b=0
min=0
t=0
while b<10:
    while min<10:
        if select[b] < select[min] :
            t=select[b]
            select[b] = select[min]
            select[min] = t
            min+=1
            print(select)
        else:
            min+=1
            print(select)
    b+=1
    min=0
        
c=len(select)
while True:
    print(select[0])
    select.pop(0)
    c-=1
    if c==0:
        break;
    
print(select)
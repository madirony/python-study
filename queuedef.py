queue=[]
def enqueue(queue):
    b=0
    while b<10:
        queue.append(input())
        b+=1
    return queue

def dequeue (queue):
    c=5
    while c != 0:
        queue.pop(0)
        c-=1
    
    return queue
        
        
def list_queue (queue):
    print(queue)
    
    
enqueue(queue)
list_queue(queue)
dequeue(queue)
list_queue(queue)
stack=[]
def pushstack(stack):
    b=0
    while b<10:
        stack.insert(0,input())
        b+=1
    return stack

def popstack (stack):
    c=5
    while c != 0:
        stack.pop(0)
        c-=1
    
    return stack
        
        
def list_stack (stack):
    print(stack)
    
    
pushstack(stack)
list_stack(stack)
popstack(stack)
list_stack(stack)
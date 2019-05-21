class stack:
    def __init__(self):
        self.stack_items=[]
    
    # pop 기능 구현
    def pop(self):
        item_length=len(self.stack_items)
        # 스택이 비어있을때는 에러메세지 출력
        if item_length < 1:
            print("Stack is empty!")
            return False
        # 가장 위에 있는 item을 반환하며 삭제
        result = self.stack_items[item_length-1]
        del self.stack_items[item_length-1]
        return result
    
    # push 기능 구현
    def push(self,x):
        self.stack_items.append(x)
        
    # isEmpty 기능 구현
    def isEmpty(self):
        return not self.stack_items
# 테스트 코드
test1 = stack()
print(test1.stack_items)
test1.push(3)
print(test1.stack_items)
test1.push(5)
test1.push(7)
test1.push(9)
test1.push(11)
print(test1.stack_items)
print(test1.isEmpty())
print(test1.pop())
print(test1.pop())
print(test1.pop())
print(test1.pop())
print(test1.pop())
print(test1.pop())
print(test1.isEmpty())

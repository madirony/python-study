class Stack: # 고정길이 Stack 클래스
    def __init__(self): #인스턴트 생성 초기에 변수를 지정해주는 생성자
        self.stacklist = [] #스택리스트
        self._stackln = 0 #크기 변수의 디폴트 값

    def push(self,i):#Stack push
        self.stacklist.append(i) #리스트에 숫자를 넣습니다.
        
    def pop(self): #Stack pop
        slen=len(self.stacklist) #스택의 길이를 저장합니다.
        result = self.stacklist[slen-1] #리스트 인덱싱을해서 나중에 들어온 숫자를 뽑습니다.
        print(self.stacklist)
        self.stacklist.remove(slen-1) #뽑은 값은 바로바로 지워줍니다.
        return result #뽑은 결과를 print(stacks.pop())에서 보여줍니다.
    
    @property
    def stackln (self): #크기를 설정하는 클래스 멤-버
        return self._stackln
    @stackln.setter #가변길이 스택 (값을 입력 받았을때..)
    def stackln (self,new):
        self._stackln = new
         
    
    
stacks=Stack() #객체 stacks를 만듭니다.
print(stacks.stacklist) #빈 스택리스트 입니다.
stacklen = 10 #스택의 크기를 저장합니다.
i=0 #push를 반복문으로 여러번 반복하기 위해 만든 변수 i
while True:
    stacks.push(i) #0부터 순서대로 값을 넣습니다.
    i +=1        
    if i == stacklen: #10개의 데이터를 넣었으면 반복문을 종료합니다.
        print("데이터는 10개의 값만 넣을 수 있습니다.")
        break;
print("리스트", stacks.stacklist) #push된 리스트를 출력합니다.

while True:
    print(stacks.pop()) #pop을 하는 반복문
    stacklen -= 1
    if stacklen == 0: #10개의 데이터를 pop했을때 반복문을 종료합니다.
        print("더이상의 데이터가 존재하지 않습니다..!")
        break;



fstack = Stack() #가변길이 stacks를 만듭니다.
print(fstack.stacklist) #빈리스트 출력
fstack.stackln = int(input("스택의 길이를 정해주세욤:")) #스택의 길이를 정합니다.
flen = fstack.stackln #길이를 정했습니다-!
i=0
while True:
    fstack.push(i) #0부터 순서대로 값을 넣습니다.
    i +=1        
    if i == flen: #가변길이로 설정한 데이터 범위까지 데이터를 모두 넣었으면 반복문을 종료합니다.
        print("데이터 범위 이탈...!")
        break;
print("리스트", fstack.stacklist) #push된 리스트를 출력합니다.

while True:
    print(fstack.pop()) #pop을 하는 반복문
    flen -= 1
    if flen == 0: #가변길이로 설정한 데이터를 모두 pop했을때 반복문을 종료합니다.
        print("더이상의 데이터가 존재하지 않습니다..!")
        break;
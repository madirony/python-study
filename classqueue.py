class Queue: # 고정길이 Queue 클래스
    def __init__(self): #인스턴트 생성 초기에 변수를 지정해주는 생성자
        self.queuelist = [] #큐 리스트
        self._queueln = 0 #큐 크기변수 디폴트 값 False

    def push(self,i):#Queue push
        self.queuelist.append(i) #리스트에 숫자를 넣습니다.
        
    def pop(self): #queue pop
        qlen=0 #FIFO으로 뽑아줍니다.
        result = self.queuelist[qlen] #리스트 인덱싱을해서 먼저 들어온 숫자를 뽑습니다.
        print(self.queuelist)
        del self.queuelist[qlen] #뽑은 값은 바로바로 지워줍니다.
        return result #뽑은 결과를 print(queues.pop())에서 보여줍니다.

    @property
    def queueln (self): #크기를 설정하는 클래스 멤-버
        return self._queueln

    @queueln.setter #가변길이 스택 (값을 입력 받았을때..)
    def queueln (self,new):
        self._queueln = new         
    
    
queues=Queue() #객체 queues를 만듭니다.
print(queues.queuelist) #빈 큐리스트 입니다.
queuelen = 10 #리스트의 고정길이는 10 입니다.
i=0 #push를 반복문으로 여러번 반복하기 위해 만든 변수 i
while True:
    queues.push(i) #0부터 순서대로 값을 넣습니다.
    i +=1        
    if i == queuelen: #10개의 데이터를 넣었으면 반복문을 종료합니다.
        print("데이터는 10개의 값만 넣을 수 있습니다.")
        break;
print("리스트", queues.queuelist) #push된 리스트를 출력합니다.

while True:
    queuelen -= 1
    print(queues.pop()) #pop을 하는 반복문
    if queuelen == 0: #10개의 데이터를 pop했을때 반복문을 종료합니다.
        print("더이상의 데이터가 존재하지 않습니다..!")
        break;

    
    
fqueue = Queue() #가변길이 queue를 만듭니다.
print(fqueue.queuelist) #빈리스트 출력
fqueue.queueln = int(input("큐의 길이를 정해주세욤:")) #큐의 길이를 정합니다.
flen = fqueue.queueln #길이를 정했습니다-!
i=0
while True:
    fqueue.push(i) #0부터 순서대로 값을 넣습니다.
    i +=1        
    if i == flen: #가변길이로 설정한 데이터 범위까지 데이터를 모두 넣었으면 반복문을 종료합니다.
        print("데이터 범위 이탈...!")
        break;
print("리스트", fqueue.queuelist) #push된 리스트를 출력합니다.

while True:
    print(fqueue.pop()) #pop을 하는 반복문
    flen -= 1
    if flen == 0: #가변길이로 설정한 데이터를 모두 pop했을때 반복문을 종료합니다.
        print("더이상의 데이터가 존재하지 않습니다..!")
        break;
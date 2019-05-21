class Person:
    def __init__(self,name,age,gender):
        self._name = name
        self._age = age
        self._gender = gender
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,newName):
        self._name = newName
        
if __name__ == "__main__": #매직 메쏘드 (예약이 되어있음 if네임은 main있잖아요)
    #파일이 직접 실행될때만 실행되는 부분 #예약어 몇개 있는데 중요한거 몇개 배우고 가려고해요
    #이터레이터랑 제너레이터를 알아야할거 같아서 이터레이터라는건 리스트나 셀이나 이런거 셀 수 있는 집합
    #fiboclass.py에서 실습해봄
    #제너레이터 설명해볼게요 피보나치를 할때 이렇게도 할 수 있는데 yield 를 사용해서 값을 반환해 줄 수도 있어요
    #리턴값이 따로없잖아요 옐드를 두고 하면 아까랑 같이 피보나치 출력이 돼요
    #
    m1 = Person("연정흠",23,"남") #property
    w2 = Person("이지은",25,"여")
    w2.name = "아이유" #setter
    print(m1.name) #m1만 하면 오브젝트 값을 출력하는거고 m1.name이라 해야함
    print(w2.name) # 이 역시 마찬가지
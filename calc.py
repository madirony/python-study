def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#얘네들은 네임스페이스가 main일때만 실행되게해서 import해서 안됨
#테스트 코드가 가려지기 위해서
if __name__ == "__main__":
    print(add(1,3))
    print(sub(1,3))
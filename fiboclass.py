class fio():
    def __init__(self):
        self.prv = 0
        self.cur = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cur, self.prv = self.cur+self.prv, self.cur
        return self.prv
    
f = fio()
for i in range(10):
    print(next(f))
    
    
    
    
class fib():
    def __init__(self):
        self.prv = 0
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cur, self.prv = self.cur+self.prv, self.cur
        return self.prv

f = fib()
for i in range(10):
    print(next(f))
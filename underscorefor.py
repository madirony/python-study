wordList1 =["apple","app","agile","aside","appendix","ace","append","attension","age"]
wordList2 =["duck","cat","pizza","chicken","elephant","mouse","fence"]
wordList = wordList1 + wordList2

#original code
for each in wordList:
    if each.startswith("a"):
        print(each)

#list comprehension
myList = [each for each in wordList if each.startswith("a")]
print(myList)

myList = [0 for _ in range(100)]
print(myList)

print(len(myList))

myList = [i for i in range(100)]
print(myList)
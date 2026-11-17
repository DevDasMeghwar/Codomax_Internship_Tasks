# studentsNames = ['Dev','Riya','Sagar','Priya','Akash']

# for name in studentsNames:
#     print(name)

# num = [10,45,22,50,100,11,43,78,95,9]

# sum = 0
# for val in num:
#     sum = sum+val
# print('sum these numbers are ',sum)

# NumList = [12,53,76,24,87]

# largestNum = NumList[0]
# smallestNum = NumList[0]

# for num in NumList:
#     if num>largestNum:
#         largestNum=num
#     if num<smallestNum:
#         smallestNum=num
# print('largest number is = ',largestNum)
# print('smallest number is = ',smallestNum)

# isEvenFreq = 0

# for num in NumList:
#     if (num%2==0):
#         isEvenFreq+=1
# print('Total even numbers are = ',isEvenFreq)
# isOdd_freq = len(NumList) - isEvenFreq
# print('Total odd number ',isOdd_freq)

newList = []
for num in range(1,6):
    val = int(input('enter the value: '))
    newList.append(val)

print(sorted(newList))

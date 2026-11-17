# def LargestOneNum(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c

# ans = LargestOneNum(4,7,1)
# print(ans)

def isPrime(num):
    flag = False
    for val in range(2,num+1//2):
        if(num%val==0):
            flag = True
    return flag

val = int(input('Enter a integer number: '))

ans = isPrime(val)
if(ans==True):
    print('Number is not Prime')
else:
    print('Number is Prime')

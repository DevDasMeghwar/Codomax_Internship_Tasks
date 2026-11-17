for i in range(1,21):
    print(i)

count = 0
while count<=50:
    if(count%2==0):
        print(count)
    count+=1

num = int(input('Enter any integer number: '))

ans = 1
for val in range(1,num+1):
    ans = ans*val

print(ans)





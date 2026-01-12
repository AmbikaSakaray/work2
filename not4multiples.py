#problem statements....

##1>print(1 - 20) which are not multiples of 4


for i in range(1, 21):
    if i % 4 != 0:
        print(i)
 
for i in range(1,10):
    if i%2 != 0:
        print(i, end=' ')
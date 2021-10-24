n=int(input().rstrip())
for i in range(1, n+1):
    count=[0, 0, 0]
    res=list(map(int, input().split(" ")))
    for j in range(0, len(res)):
        count[res[j]]+=1
    if(count[1]>count[2]):
        print("INDIA")
    elif(count[1]<count[2]):
        print("ENGLAND")
    else:
        print("DRAW")

# cook your dish here
n=int(input().rstrip()) # number of test cases
for i in range(1, n+1):
    a, b, c=map(int, input().split(" ")) # The three digits of the lottery tickets
    if a==7 or b==7 or c==7: # to be lucky, at least one digit should be 7
        print("YES")
    else:
        print("NO")

# 이코테 그리디 알고리즘
# 큰 수의 법칙

N,M,K=map(int,input().split())

nums=list(map(int,input().split()))
nums=sorted(nums)
result=0
count=0
while count<M:
    for i in range(K):
        result+=num[-1]
        count+=1
    if count<M:
        result+=num[-2]
print(result)
# 이코테 다이나믹 프로그래밍
# 1로 만들기

# 정수 X를 입력받기
x=int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[0]*30001

# 다이나믹 프로그래밍 진행(BottomUP)
for i in range(2,x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i]=d[i-1]+1
    # 현재의 수가 2,3,5,로 각각 나누어 떨어지는 경우 현재의 값 갱신
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])

# Insertion_sort
lst=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(lst)):
    for j in range(i,0,-1): # i부터 1까지 1씩 감소하며 반복
        if lst[j]<lst[j-1]:
            lst[j],lst[j-1]=lst[j-1],lst[j] # 바로 앞과 매번 비교하면서 자신이 더 작으면 바꿈
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(lst)

# 정수 n, m 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
arr = []
for i in range(n):
    arr.append(int(input()))
    
# DP 테이블 초기화
d = [10001] * (m + 1)

# Dynamic Programming
d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001:  #(i-k를 만드는 방법이 존재하는 경우)
            d[j] = min(d[j], d[j-arr[i]] + 1)
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
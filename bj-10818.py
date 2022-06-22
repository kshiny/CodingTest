n = int(input())
arr_list = list(map(int, input().split()))

max_num = arr_list[0]
min_num = arr_list[0]

# 최댓값과 최솟값을 찾기 위해서 배열 안에 수들을 하나하나 순회한다.
for num in arr_list:
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
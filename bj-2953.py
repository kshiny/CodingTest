human = [list(map(int, input().split())) for _ in range(5)]
humanScore = [0]*5 # 참가자들의 총합 점수를 저장하기 위한 배열 생성
score = 0 # 최대 점수 저장
for i in range(5): # 0부터 4까지 for문을 탐색해 참가자들을 순회
    sum = 0 # 참가자의 점수를 저장하기 위한 변수 sum
    for j in range(4): # 4번의 평가
        sum += human[i][j]
    humanScore[i] = sum
    score = max(score, sum) # 점수의 최댓값을 score에 저장
    
for i in range(5): # 참가자의 총 점수가 최대 점수라면 i+1, score를 출력
    if humanScore[i] == score:
        print(i+1, score)
        break
        
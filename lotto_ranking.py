def solution(lottos, win_nums): #lottos는 민우가 구매한 로또 번호, win_nums는 당첨 번호
    answer = [] # 최고순위, 최저 순위 
    win_times=0 # 확실하게 이긴 횟수
    zero_num=lottos.count(0) # 알아볼 수 없는 번호의 개수
    for i in range(6):
        for j in range(6):
            if lottos[i]==win_nums[j]:
                win_times+=1
    answer.append(6-(win_times+zero_num)+1) # 최고순위를 저장
    if answer[0]>=6: # answer[0]이 6 이상 나오면 6으로 저장
        answer[0]=6
    answer.append(6-win_times+1) # 최저순위를 저장
    if answer[1]>=6: # answer[1]이 6 이상 나오면 6으로 저장
        answer[1]=6
    print(answer)
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
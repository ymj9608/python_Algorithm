# 오늘 푼 알고리즘
## 백준 1244 스위치 켜고 끄기 실버4 부분 해결
```python
N = int(input())
switch = list(map(int, input().split()))
number_of_student = int(input())

for _ in range(number_of_student):
    gender_switch = list(map(int, input().split()))
    if gender_switch[0] == 1:
        k = gender_switch[1]
        for i in range(k, N + 1, k):
            switch[i - 1] = 1 - switch[i - 1]
    else:
        k = gender_switch[1]
        switch[k - 1] = 1 - switch[k - 1]
        for j in range(1, min(k - 1, N - k) + 1):
            if switch[k - j - 1] == switch[k + j - 1]:
                switch[k - j - 1] = 1 - switch[k - j - 1]
                switch[k + j - 1] = 1 - switch[k + j - 1]
            else:
                break

elements_per_line = 20

for index, item in enumerate(switch):
    print(item, end=" ")
    if (index + 1) % elements_per_line == 0 and (index + 1) != len(switch):
        print()
```
- 코드리뷰  
남학생인 경우는 맞았지만, 여학생의 경우 대칭이 아니면 멈춰야 하는데 else: break를 빠뜨림. 조건 생각하고, 다양한 case 확인하기  
아래 한줄에 20개씩 출력하는 코드 외우기
```python
switch = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
elements_per_line = 20
for index, item in enumerate(switch):
    print(item, end=" ")
    if (index + 1) % elements_per_line == 0 and (index + 1) != len(switch):
        print()
'''
출력결과
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 0 1 
'''
```
---
# 백준 2628 종이자르기 실버5 해결 완료
```python
width, length = map(int, input().split()) # 가로, 세로 길이 입력
number_of_cut = int(input()) # 자르는 횟수 입력
width_cut = [0] # 가로 자르기 번호 리스트, 최댓값을 구하기 위해 0도 추가
length_cut = [0] # 세로 자르기 번호 리스트, 최댓값을 구하기 위해 0도 추가
width_max = 0 # 자른 가로 최대 길이 초기값
length_max = 0 # 자른 세로 최대 길이 초기값

for _ in range(number_of_cut): # 자른 횟수만큼 입력하기 위해 for문 작성
    direction, number = map(int, input().split()) # 자르는 방향, 자르는 번호
    if direction == 1: # 자르는 방향이 1이면 세로
        length_cut.append(number) # 세로 자르기 번호 리스트에 추가
    else: # 자르는 방향이 0이면 가로
        width_cut.append(number) # 가로 자르기 번호 리스트에 추가
    length_cut.sort() # 세로 번호 정렬
    width_cut.sort() # 가로 번호 정렬

length_cut.append(width) # 세로 자르기 번호에 가로 길이 추가 (ex 가로 길이 10이고 세로 자르기 2, 5, 8일 때, length_cut = [0, 2, 5, 8, 10])
width_cut.append(length) # 가로 자르기 번호에 세로 길이 추가 (ex 세로 길이 8이고 가로 자르기 1, 3, 6일 때, width_cut = [0, 1, 3, 6, 8])

for i in range(len(length_cut) - 1): # length_cut에서 각 항과 이전항의 차이가 가장 큰값을 length_max로 선택)
    m = length_cut[len(length_cut) - i - 1] - length_cut[len(length_cut) - i - 2]
    if m > length_max:
        length_max = m

for j in range(len(width_cut) - 1): # width_cut에서 각 항과 이전항의 차이가 가장 큰값을 width_max로 선택)
    k = width_cut[len(width_cut) - j - 1] - width_cut[len(width_cut) - j - 2]
    if k > width_max:
        width_max = k

print(length_max * width_max) # length_max * width_max의 값이 자른 종이의 넓이의 최댓값이 됨
```
---  
# 백준 1181 단어 정렬 실버5 정렬은 했으나 시간 초과 lambda 함수를 이용하여 추후 해결
```python
N = int(input())
my_list = []
for _ in range(N):
    word = input()
    my_list.append(word)

unique_words = list(set(my_list))

unique_words.sort(key=lambda x: (len(x), x))

for word in unique_words:
    print(word)
```
- 코드 리뷰  
.sort(key = lambda x: ~ ) 아래와 같이 사용
```python
# 숫자 리스트 정렬 (오름차순)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(key=lambda x: x)
print(numbers)  # 출력: [1, 1, 2, 3, 4, 5, 6, 9]

# 숫자 리스트 정렬 (내림차순)
numbers.sort(key=lambda x: -x)
print(numbers)  # 출력: [9, 6, 5, 4, 3, 2, 1, 1]

# 튜플 리스트 정렬 (첫 번째 요소 기준 오름차순, 두 번째 요소 기준 내림차순)
data = [(1, 5), (1, 2), (2, 3)]
data.sort(key=lambda x: (x[0], -x[1]))
print(data)  # 출력: [(1, 5), (1, 2), (2, 3)]
```
---
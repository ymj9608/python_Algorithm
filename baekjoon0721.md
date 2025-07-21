# 오늘 푼 알고리즘
## 백준 2635 수 이어가기 실버5 해결 완료
```python
N = int(input())
my_list = [N]
if N == 1:
    print(4)
    print(1, 1, 0, 1)
elif N == 2:
    print(5)
    print(2, 1, 1, 0, 1)
elif N == 3:
    print(6)
    print(3, 2, 1, 1, 0, 1)
else:
    new_my_list = [N, 1]
    for i in range(2, new_my_list[0] + 1):
        k = new_my_list[i-2] - new_my_list[i-1]
        new_my_list.append(k)
        if k <= 0:
            del new_my_list[-1]
            break

    for i in range(2, my_list[0] + 1):
        my_list.append(i)
        for j in range(2, my_list[0] + 1):
            k = my_list[j-2] - my_list[j-1]
            my_list.append(k)
            if k < 0:
                del my_list[-1]
                break
        if len(my_list) > len(new_my_list):
            new_my_list = my_list
            my_list = [N]
        else:
            my_list = [N]

    print(len(new_my_list))
    print(' '.join(map(str, new_my_list)))
```
- 코드리뷰  
  - N이 1, 2, 3인 case를 생각안했음. 항상 처음 case를 조심하고 Test해보기  
  - 0도 포함인데, 생각 안했음. 조건 꼭 다시 확인하기  
  - 리스트를 대괄호 없이 띄어쓰기로 출력하는 아래 코드 기억하기  
print(' '.join(map(str, new_my_list)))  
---

## 백준 2669 직사각형 네개의 합집합의 면적 구하기 (실버5) 실패
```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = []

for i in range(101):
    arr.append([])
    for j in range(101):
        arr[i].append(0)

x1 = a[0]
x2 = a[2]
y1 = a[1]
y2 = a[3]

for y in range(y1, y2):
    for x in range(x1, x2):
        arr[y][x] = 1

x1 = b[0]
x2 = b[2]
y1 = b[1]
y2 = b[3]

for y in range(y1, y2):
    for x in range(x1, x2):
        arr[y][x] = 1

x1 = c[0]
x2 = c[2]
y1 = c[1]
y2 = c[3]

for y in range(y1, y2):
    for x in range(x1, x2):
        arr[y][x] = 1

x1 = d[0]
x2 = d[2]
y1 = d[1]
y2 = d[3]

for y in range(y1, y2):
    for x in range(x1, x2):
        arr[y][x] = 1

total_area = 0

for row in arr:
    total_area += row.count(1)

print(total_area)
```
- 코드리뷰  
2차원 배열 문제로 코드를 하나하나 확인하며 다시 생각해볼 것
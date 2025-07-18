# 오늘 푼 알고리즘
```python
# 백준 2869 달팽이는 올라가고 싶다 (브론즈1)
import math
A, B, V = map(int, input().split())

print(math.ceil((V - A) / (A - B)) + 1)
```

```python
# 백준 14626 ISBN (브론즈1) 런타임 오류
# ISBN 코드를 리스트로 입력받습니다.
isbn_list = list(input())

# '*'의 위치(인덱스)를 찾습니다.
star_index = isbn_list.index('*')

# '*'를 제외한 나머지 숫자들의 가중치 합을 계산합니다.
total_sum = 0
for i in range(13):
    # '*' 문자는 건너뜁니다.
    if i == star_index:
        continue

    digit = int(isbn_list[i])

    # 위치(1부터 시작)에 따라 가중치를 적용합니다.
    # 홀수 번째는 1, 짝수 번째는 3을 곱합니다.
    if (i + 1) % 2 != 0:
        total_sum += 1 * digit
    else:
        total_sum += 3 * digit

# '*' 위치의 가중치를 결정합니다 (홀수 위치: 1, 짝수 위치: 3).
star_weight = 1 if (star_index + 1) % 2 != 0 else 3

# 0부터 9까지의 숫자를 '*' 자리에 대입해봅니다.
for m in range(10):
    # (기존 합계 + '*' 자리에 들어갈 숫자 * 가중치)가 10의 배수인지 확인합니다.
    # ISBN-13 유효성 검사 공식: (전체 가중치 합) % 10 == 0
    if (total_sum + m * star_weight) % 10 == 0:
        # 조건을 만족하는 숫자를 찾으면 출력하고 반복을 종료합니다.
        print(m)
        break
```

# 코드리뷰
ISBN 문제에서 런타임 오류가 발생했다. 우선 m을 구하는 방식에 대해 고민하고, if와 for문을 최소화하여 코드를 구성하는 것이 시간복잡도를 줄이는 방법이니 고민해볼 것.
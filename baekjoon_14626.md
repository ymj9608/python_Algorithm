# 오늘 배운것

```python
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
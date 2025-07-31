# 백준 2839번 설탕 배달
N = int(input())

# 5로 나누어 떨어지면 N/5이 최솟값
if N % 5 == 0:
    print(int(N/5))

# 5로 나누어 떨어지지 않으면 for문으로
# N을 N보다 작은 가장 큰 5의 배수부터 빼보면서
# 그 값이 3으로 나누어떨어지는지 체크
# 3으로 나누어떨어지면 최솟값 출력하고 break
# for문 다 돌렸는데 전부 3으로 안나누어떨어지면 -1 출력
else:
    is_num = False
    for i in range(N // 5 + 1):
        if (N - 5 * (N // 5 - i)) % 3 == 0:
            is_num = True
            result = int((N // 5 - i + ((N - 5 * (N // 5 - i)) // 3)))
            print(result)
            break

    if is_num is False:
        print(-1)
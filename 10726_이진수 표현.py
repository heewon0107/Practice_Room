# # for i in range(1 << 12):
# #     for j in range(12):
# #         if i & (1 << j):
#
# to_bn = {
#     "0" : "0000",
#     "1" : "0001",
#     "2" : "0010",
#     "3" : "0011",
#     "4" : "0100",
#     "5" : "0101",
#     "6" : "0110",
#     "7" : "0111",
#     "8" : "1000",
#     "9" : "1001",
#     "A" : "1010",
#     "B" : "1011",
#     "C" : "1100",
#     "D" : "1101",
#     "E" : "1110",
#     "F" : "1111",
# }
# '''
# 5
# 4 0
# 4 30
# 4 47
# 5 31
# 5 62
#
# '''
#
# T = int(input())
# for tc in range(1, T+1):
#     # M의 이진수 표현의 마지막 N 비트가 모두 켜져있는가
#     N, M = map(int, input().split())
#     bn = bin(M)
#     result = "ON"
#
#     for i in range(-1, -1-N, -1):
#         if bn[i] == "0":
#             result = "OFF"
#             break
#
#     print(f"#{tc} {result}")

T = input()
for _ in range(T):
    A, B, N = map(int, input().split())
    cnt = 0
    if A > B:
        while A < N and B < N:
            for t in range(2):
                if t == 0:
                    B += A
                else:
                    A += B
                cnt += 1
                if not A < N and not B < N:
                    break

def backtrack(a, k, n):  # a = 주어진 배열, k 결정할 원소,  n = 원소개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):
    in_perm = [False] *(NMAX + 1)
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=" ")
        print()


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1, 2, 3, 4]
backtrack(a, 0, 3)

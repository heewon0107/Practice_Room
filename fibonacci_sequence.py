def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
fibo_n = []
n = int(input("피보나치의 n번째 값을 입력하세요 :"))
for i in range(n):
    fibo_n.append(fibo(i))
print(f"피보나치 수열 : {fibo_n}")
print(*fibo_n)
print(f"{n}번째의 피보나치 수 : '{fibo_n[n-1]}'")



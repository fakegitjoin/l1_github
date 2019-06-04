def fibo(num):
	if num == 2 or num == 1:
		return 1
	return fibo(num-1) + fibo(num-2)

result = fibo(6)
print(result)

n,k = input().split()
res = 0
x = 0
y = 0
arr = []
i = 0

while i < int(n):
	a = input()

	arr.append(a)

	i += 1

z = 0
a = 0
while z < int(n):
	if arr[int(a)] > 5:
		res += 1
	elif arr[a] < 5:
		pass

	z += 1

print(arr)
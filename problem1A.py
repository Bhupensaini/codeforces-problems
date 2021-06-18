import math

n,m,a = map(int, input().split())
ans=0

if (n*m)%(a*a)!=0 or (n*m)>(a*a):
	i=math.floor(n/a)+1
	j=math.floor(m/a)+1
	ans=i*j
else:
	ans = math.floor((n*m)/(a*a));

print(ans)
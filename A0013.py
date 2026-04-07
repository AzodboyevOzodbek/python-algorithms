n = int(input())

n = n % (24 * 3600)

h = n // 3600
m = (n % 3600) // 60
s = n % 60

print(f"{h}:{m:02}:{s:02}")
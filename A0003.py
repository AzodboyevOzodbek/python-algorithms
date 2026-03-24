a = list(map(int, input().split()))

jami = sum(a)
min_sum = jami - max(a)
max_sum = jami - min(a)

print(min_sum, max_sum)
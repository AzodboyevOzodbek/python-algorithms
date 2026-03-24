import math
a , b , c = map(int, input().split())
sinf1 = math.ceil (a / 2)
sinf2 = math.ceil(b / 2)
sinf3 = math.ceil(c / 2)
print(sinf1 + sinf2 + sinf3)
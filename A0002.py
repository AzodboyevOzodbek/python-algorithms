y = int(input())

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print(f"12/09/{y:04d}")
else:
    print(f"13/09/{y:04d}")
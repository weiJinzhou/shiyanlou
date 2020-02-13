for i in range(1,101):
    x = i % 7
    y = i % 10
    z = int(i / 10)
    if x == 0 or y == 7 or z ==7:
        continue
    print(i)

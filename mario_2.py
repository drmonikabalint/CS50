Height = input("Height:")
count = int(Height)

for i in range (1, count+1):
    count_space = count-i
    print(" "*count_space, "#"*i, "#"*i )

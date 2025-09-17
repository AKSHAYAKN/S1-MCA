list1 = input("List 1 colors:").split(',')
list2 = input("List 2 colors:").split(',')
for color in list1:
    if color not in list2:
        print(color.strip())

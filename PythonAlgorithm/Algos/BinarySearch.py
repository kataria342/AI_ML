ls = [2, 3, 1, 6, 34, 65, 13, 24, 36, 78, 96, 23, 67, 90, 1]
beg = 0;
end = int(len(ls)-1)

ls.sort()
print(ls)
flag = True
mid = int((beg + end) / 2)

item = int(input("Enter the number to search: \n"))
while beg <= end:
    if ls[mid] == item:
        flag = False
        print(item, "Item found at", mid, "value")
        break
    elif ls[mid] < item:
        beg = int(mid + 1)
        mid = int((beg + end) / 2)
    elif ls[mid] > item:
        end = int(mid - 1)
        mid = int((beg + end) / 2)
    else:
        break

if flag:
    print("Item not found in list")

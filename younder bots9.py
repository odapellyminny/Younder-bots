list1 = list(map(int, input("Enter elements of list 1 separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of list 2 separated by spaces: ").split()))
intersection = list(set(list1) & set(list2))
print("Common elements (Intersection):", intersection)
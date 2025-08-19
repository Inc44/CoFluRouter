with open("lists/list1.txt", "r") as file1, open("lists/list2.txt", "r") as file2:
	list1 = set(file1.readlines())
	list2 = set(file2.readlines())

assert list1 == list2, "Lists do not match"

with (
	open("lists/list1.txt", "r", encoding="utf-8") as file1,
	open("lists/list2.txt", "r", encoding="utf-8") as file2,
):
	list1 = set(file1.readlines())
	list2 = set(file2.readlines())
diffs = list1.symmetric_difference(list2)
for name in sorted(diffs):
	print(name)

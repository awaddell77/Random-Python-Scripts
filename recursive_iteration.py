
#recursive iteration

lst = [i for i in range(0,20)]

def recursive_iteration(lst):
	print(lst[0])
	if len(lst) <= 1: return
	recursive_iteration(lst[1:])


recursive_iteration(lst)
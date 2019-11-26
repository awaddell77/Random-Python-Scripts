#function that produces binary representation of decimal numbers recursively
def num_to_bin(num):
	#when num is zero then the process is over
	if num < 1: return ''
	return  num_to_bin(num//2) + str(num % 2)
if __name__ == "__main__":
	test_n = 122
	res_n = num_to_bin(test_n)
	print("Number is {0}. It's binary represention is: {1} .".format(test_n, res_n))

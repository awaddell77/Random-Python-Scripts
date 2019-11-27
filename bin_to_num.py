#bin to num

def bin_to_num(b_str, signed = False):
	total = 0
	end = -1
	if signed: end = 0 
	for i in range(len(b_str)-1, end,-1):
		b_len = len(b_str)-1
		if b_str[i] != "0": total += 2**(b_len-i)
	if signed and b_str[0] == "1": total *= -1


	return total

test_val = '1000'
test_val_neg = '11000'
res = bin_to_num(test_val)
res_s = bin_to_num(test_val_neg, True)
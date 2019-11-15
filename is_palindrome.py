
def is_palindrome(word):
	print("Checking ", word)
	if len(word) <= 1: return True

	if word[0] == word[-1]:
		return is_palindrome(word[1:len(word)-1])
	return False
#res = is_palindrome("bob")
words = ['nuclear', 'hannah', 'bannana', 'clock', 'letter', 'jaguar', '1001', 'bob']
for word in words:
	res = is_palindrome(word)
	if res: print("{0} is a palindrome".format(word))
	else: print("{0} is not a palindrome".format(word))



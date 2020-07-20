import re
def is_palindrome(s):
	forward = ''.join(re.findall(r'[a-z]+',s.lower()))
	backward = forward[::-1]
	return forward == backward


print(is_palindrome("race car")) #True
print(is_palindrome("123321")) #True
print(is_palindrome("notplaidrome")) #False
print(is_palindrome("A Santa at NASA")) # True
print(is_palindrome("GO HANG A SALAM! I'M A LASAGNA HOG!")) #True

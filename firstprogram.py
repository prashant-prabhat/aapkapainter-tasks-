s1=input('Enter first string to check angram').strip()
s2=input('Enter second string to check angram').strip()
if sorted(s1)==sorted(s2):
	print('The given string is angram')
else:
	print('The given strings are not angram')
  

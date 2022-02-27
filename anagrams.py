s=[1,2,3,2,4,4]
for i in range(len(s)):
	if s.count(s[i])>1:
		print(s[i])
		break

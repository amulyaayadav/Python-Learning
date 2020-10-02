def hero(string):
	count=0
	temp=[]
	for i in string:
		if(i not in temp):
			count+=1
			temp.append(i)
	if count%2==0:
		print("CHAT WITH HER")
	else:
		print("IGNORE HIM")

hero('wjzmbr')

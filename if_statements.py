if 1 < 2: print("one liner code")
print("one liner if-else") if 2 > 1 else print("not")

#one line if else statement, with 3 conditions:
print("ternary operator") if 2 > 1 else print("not") if 1==2 else print("not") 

if 2 > 0 and 1 > 0:
	print("positive numbers")#both conditions are true

if 2 > 0 or -1 > 0:
	print("at least one condition is true")

x = 0
if 80 < x: 
	print("positve numba----")
	if 60 < x: 
		print("also positive----")
	else : 
		print("not positive-----")

def negORpos(neg,pos,zero):
	if neg > pos:
		print("lesser")
	elif neg == pos:
		print("equals")
	else: 
		print("greater")	
negORpos(-1,1,0)	



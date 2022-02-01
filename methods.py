xlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ylist = ["a","a","c","d","b","e","f","g","h","j","k"]
clear_this_list = ["this list shall be emty",0]

print("ylist length",len(ylist))

isinstance_method_num = 45j
print(isinstance(isinstance_method_num, complex))#true

sort_list = ylist.sort()
ylist.sort(reverse = True)

#---------------------------------------
def sort_closes_to(param):
	return abs(param - 50)

sortingnumber = [100, 50, 65, 82, 23]
sortingnumber.sort(key = sort_closes_to)#[50, 65, 23, 82, 100]
# sort the list based on how close the number is to 50:
#----------------------------------------

removesLastItemOrSpecified = xlist.pop(1)

removeSpecifiedOnly = xlist.remove(15)

del xlist[2] #delete specified index 

clear_this_list.clear();

insertAt_specifiedIndex = xlist.insert(-2,"inserted")

addValuetoEnd = xlist.append("added")

reverseList = xlist.reverse()

countSpecified_values = ylist.count("a")
print(countSpecified_values,": times")#2 : times

# range(start, stop, increment by)
ranger = range(0,13,2)
for i in ranger:
	print(i)

strList = ["ask","bout","me"]
comprehensionList = [i for i in strList if "a" in i] #['ask']

#copy method
copy_xlist = xlist.copy()
copy_ylist = list(ylist)
alternate_copy_method = copy_xlist[:] ;del alternate_copy_method[:7] #delete after 7th index


#join 2 lists
combining_lists = ylist.extend(xlist)
concat_list = copy_xlist + copy_ylist
ab = ["a","b"]
cd = ["c","d"]
for i in cd:
  ab.append(i)



print(sortingnumber,"<><><<<<<____________")
print(xlist)
print(ylist)
print(ab,"<------?%%% copy")
print(alternate_copy_method,"<<<--alternate method")
print(comprehensionList)

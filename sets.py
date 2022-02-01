#A set is a collection which is both unordered and unindexed.
#Set items are unordered, unchangeable, and do not allow duplicate values.
#duplicate values will be ignored

bookset = {"jeremiah","isaiah","zachariah"}
length = len(bookset)
types = type(bookset)

#note use double brackets
converter = set(("bob","sue","ezekiel"))
print(converter)

for i in bookset:
	print(i)

checkIF_value_inSet = "isaiah" in bookset # true

#Once a set is created, you cannot change its items, but you can add new items.
#add value
bookset.add("micah")

#join
bookset.update(converter)
#can also join with tuples, dictionaries, list etc
#both union and update will remove duplicates
a1 = {1,2,3}
a2 = {4,5,6}
a3 = a1.union(a2)
a4 = {4,2,6,99}

#returns only the duplicate
returnDup = a3.intersection_update(a4)#{2,4,6}
#return value present in both
presentInBoth = a2.intersection(a4)#{4,6}
#returns not present in both
NOTpresentInBoth = a4.symmetric_difference(a2)

#symmetric_difference_update() <---keeps not present in both/removes duplicates

bookset.remove("sue")
bookset.discard("bob")
removedItem = bookset.pop()#removes last item and returns it



print(removedItem)
print(bookset)
print(a4,"--4")
print(a3,"--3")
print(a2,"--2")
print(a1,"--1")
#2 4 6 99
#4 5 6
#2 5 99
#4 6
print(NOTpresentInBoth,"<<<<---Not in both")
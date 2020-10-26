multiLine_str_tripleQuotation = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(multiLine_str_tripleQuotation[0:6])
print(multiLine_str_tripleQuotation[-23:-1])
print("length is =", len(multiLine_str_tripleQuotation))
print("one line", "two line", sep="-----")  #one line-----two line

stripMethod = "   hello   "
print(stripMethod.strip())  #removes spaces

lowerMethod = "hELLo UnIvERse"
print(lowerMethod.lower())  #returns lower cases

upperMethod = "these are capital letters"
print(upperMethod.upper())

replaceMethod = "Replace me with yo"
print(replaceMethod.replace("me","yo"))

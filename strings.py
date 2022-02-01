
if __name__ == "__main__": 
    print ("Executed when invoked directly]]]]]]]]")
	
multiLine_str_tripleQuotation = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(multiLine_str_tripleQuotation[0:6])
print(multiLine_str_tripleQuotation[-23:-1])
print("length is =", len(multiLine_str_tripleQuotation))
print("one line", "two line", sep="-----")  #one line-----two line

stripMethod = "   hello   "
print(stripMethod.strip())#removes spaces

lowerMethod = "hELLo UnIvERse"
print(lowerMethod.lower())#returns lower cases

upperMethod = "these are capital letters"
print(upperMethod.upper())#returns capitals

replaceMethod = "Replace me with yo"
print(replaceMethod.replace("me","yo"))

splitMethod = "hello - universe"
print(splitMethod.split(","))
#method splits the string into subtstrings if it 
#finds instances of the separator

checkIfTxt = 'Check if the wapa is in text'
checkFunc = "wapa" in checkIfTxt
print(checkFunc, ": The word wapa is in")

checkIf_notIn_txt = "is the word poopy in this string"
checkIf_not_func = "poopy" not in checkIf_notIn_txt
print(checkIf_not_func,": The word poopy is not in")

hello = "hello "
world = "world"
print(hello+world)

mixedMethods = "   HelLoR   ZsS  "
print(mixedMethods.lower().strip().split())

arrow_str = "<-----"
arrow_str1 = "----->"
print(arrow_str+" + "+arrow_str1)

neckSize = 36
footSize = 86.3
unlimitedTimes = 99
format_method_txt = "Her neck size is {}, foot size is {},times i can do this is {}" 
#brackets are the placeholders
print(format_method_txt.format(neckSize,footSize,unlimitedTimes))

formatTXT_2 = "number three is {2}, two one {0} ,two is {1}"
print(formatTXT_2.format(neckSize,footSize,unlimitedTimes))

backlash_txt = "This is an \"escape\" character"
print(backlash_txt) #This is an "escape" character

single_quote = 'It\'s a single quote'
print(single_quote)

single_backlash = "this will insert one backlash \\" 
print(single_backlash)# this will insert one backlash \

new_line = "one \ntwo"
print(new_line)

count_meth ="count the word Jesus, Jesus, Jesus appears here"
print("amount:",count_meth.count("Jesus"))
#return a palindrome
def palindrome(txt):

  rightWord = list(txt)
  reverseWord = list(txt[::-1])
  
  if rightWord == reverseWord:
      return ("This is a palindrome")
  else:
      return ("It's not a palindrome")
    
print(palindrome("seyesd"))


def isPalindrome(s):
    return s == s[::-1]
		
# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
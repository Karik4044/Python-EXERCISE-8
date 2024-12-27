def isPalindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
print("The string is a palindrome" if isPalindrome(s) else "The string is not a palindrome")
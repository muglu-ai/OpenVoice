
def is_palindrome(s):
    s = s.replace(' ', '').lower()  # remove spaces and convert to lowercase
    return s == s[::-1]  # check if the string is equal to its reverse

# test the function
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False

def is_palindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True
if(is_palindrome("malayalam")):
    print("True")
else:
    print("False")
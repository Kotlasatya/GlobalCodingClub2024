def palindrome(string):
    new_string = string[::-1]
    if string==new_string:
        return True
    else:
        return False
string = input()
print(palindrome(string))

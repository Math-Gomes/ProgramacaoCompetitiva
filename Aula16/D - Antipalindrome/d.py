def is_palindrome(s):
    if len(s) > 0:
        return s == s[::-1]
    else:
        return False

def solve(s):
    if is_palindrome(s):
        return solve(s[:-1])
    else:
        return len(s)

if __name__ == '__main__':
    print(solve(input()))

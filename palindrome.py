import string

def palindrome(a):
    b = {letter: 0 for letter in string.ascii_uppercase}
    for i in range(0, len(a)):
         b[a[i]] += 1
    result = ""
    last_key = ""
    odd_result = False
    for i in b:
        if b[i]//2 != 0:
            result += i * (b[i]//2)
            last_key = i
    for i in b:
        if i >= last_key and b[i]%2 == 1:
            result += i
            odd_result = True
            break
    if odd_result:
        result += result[1::-1]
    else:
        result += result[::-1]

    return result

print (palindrome("AAAEDYZBB"))
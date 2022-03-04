#n = range(9)
"""for i in range(1, 10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,(i*j)))"""


from audioop import reverse


def is_number_palindrome(num):
    a =[]
    b = []
    for i in num:
        a.append(i)

    c = a
    a.reverse()
    b = a
    if c == b:
        return True
    else:
        print(a)

b = is_number_palindrome('101')
print(b)

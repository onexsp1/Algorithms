import datetime
from math import gcd, lcm, pi, sqrt, trunc
import  os.path
import sys
import files
from pathlib import Path
"""string = "Twinkle, twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky.\nTwinkle, twinkle, little star,\n        How I wonder what you are"
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
print(datetime.datetime.now())

r = float(input("Enter circle's Radius: "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))"""

"""name = input("First Name: ")
last_name = input("Last Name: ")
full_name = last_name +" "+name
print(full_name)"""

"""sequences = input("Numbers sequence:")
myList = sequences.split(',')
myTuple = tuple(myList)
print(myList)
print(myTuple)"""

#get file extension ex. abc.java get java
"""filename = input('Filename: ')
file_ext = filename.split('.')
print(file_ext[-1])"""

#get first and last color from list
"""color_list =  ["Red","Green","White" ,"Black"]
print('The first color is: {f} and the last color is {l}'.format(f=color_list[0], l=color_list[-1]))"""

#extract date from tuple
"""exam_date = (11, 12, 2014)
startdate = str(exam_date)
print("The examination will start from : "+datetime.date(startdate))"""

#computes the value of n+nn+nnn
"""n = int(input("Value of n: "))
print(n+(n*11)+(n*111))

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)"""

"""y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))"""

#substract dates
"""date1 = datetime.date(2014,7,2)
date2 = datetime.date(2014,7,11)
days = date2 - date1
print("{} Days".format(days.days))"""

# volume of a sphere 
"""r = int(input('Radius: '))
v = round((4/3) * pi * (pow(r,3)),2)
print("Volume is: {}".format(v))"""

#double absolute difference
"""def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

n = int(input("Number:"))
print(difference(n))
"""

#number between 100 and 1000 or 2000
"""n = int(input("Number:"))
if (1000 - n) <=100 or (2000 - n) <=100 :
    print("{} is within 100 and 1000 or 2000".format(n))
else:
    print("{} is NOT within 100 and 1000 or 2000".format(n))"""

#return value
"""resullt = 0
n = input('insert numbers separeted by comma:')
sum_list = n.split(',')
is_equals = True
for i in range(0, len(sum_list)):
    resullt += int(sum_list[i])

for i in range(0, len(sum_list)):
    if sum_list[0] != sum_list[i]:
        is_equals = False
        break

if is_equals == True:
    print(resullt*3)
else:
    print(resullt)"""

#number of copies
"""n_copies = int(input("Number of copies: "))
temp = 0
text = ".test"
while temp <= n_copies-1:
    print(text)
    temp += 1
for i in range(0,n_copies):
    print(text)

"""

#number odd or evenn
"""n=int(input("Insert the number:"))
if n%2==0:
    print("even")
else:
    print("odd")
    """

#count number of time of N
"""n = input('insert numbers separeted by comma:')
number_tofind = int(input("Insert number to be found: "))
sum_list = n.split(',')
count = 0
for i in range(0,len(sum_list)):
    if int(sum_list[i]) == number_tofind:
        count += 1
print("Number {} is {} times in the list".format(number_tofind, count))"""

"""def isVowel(v):
    vowels = ['a','e','i','o','u']
    is_vowel = False
    for i in range(0,len(vowels)):
        if vowels[i] == v:
            is_vowel = True
            break
    return is_vowel

v = input("Insert the letter: ")
print(isVowel(v))"""

#histogram
"""def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '@'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])"""

#print even numbers
"""numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for n in numbers:
    if n == 237:
        break
    if n%2==0:
        print(n)
        """

#difference color list
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
"""for c in color_list_1:
    if c not in color_list_2:
        print(c)
        """

# triangle area
"""def triangleArea(b,h):
    return (b*h)/2

b = (float(input("Base:")))
h = (float(input("Height:")))
print("Area of the triangle is: {}".format(triangleArea(b,h)))"""

#lcm and gcd
"""print(lcm(4,5))
print(gcd(4,5))"""

"""def getSum(a,b):
    if (a+b) in range(15,20):
        return 20
    else:
        return a+b

print(getSum(15,66))"""

"""def is_true(a,b):
    if a == b or a+b == 5 or a-b == 5:
        return True
    else:
        return False

print(is_true(7,2))"""

"""def getEcuation(x,y):
    return (x+y)*(x+y)

x=4
y=3
print("({}+{})^2 = {}".format(x,y,getEcuation(x,y)))"""

#calculate interest
"""def calculateInterest(a,i,y):
    return a*((1+(0.01*i)) ** y)

a = 10000
i = 3.5
y = 7
print(round(calculateInterest(a,i,y),2))
"""

# calculate distance
"""def getDistance(x1,y1,x2,y2):
    return sqrt(pow((x2 - x1),2) + pow((y2-y1),2))

print(getDistance(4,0,6,6))"""

"""f = "files/pythonfilee.txt"
print(os.path.exists(f.p))"""

#sum of the integer digists
d = input("Input integer number: ")
r = 0
for i in range(0, len(d)):
    r += int(d[i])

print(r)

#convert seconds to day, hour, minutes, seconds
"""time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))"""


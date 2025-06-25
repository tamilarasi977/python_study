

# 1) Write a function to check if two strings are anagrams of each other (contain the same characters in any order).
#use for loops
def are_anagrams(s1, s2,**h):
    a="list"
    b="silit"
    c="hello"
    sortStr1 = sorted(s1)
    sortStr2 = sorted(s2)
    return sortStr1 == sortStr2

# Example
print(are_anagrams("listen", "silent","ooo","iuiuiuiu"))  # True
print(are_anagrams("hello", "world"))    # False
# or
# s1=("listen")
# s2=("slient")
# if(sorted(s1)==sorted(s2)):
#       print("true")
# else:
#       print("false")
  



# 2) palindrome Using slicing method

def palindrome(str):

     if str == str[::-1]:
          print("isPalindrome",True)
     else:
          print("isNotPalindrome",False)   

     print(palindrome("madam")) #opt ===> isPalindrome True
     print(palindrome("hello world"))  #opt ===>isNotPalindrome False  
 



# 3)Find the max and min number from a list. Sample Input:numbers = [12, 45, 7, 89, 23] Sample Output:Max: 89, Min: 7
     

l=[12, 45, 7, 89, 23]
min_num = max_num = l[0]

for num in l:
     
     if num < min_num:   # the left operand is less than the right
          min_num = num
     if num > max_num:    #the left operand is greater than the right
          max_num = num

print("Minimum number:", min_num)
print("Maximum number:", max_num)   


# 4) Sort in Ascending and Descending Order

# Ascending Order

data = [34, 12, 5, 66, 29]
data.sort()
print(data)


#Descending Order
data = [34, 12, 5, 66, 29]
data.sort(reverse = True)
print(data)



# 5) Remove duplicates from the list We can use set() 

a = [1, 2, 2, 3, 4, 4, 5]
def removedup(a):
# Remove duplicates by converting to a set because set will not allow the duplicate:

     a=list(set(a))
     print(removedup(a))



# 6) Check Even or Odd if a number is even or odd.

x=17

# Check the remainder dividing x by 2 is 0

if x % 2 == 0:

  print("even")
else:
     print("odd") 

 
#Ex 2:
 
x=24

# Check the remainder dividing x by 2 is 0

if x % 2 == 0:

  print("even")
else:
     print("odd")   


# 7)  Reverse a String in Python 

text="python"[::-1]
print(text)

        


# 8)  Check if 13 is a prime number:

num = 13

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("prime")
else:
    print("not a prime")
# Lists:

mylist=["apple","banana","orange"]
print(mylist)

# length;
mylist=["apple","banana","orange"]
print(len(mylist))

#index;
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

# Returns banana to kiwi

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[1:5])

# Returns from kiwi to end

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[4:])

# Returns from orange  to melon end 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])



# Add the number `4` at the 6th index of the list `l`.  

l=[1,22,3,44,55,6,11,1200]
l.insert(6,4)
print(l)

#Remove the value `44` from the list `l`.  

l=[1,22,3,44,55,6,11,1200]
l.remove(44)
print(l)

# Append the number `88` to the end of the list `l`.  

l=[1,22,3,44,55,6,11,1200]
l.append(88)
print(l)

#Remove the value at the 2nd index of the list `l`.
 
l=[1,22,3,44,55,6,11,1200]
l.pop(2)
print(l)

# Merge the list `m = [1, 2, 3, 546]` into the list `l`.

l=[1,22,3,44,55,6,11,1200]
m = [1, 2, 3, 546]
l.extend(m)
print(l)

 




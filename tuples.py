# Change  the value in tuple:

x=("apples","banana","kiwi","abc")

#Tuples are unchangeable:

# Convert the tuple into a list to be able to change it:

y=list(x)

print(y)  #  Returns ("apples","banana","kiwi","abc")

y[2]="cherry" # Now replace the cherry index of 2 kiwi

x=tuple(y)

print(x)


# Add the value in tuple:

x=("apples","banana","kiwi","abc")

#Tuples are unchangeable so we cannot add the value:

# Convert the tuple into a list to be able to change it:

y=list(x)

print(y)

# Add the "orange" value;
#append is used to add the value in end of the list

y.append("orange")

print(y)



# Remove the value in tuple:

#Tuples are unchangeable so we cannot remove the value:

# Convert the tuple into a list to be able to change it:

x=("apple","banana","kiwi","abc")
y=list(x)
print(y)

y.remove("apple")
print(y)



 

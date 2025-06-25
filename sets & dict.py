# Sets:

# Add the items:

x={"apple","banana","chery"}
x.add("color")
print(x)


# Update the list and removed duplicates:

x={"apple","banana","chery"}
y={"hello", "world","banana"}

x.update(y)
print(x)


# remove random item:

x={"apple","banana","chery"}

y=x.pop()
print(y)


# Dictonaries:

# Add the items:

x={
    "name":"tamil",
    "age":24
}
x["number"]="97"
print(x)

# change the items:

x={
    "name":"tamil",
    "age":24
}
x["age"]=36
print(x)

# Return the keys:

x={
    "name":"tamil",
    "age":24
}
y=x.keys()
print(y)

# Return the Values:

x={
    "name":"tamil",
    "age":24
}
y=x.values()
print(y)








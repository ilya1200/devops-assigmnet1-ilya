name = "john"
name = 'john'

# Both expressions are equivalent
# In both cases, a string with the same content(john) will be stored in the variable

###########

# This code will raise a TypeError
# because a string can't be concatenated with an int using + operator
my_number = 5 + 5
print("result is:" + my_number)

# a solution will be casting the value stored in my_number into a string.
# Since two strings can be concatenated with + , this should work
# Good code version
my_number = 5 + 5
print("result is:" + str(my_number))

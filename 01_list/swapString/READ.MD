Sometimes, while working with data records we can have a problem in which we need to perform certain swap operation in which we need to change one element with other over entire string list.


# The str() function converts values to a string form so they can be combined with other strings
#   pi = 3.14
#   ##text = 'The value of pi is ' + pi      ## NO, does not work
#   text = 'The value of pi is '  + str(pi)  ## yes


# Python join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator. This function joins elements of a sequence and makes it a string.

# Example:

# str = '-'.join('hello')
# print(str)
# Output:
# h-e-l-l-o


# string.replace(oldvalue, newvalue, count)
# string.split(separator, maxsplit)

# using replace() + join() + split()
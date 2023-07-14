Given two numbers, write a Python code to find the Minimum of these two numbers. Examples:

Input: a = 2, b = 4
Output: 2

Input: a = -1, b = -4
Output: -4

<!-- min() -->
The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.

<!-- Sorted -->
The sorted() function returns a sorted list of the specified iterable object.

sorted(iterable, key=key, reverse=reverse)


<!-- Reduce -->
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

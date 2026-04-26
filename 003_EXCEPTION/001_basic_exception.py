
"""
Exception are situation in a running program where the next stage in undefined. This usually ends with non zero exit
For example our program wanted to open a file, but due to permission the OS returned error, we need to treat this
as a part of normal flow, rather than exiting the program

Let's treat exception as first class citizen and handle them like a man.
Also, exception is a kind of error which terminates a program (unless handled, we will see)
"""

# We want to write a program that tells if i am eligible for driving

age_str = input("What is your age? ")
age = int(age_str)
if age >= 18:
	print("Congrats, you are eligible for driving")
else:
	print("Sorry, you are not eligible for driving")

print("End of program natural floe") #This will not run if we encounter an exception

'''
This program runs okay, unless you accidentally enter non numeric value, which crashes the program
Because it doesn't know what to do when you enter non numeric value, which crashes the program
That's why we need to treat this as a part of normal flow, rather than exiting the program
We handle thy exception, we try running this on a try block, where if we get and exception,we will catch it and 
continue our normal flow
'''


age_str = input("What is your age? ")
try:
	age = int(age_str) # type some non-numeric value here
	if age >= 18:
		print("Congrats, you are eligible for driving")
	else:
		print("Sorry, you are not eligible for driving")
except ValueError as e:
	print(e)
print("End of program natural flow")
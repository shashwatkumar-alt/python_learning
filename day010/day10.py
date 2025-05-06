a = input("Enter a :")
print("You've typed :",a)

''' python input function is not intelligent enough to sense that the input is a number or alphabet or any kind of symbol.
So, it always inputs everything in string format'''

b = input("Enter the first number :")
c = input("Enter the second number :")
print(b+c)
print(int(b)+int(c))
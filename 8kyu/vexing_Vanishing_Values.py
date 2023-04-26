"""
Confusion, perplexity, a mild headache. These are just a sample of the things you have experienced in the last few minutes while trying to figure out what is going on in your code.

The task is very simple: accept a list of values, and another value n, then return a new list with every value multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].

While writing the function, you even added some debugging lines to make sure that you didn't mess anything up, and everything looked good! But for some reason when you run the function it always seems to return an empty list, even though you can clearly see, that the list should have the right values in it! Somehow, the values are simply disappearing! Is this a bug in the programming language itself...?
"""
lst = [1,2,3,4,5,6]
n = 5
def mul_by_n(lst, n):
    print("Inputs: ", lst, n) # Check our inputs
    result = (x * n for x in lst)
    #print("Result: ", list(result)) # Check our result
    #list is a generator, which makes iteration to occur only once, hence further use of list in the return failed returned an empty string.add()
    #To solve this challenge, I will either comment out the print statement so that the list iteration will occur only in the return line or I will print(result) without the list() function. Which makes iteration possible countless times.
    return list(result)

print(mul_by_n(lst, n))
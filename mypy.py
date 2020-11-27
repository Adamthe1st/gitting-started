print("Gitting-started")


#you get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0.
#answer:

def positive_sum(arr):  #this is the definition satatement of the function being created
    total = 0           #we start with a total of 0 to build the function
    for x in arr:       # we use "for" loop here
        if x > 0:
            total = total + num
    return total

#Create a function (or write a script in Shell) 
#that takes an integer as an argument 
#and returns "Even" for even numbers or "Odd" for odd numbers.
#Answer:
def even_or_odd(number): #this is our definition statement for the function
    if number % 2 == 0:   # the '%' is modulu that returns the reminder of a devision.
        #here, any number devided by 2 and has 0 reminder must be an even number (just remember this even if it doesnt make sense)
        return 'Even'
    else:
        return 'Odd'

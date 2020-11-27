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

print("Gitting-started")

=================================================================
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
==================================================
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
===============================================
#Write a function called repeat_str which repeats the given string exactly x times.
#example:
#repeatStr(6, "I") // "IIIIII"
#repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

#answer: the long way:
def repeat_str(repeat, string): #we start by creating a function statement
    substring = ' ' # creating a substring with empty string
    # we are going to "for loop" on the "repeat" argument in line 33
    # remember repeat is a number we want to repeat, thus we 
    #are going to use a "range" function:
    for x in range (repeat):
        substring = substring + string #this is the same as (substring += string)
    return substring

#the easy way:
def repeat_str(repeat, string):
    return repeat * string
===========================================
#Maximums and Minimums: 1.create a function that returns the max number out of list
#                       2.create a function that returns the min number out of list
#answer: 1.
def minimum(arr):
    return min(arr)
#2.
def maximum(arr):
    return max(arr)
================================
#next question:
def find_needle(haystack):
    for i, word in enumerate(haystack): #for 'index' of 'word' in enumerate (haystack):
        if word == "needle":
            return 'found the needle at position ' + str(i) #notice the space after the word 'position'
        #also notice 'i' has to be a string so we use 'str(i)' to avoid python error
==================================
#function to reverse a string passed into it.
def solution(string):
    return string [::-1]
#[::-1] is a built in function that reverses a list (hi mum) => (ih mum)
=================================================
#Create a function that returns the sum of the two lowest positive numbers given an array 
#No floats or non-positive integers will be passed.
#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#answer:
def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers) #sorted() is a built in function that sorts smallest to largest
    #now numbers in the variable 'sorted_numbers' are sorted
    #smallest 2 numbers are the 1st two numbers. thus:
    my_first_two_numbers = sorted_numbers[:2] #[:2] gives first two index in list
    return sum(my_first_two_numbers) #this adds up the two numbers index 0 and index 1
===================================================
#1. chop the string into numbers separated by comas using .split built in function 
#2. then turn string into integers 
#3. then sort smallest to largest
#4. we will extract smallest number at [0] and largest number at [-1]
def high_and_low(numbers_string):
    numbers_string_list = numbers_string.split(' ') #notice space between ' ' to signify we want to split on the actual spaces
    numbers = [] #creating an empty list
    #we will loop through 'numbers_string_list' and transform each string into an actual number and add them to the variable 'numbers' we created in the previous line
    for actual_num_string in numbers_string_list: #starting a 'for loop'
        n = int(actual_num_string) #int() is a built in function that turns a string into an integer
        numbers.append(n) #adding numbers as integers into our empty list 'numbers'
    sorted_numbers = sorted(numbers) #at end of for loop, we are creating a variable 'sorted_numbers' and using the built in func 'sorted()'   
     #now, we need to return a string with largest num first then smallet num
    high_low = str(sorted_numbers[-1]) + ' ' + str(sorted_numbers[0])
        #str() is a built in func to turn a number into a string
    return high_low
#this process is called string concatenation which is different from interpolation
===================================
#same as previous (just a little cleaner)
def high_and_low(numbers_string):
    numbers_string_list = numbers_string.split(' ')
    numbers = []
    for x in numbers_string_list:
        string_to_num = int(x) #transforming string list into integers
        numbers.append(string_to_num)
    sorted_numbers = sorted(numbers) #now we sort the numbers samllest - largest using 'sorted' function
    output_high_low = str(sorted_numbers[-1]) + ' ' + str(sorted_numbers[0])
    return output_high_low
===================================================================
#return the count of pairs that have consecutive numbers as follows:
#pairs([1,2,5,8,-4,-3,7,6,5]) = 3
#answer:
def pairs(array): #fisrt need to check if array pair count is odd or even
        if len(array) % 2 == 1: #remember, if the remider is 1, then we have odd pair count
            array = array[0:-1] #this excludes the last integer in the array so that we only have even sets of pairs
        pair_count = 0            
        for i in range(0, len(array), 2): #we are looping thro our array.and using range function starting at idex '0' up to 'whole length of array list' then adding a 3rd prameter in our range function which is 'skip' skiping idex of 2 (ie. count starting at idex 0, then 2,4,6 etc)
            first = array[i] #fisrt = 1st number in a pair set
            second = array[i+1] #second = 2nd number in a pair set
            if first + 1 == second or first -1 == second:
                pair_count = pair_count + 1
        return pair_count
========================================
#find challenge at: https://www.codewars.com/kata/rectangle-into-squares/python
def sort_sides(lng, wdth):#this function to identify lenghts of sides
    return sorted([lng, wdth]) #using sorted function, we will return small side fisrt then larger side 2nd

def sqInRect(lng, wdth):
    if lng == wdth:
        return None #this reules out squares since we are only interested in rectangles
    small, large = sort_sides(lng, wdth)
    print('small', small, 'large', large)
    squares = []
    while small > 0:
        squares.append(small)
        new_side = large - small
        small, large = sort_sides(new_side, small)
    return squares

"""
Simple functions to find different items in a list

file: listFunctions.py

author: Andrew Kotoski & Donovan Griego

date: September 13 2021

assignment: PreLab4
"""
Inlist = "type(list[int])"

def max(elements: Inlist):
    """returns the max element in the given list
    
    elements: the list to search
    """
    out = elements[0]
    for i in elements:
        if i > out:
            out = i
    return out

def min(elements: Inlist):
    """
    returns the minimum element in the given list
    
    elements: the list to search
    """
    out = elements[0]
    for i in elements:
        if i < out:
            out = i
    return out

def sum(elements: Inlist):
    """
    returns the sum of all the elements in the given list
    
    elements: the list to sum
    """
    out = 0
    for i in elements:
        out += i
    return out

def midpoint(elements: Inlist):
    """returns the element at the middle of the list
    
    elements: the list to search
    """
    return elements[(len(elements) // 2)]

def average(elements: Inlist):
    """"
    returns the average value of the elements in the given list
    
    elements: the list to average the elements of
    """
    return sum(elements) / len(elements)

def reverse(elements: Inlist):
    """returns the same list but reversed order
    
    elements: the list to reverse
    """
    elements.reverse()
    return elements

def linear_search(elements: Inlist, num: int):
    """returns whether or not the given value is in the given list
    
    elements: the list to search
    num: the value to search for
    """
    try:
        out = elements.index(num)
        return True
    except ValueError:
        return False


def main():
    lst = [10, 4, 32, 5, 65, 43, 100, 13, 15, 27, 54]
    print("max: ", max(lst))
    print("min: ", min(lst))
    print("sum: ", sum(lst))
    print("midpoint: ", midpoint(lst))
    print("average: ", average(lst))
    print("reverse: ", reverse(lst))
    print("linear_search for 10000: ", linear_search(lst, 10000))
    print("linear_search for 5: ", linear_search(lst, 5))


if __name__ == "__main__":
    main()
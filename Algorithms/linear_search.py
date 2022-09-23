from unittest import result


def linear_Search(list, target):
    """
        Returns the index position of the target in the list, else returns None.
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index != None:
        print("Target found at index: ", index)
    else:
        print("Target not found at index")
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_Search(numbers, 9)
verify(result)
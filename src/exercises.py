def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    input_list.reverse()
    return input_list

input_list = [5,8,2,1,3,4]
print(reverse_list(input_list))
    

def count_digits(number):
    """
    Return count of digits
    """
    number = str(number)
    return len(number)

number = 1235678
print(count_digits(number))
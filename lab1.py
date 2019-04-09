
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:  #Error if list is None
        raise ValueError
    if len(int_list) == 0: #Checks if it is 0 length
        return None
    max = int_list[0] #keep track of greatest number
    for i in range(1, len(int_list), 1): #iterate
       if int_list[i] > max: #replace max if it is smaller than another number
          max = int_list[i]
    return max


def reverse_rec(int_list):   # must use recursion
    if int_list is None: #Error if list is none
        raise ValueError
    elif len(int_list) == 0: #Base case if len is 0
        return []
    else:
        last = int_list[len(int_list) - 1] #removes the last and adds it to the front + recall the method
        int_list.pop(len(int_list) - 1)
        return [last] + reverse_rec(int_list)


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None: #Error if list is none
        raise ValueError
    elif low < 0 or high >= len(int_list): #Error if low or high are not compatible
        raise IndexError
    elif (high == low and int_list[low] != target) or len(int_list) == 0 or low > high or high < low: #Base case if len of sublist is 0 and target not found
        return None
    elif int_list[(high + low) // 2] == target: #Return if the last number is the target
        return (high + low) // 2
    elif target < int_list[(high + low) // 2]:
        return bin_search(target, low, ((high + low) // 2) - 1, int_list)
    else:
        return bin_search(target, ((high + low) // 2) + 1, high, int_list)

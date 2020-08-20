'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            current = i
            prev = i + 1
            if arr[current] == 0:
                if arr[current] == arr[prev]:
                    swapped == False
                else:
                    print(arr)
                    arr[current], arr[prev] = arr[prev], arr[current]
                    swapped = True
    return arr
    # # Your code here
    # for i in arr:
    #     temp = None
    #     if i == 0:
    #         temp = 0
    #         arr.remove(i)
    #         arr.append(temp)
    # return arr
    # # pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
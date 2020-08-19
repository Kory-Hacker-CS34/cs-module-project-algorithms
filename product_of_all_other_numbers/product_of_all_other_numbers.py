'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    #base value which numbers shall loop through
    base = 1

    #array in which we shall store the multiplied numers
    answerArr = []
    for i in range(len(arr)):
        for y in arr:
            #checking to see that we don't multiply the number we're already looking at
            if y != arr[i]:
                base *= y
        answerArr.append(base)
        #resetting the base value for the next loop
        base = 1
    return answerArr



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

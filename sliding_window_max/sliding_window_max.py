'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    from collections import deque
    current = 0
    # print(nums)
    # print(nums[current])
    start = 0
    end = k
    window = []
    answerArr = []

    # print(window)

    for i in nums:
        window = nums[start:end]
        answerArr.append(max(window))
        print(window)
        start += 1
        end += 1
        if len(window) < k:
            answerArr.pop(-1)
            return answerArr
    # return answerArr
        
    # pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

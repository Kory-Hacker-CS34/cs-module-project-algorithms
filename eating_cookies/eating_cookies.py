'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    count = 0

    if n == 0:
        return count
    while n > 0:
        if (n - 1) > 0:
            count += 1
        
    
    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

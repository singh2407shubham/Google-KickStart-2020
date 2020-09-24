def lengthOflongestArray(array, array_len):
    
    longest = 0
    stack = []
    
    if array_len < 2: return
    
    for Idx in range(1, array_len):
        diff = array[Idx] - array[Idx-1]
        if not stack:
            stack.append(diff)
            currLongest = 2
            
        else:
            if diff == stack[-1]:
                currLongest += 1
            else:
                stack.pop()
                currLongest = 2
                stack.append(diff)
                
        longest = max(longest, currLongest)
        
    return longest

    
t = int(input())
for i in range(1, t+1):
    length = int(input())
    test_array = [int(item) for item in input().split()]
    ans = lengthOflongestArray(test_array, length)
    print("Case #{}: {}". format(i, ans))

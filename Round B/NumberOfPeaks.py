def numOfPeaks(checkpointArray, N):
    
    count = 0
    for idx in range(1, N-1):
        if checkpointArray[idx-1] < checkpointArray[idx] > checkpointArray[idx+1]:
            count += 1
    return count
    
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    checkpointArray = [int(item) for item in input().split()]
    ans = numOfPeaks(checkpointArray, N)
    print("Case #{}: {}". format(i, ans))
'''
houses = h1, h2 ...... hn
cost(hi) = Ai
budget = B
'''

def maxNumOfHouses(N, B, costArray):
    
    count = 0
    budget = B
    costArray.sort()
    for cost in costArray:
        if cost <= budget:
            budget = budget - cost
            count += 1
        if budget == 0:
            break
    return count

t = int(input())
for i in range(1, t+1):
    N, B = [int(s) for s in input().split(" ")]
    costArray = [int(item) for item in input().split()]
    ans = maxNumOfHouses(N, B, costArray)
    print("Case #{}: {}". format(i, ans))
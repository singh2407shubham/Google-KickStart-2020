def latestDay(numOfRoutes, days, busRoutes):
    
    if days == 1:
        return 1
    day = days    
    for idx in range(N-1, -1, -1):
        day = day - (day % busRoutes[idx])
    return day

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    N, D = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    routes = [int(item) for item in input().split()]
    ans = latestDay(N, D, routes)
    print("Case #{}: {}".format(i, ans))
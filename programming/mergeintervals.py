intervals=[[1,3],[2,6],[8,10],[9,12]]
intervals.sort()
merged=[]
for interval in intervals:
    if len(merged)==0:
        merged.append(interval)
    else:
        last=merged[-1]
        if interval[0]<=last[-1]:
            if interval[1]>last[-1]:
                last[-1]=interval[1]
        else:
            merged.append(interval)
print(merged)
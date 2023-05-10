import heapq

res = 0
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(n):
    arr2[i] += arr1[i]

arr = []
for i in range(n):
    arr.append((arr1[i], arr2[i]))
arr.sort()

heap = []
heapq.heapify(heap)

for start, end in arr:
    
    while len(heap) > 0 and heapq.nlargest(1, heap)[0] >= -start:
        heapq.heappop(heap)
    
    heapq.heappush(heap, -end)
    res = max(res, len(heap))
    
print(res)
    

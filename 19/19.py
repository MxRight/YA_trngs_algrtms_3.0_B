def insert(heap, n: int):
    heap.append(n)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[(pos - 1) // 2], heap[pos] = heap[pos], heap[(pos - 1) // 2]
        pos = (pos - 1) // 2

def extract(heap):
    res = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos * 2 + 1 < len(heap) - 1:
        max_indx = pos * 2 + 1
        if heap[pos* 2 + 2] > heap[max_indx]:
            max_indx = pos * 2 + 2
        if heap[pos] < heap[max_indx]:
            heap[pos], heap[max_indx] = heap[max_indx], heap[pos]
            pos = max_indx
        else:
            break
    heap.pop()
    return res

heap = []
n = int(input())
for i in range(n):
    data = input()
    if data[0] == '0':
        insert(heap, int(data.split()[1]))
    else:
        print(extract(heap))

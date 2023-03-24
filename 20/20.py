n = int(input())
lst = list(map(int, input().split()))


def make_heap(heap, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and heap[i] < heap[l]:
        largest = l
    if r < n and heap[largest] < heap[r]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        make_heap(heap, n, largest)


def heap_sorter(heap):
    n = len(heap)
    for i in range(n, -1, -1):
        make_heap(heap, n, i)
    for i in range(n - 1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        make_heap(heap, i, 0)

heap_sorter(lst)
print(*lst)

array = [63, 37, 27, 83, 48, 28, 84, 95]

def bubble_sort(array):
    for _ in range(len(array)):
        for item in range(len(array)-1):
            if array[item] > array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]

def revbubble_sort(array):
    for _ in range(len(array)):
        for item in range(len(array)-1):
            if array[item+1] > array[item]:
                array[item+1], array[item] = array[item], array[item+1] 

bubble_sort(array)
print(array)

revbubble_sort(array)
print(array)
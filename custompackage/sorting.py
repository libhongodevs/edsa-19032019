def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    for x in range(len(items)-1,0,-1):
        for i in range(x):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items)>1:
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k]=left[i]
                i=i+1
            else:
                items[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            items[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            items[k]=right[j]
            j=j+1
            k=k+1
    
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
# sorting functions
def bubble_sort(items):


    '''Return array of items, sorted in ascending order'''
    length = len(items) - 1
    sorted = False

    while not sorted: # checks if the items are sorted
        sorted = True
        for i in range(length):
            if items[i] > items[i+1]:
                sorted = False
                items[i], items[i+1] = items[i+1], items[i]
    return items # returns items

#-----------------------------------------------------------------------------------
def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
                k= k+1

        while i < len(lefthalf): # check left half side of the items

            items[k]=lefthalf[i]
            i= i+1
            k= k+1

        while j < len(righthalf): # check right half side of the items

            items[k] = righthalf[j]
            j=j+1
            k=k+1
    return items # returns the items

#-----------------------------------------------------------------------------------
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    q_sorted = [] # initialising an empty q_sorted list
    q_sorted = sorted(items) # sortingthe items
    return q_sorted # returns the items



def bubblesort(array):
    swap = True
    n = len(array)
    
    while swap:
        swap = False

        for i in range(n-1):
            if array[i] >array[i+1]:
                temp = array [i]
                array[i] = array[i+1]
                array[i+1] = temp
                swap = True
    return array   
nums = [12, 5, -1, 6, 9, 10]
print(bubblesort(nums))         
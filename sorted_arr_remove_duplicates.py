
def remove_duplicates(arr):
    for index, int in enumerate(arr):
        if index != 0:
            if int == arr[index-1]:
                arr.remove(int)
    return arr

arr = [0,1,2,3,3,4,5,6,6,7,8,8,9]
print(remove_duplicates(arr))

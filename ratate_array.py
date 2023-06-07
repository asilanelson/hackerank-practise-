def rotate_array(d,n):
    #n = len(array)
    d= d%n
    array = [1,2,3,4,5,6,7]
    #n = len(array)
    new_array = array[d:] + array[:d]
    return new_array
print(rotate_array(8,7))

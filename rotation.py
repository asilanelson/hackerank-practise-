#A left rotation operation on an array of size  shifts each of the
# array's elements  unit to the left. Given an integer, ,
# rotate the array that many steps left and return the result

#d =2
# arr = [1,2,3,4,5]
#after 2 roatations = 
#arr1 = [3,4,5,2,1]
def rotateLeft(d, arr):
    n = len(arr)
    rotatedArray = [0] * n
    effectiveRotations = d % n
    while True:

        for i in range(n):
            rotatedArray[i] = arr[(i + effectiveRotations) % n]

        return rotatedArray

def isUnique(str):
    arr = [False] * 128 #creating an array that contains 128 false values which will be compared with the string to be flipped
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        arr[index] = True
    return True
    
def Gameoflife(arr):
    result = 'Dies!'

    # check size array
    if not isinstance(arr,list) or len(arr)!=3 or len(arr[0])!=3 or len(arr[1])!=3 or len(arr[2])!=3:
        return 'Error!'

    # center char
    c = arr[1][1]
    l = checkAround(c,arr)-1
    if (c =='L' and (l == 2 or l == 3)) or (c == 'D' and (l == 3)):
        result = 'Becomes alive!'
    return result

def checkAround(k,arr):
    l = 0
    for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if arr[i][j] == k:
                    l = l + 1
    return l

if __name__ == "__main__":
    arr = []
    for i in range(0,3):
        a = []
        for j in range(0,3):
            a.append(input("arr[%s][%s] = Enter L or D : " % (i,j)))
        arr.append(a)
    print("Gameoflife(%s) : %s" % (arr,Gameoflife(arr)))
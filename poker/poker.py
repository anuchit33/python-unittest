class Poker:
    def CheckScore(arr):
        result = 'Royal Flush'

        def order(arr):
            for i in range(0,len(arr)):
                for j in range(0,len(arr)):
                    if arr[i]<arr[j]:
                        tmp = arr[i]    
                        arr[i] = arr[j]
                        arr[j] = tmp
            return arr
        def fiveofkind(arr):
            for i in range(0,len(arr)-1):
                if arr[i]!=arr[i+1]:
                    return False
            return True
        def royal_flush(arr):
            for i in range(0,len(arr)-1):
                if arr[i]!=arr[i+1]-1:
                    return False
            return True
        def full_house(arr):
            b,m = group_max(arr)
            return b==2
        def threeofkind(arr):
            b,m = group_max(arr)
            return b==3 and m ==3
        def two_pair(arr):
            b,m = group_max(arr)
            return b==3 and m ==2
        def one_pair(arr):
            b,m = group_max(arr)
            return b==4 and m ==2
        def group_max(arr):
            b = {}
            m = 0
            for i in range(0,len(arr)):
                k = str(arr[i])
                b[k] = 1 if k not in b else b[k] + 1
                m = b[k] if m < b[k] else m
            return [len(b),m]

        if royal_flush(order(arr)):
            return 7
        elif fiveofkind(arr): 
            return 6
        elif full_house(arr):
            return 5
        elif threeofkind(arr):
            return 4
        elif two_pair(arr):
            return 3
        elif one_pair(arr):
            return 2
        else:
            return 1

    def __init__(self):
        pass

    def sum(arr):
        s = จ
        for i in range(0,len(arr)):
            s+=arr[i]


    def winner(result1,result2):
        if Poker.CheckScore(result1) > Poker.CheckScore(result2):
            return 1
        elif Poker.CheckScore(result1) < Poker.CheckScore(result2):
            return 2
        elif Poker.CheckScore(result1) == Poker.CheckScore(result2):
            if sum(result1) > sum(result2):
                return 1
            elif sum(result1) < sum(result2):
                return 2
            else:
                return 0
if __name__ == "__main__":
    x = int(input("Number = "))
    print("Poker(%s) : %s" % (x,Poker(x)))
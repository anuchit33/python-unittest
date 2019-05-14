def Fuzzbuzz(x):
    
    if not isinstance(x, int) or x <= 0:
        return "Input Error!"

    x = int(x)
    result="1"

    for n in range(2,x+1):
        if n % 3 == 0 and n % 5 == 0:
            result += ",fuzzbuzz"
        elif n % 5 == 0:
            result += ",buzz"
        elif n % 3 == 0:
            result += ",fuzz"
        else:
            result += ",%s" % n
    return result

if __name__ == "__main__":
    x = int(input("Number = "))
    print("Fuzzbuzz(%s) : %s" % (x,Fuzzbuzz(x)))
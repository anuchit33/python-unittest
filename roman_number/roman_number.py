import math
c = [['M',1000],
    ['D',500],
    ['C',100],
    ['L',50],
    ['X',10],
    ['V',5],
    ['I',1],
]

def RomanNumber(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Input Error!"

    def split_unit(number):
        s = str(number)
        n = s[0]
        for i in range(1,len(s)):
            n += '0'
        return int(n)

    global c
    result = ''
    for i in range(0,len(c)):
        n = c[i][1]
        s = c[i][0]
        if number <1:
            break
        
        if int(number / n) > 0 : 
            # added
            if int(number / n) <= 3 and int(number / n) >0:
                for i in range(0,int(number / n)):
                    result += s
                    number = number - n
        if number > 0:
            for j in range(i,len(c)):
                n2 = c[j][1]
                s2 = c[j][0]
                # subtracted
                if split_unit(number) != n2 and (split_unit(number)) == n-n2 :
                    result +=  s2 + s
                    number = number - (n - n2)
                    break
                    
    return result

if __name__ == "__main__":
    x = int(input("Number = "))
    print("RomanNumber(%s) : %s" % (x,RomanNumber(x)))
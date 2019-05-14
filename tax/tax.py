tax_rate = [
        [0,150000], [0.05,300000], 
        [0.1,500000], [0.15,750000], 
        [0.2,1000000], [0.25,2000000],
        [0.3,5000000],[0.35,9999999999.99]]

def Tax(net):
    global tax_rate
    if (type(net) is not float and type(net) is not int ) or net < 0:
        return "Input Error!"
    
    tax = float(0)
    net =  float(net)

    for i in range(1,len(tax_rate)):
        rate = tax_rate[i][0]
        _max = tax_rate[i][1]
        _min = tax_rate[i-1][1]
        _d = net-_min
        if _d > 0:
            if _d < _max-_min :
                tax += (rate * _d)
            else:
                tax += (rate * (_min))
    return tax

if __name__ == "__main__":
    net = float(input("Net = "))
    print("Tax(%s) : %s" % (net,Tax(net)))
def Tax(net):
    
    if (type(net) is not float and type(net) is not int ) or net < 0:
        return "Input Error!"
    
    tax_rate = [0, 0.05, 0.1, 0.15, 0.2, 0.25,0.3,0.35]
    arr_max = [150000, 300000 , 500000,750000,1000000,2000000,5000000,9999999999.99]
    
    tax = float(0)
    net =  float(net)

    for i in range(1,len(tax_rate)):
        rate = tax_rate[i]
        _max = arr_max[i]
        _min = arr_max[i-1]
        _d = net-_min
        if _d > 0:
            if _d < _max-_min :
                #print("2 %s x %s , %s" % (rate,_d,_d))
                tax += (rate * _d)
            else:
                #print("3 %s x %s " % (rate,_min))
                tax += (rate * (_min))
    return tax

# tax rate 5%
def taxRate(r,net):
    
    return net * r

if __name__ == "__main__":
    net = float(input("Net = "))
    print("Tax(%s) : %s" % (net,Tax(net)))
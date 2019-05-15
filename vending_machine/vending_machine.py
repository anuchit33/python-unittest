
import math

def VendingMachine(one,five,ten,product):
    _product = [13,15,17]

    total_receive = one+(five*5)+(ten*10)
    p = _product[product-1] if product < len(_product) else -1
    change = total_receive - p
    
    # status
    status = 1 if change < 0 or p < 0 else 0
    
    if status == 0:
        # change coin ten
        if change / 10 >= 1 :
            ten = math.ceil(change/10)
            change = change - (ten*10)
        else:
            ten = 0
        # change coin five
        if change / 5 >= 1 :
            five = math.ceil(change/5)
            change = change - (five*5)
        else:
            five = 0
        # change coin one
        one = change

    return {
        'one': one,
        'five': five,
        'ten': ten,
        'status': status
    }

if __name__ == "__main__":
    one = int(input("Enter coin one = "))
    five = int(input("Enter coin five = "))
    ten = int(input("Enter coin ten = "))
    product = int(input("Enter product [1,2,3] = "))
    print("VendingMachine : %s" % (VendingMachine(one,five,ten,product)))
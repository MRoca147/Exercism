import math

def roman(number):
    unit=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ten=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundred=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousand=["", "M", "MM", "MMM"]
    
    u= number % 10
    d=int(math.floor(number/10))%10
    c=int(math.floor(number/100))%10
    m=int(math.floor(number/1000))
    if(number>=1000): 
        return thousand[m]+hundred[c]+ten[d]+unit[u]
    if(number>=100): 
        return hundred[c]+ten[d]+unit[u]
    else:
        if(number >= 10):
            return ten[d]+unit[u]
        else:
            return unit[number]
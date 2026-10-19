import sys
from decimal import Decimal
def calculate(cost,price,quantity):
 c=Decimal(str(cost));p=Decimal(str(price));q=int(quantity)
 if not c.is_finite() or not p.is_finite() or c<0 or p<0 or q<=0:raise ValueError("Invalid input")
 revenue=p*q;profit=(p-c)*q
 return revenue,profit,(profit/revenue*100 if revenue else Decimal(0))
if __name__=="__main__":
 revenue,profit,margin=calculate(*sys.argv[1:4])
 print(f"Revenue TZS {revenue:,.2f}\nGross profit TZS {profit:,.2f}\nGross margin {margin:.2f}%")

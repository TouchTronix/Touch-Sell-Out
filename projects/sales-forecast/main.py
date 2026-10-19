import csv,sys
from datetime import date,timedelta
from decimal import Decimal
from collections import defaultdict
def forecast(path,window=7):
 totals=defaultdict(lambda:Decimal(0))
 with open(path,newline="",encoding="utf-8") as f:
  for r in csv.DictReader(f):
   d=date.fromisoformat(r["date"]);v=Decimal(r["revenue"])
   if not v.is_finite() or v<0:raise ValueError("Invalid revenue")
   totals[d]+=v
 if not totals:raise ValueError("Empty data")
 end=max(totals)
 average=sum((totals[end-timedelta(days=i)] for i in range(window)),Decimal(0))/window
 for i in range(1,8):print(f"{end+timedelta(days=i)}: estimated TZS {average:,.2f}")
if __name__=="__main__":forecast(sys.argv[1])

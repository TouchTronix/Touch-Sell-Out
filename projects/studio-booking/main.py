import csv,sys
from datetime import datetime,timedelta
from pathlib import Path
FIELDS=["alias","start","minutes","service"]
def book(path,alias,start,minutes,service):
 p=Path(path); a=datetime.fromisoformat(start); n=int(minutes)
 if n<=0:raise ValueError("Duration must be positive")
 if p.exists():
  with p.open(newline="",encoding="utf-8") as f:
   for r in csv.DictReader(f):
    b=datetime.fromisoformat(r["start"])
    if a<b+timedelta(minutes=int(r["minutes"])) and b<a+timedelta(minutes=n):
     raise ValueError("Booking conflict")
 with p.open("a",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS)
  if p.stat().st_size==0:w.writeheader()
  w.writerow(dict(alias=alias,start=start,minutes=n,service=service))
if __name__=="__main__":book(*sys.argv[1:6]);print("Booking saved")

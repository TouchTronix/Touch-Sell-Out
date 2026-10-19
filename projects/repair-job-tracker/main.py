import csv,sys
from pathlib import Path
FIELDS=["job_id","device","issue","status"]
def add(path,job_id,device,issue):
 p=Path(path)
 if p.exists():
  with p.open(newline="",encoding="utf-8") as f:
   if any(r["job_id"]==job_id for r in csv.DictReader(f)): raise ValueError("Duplicate job ID")
 with p.open("a",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS)
  if p.stat().st_size==0:w.writeheader()
  w.writerow(dict(job_id=job_id,device=device,issue=issue,status="received"))
def list_jobs(path):
 with open(path,newline="",encoding="utf-8") as f:
  for r in csv.DictReader(f):print(r)
if __name__=="__main__":
 if sys.argv[1]=="add":add(*sys.argv[2:6])
 elif sys.argv[1]=="list":list_jobs(sys.argv[2])
 else:raise SystemExit("Usage: main.py add file.csv ID DEVICE ISSUE | list file.csv")

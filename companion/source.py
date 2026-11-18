"""Estimate recording runway from growth in a selected folder on its own volume."""
import shutil,subprocess,time
from pathlib import Path
from serve import page
INTERVAL=5
def measurements(o):
    folder=Path(o["folder"]).expanduser()
    if not folder.is_dir():raise ValueError("Choose an existing recording directory")
    command=["du","-sk",str(folder)]
    used=int(subprocess.check_output(command,text=True,timeout=15).split()[0])*1024
    return used,shutil.disk_usage(folder).free
def estimate(used,free,now,m):
    history=m.setdefault("samples",[])
    if history and used<history[-1][1]:history.clear()
    history.append((now,used))
    while len(history)>2 and now-history[0][0]>120:history.pop(0)
    delta=now-history[0][0];rate=(used-history[0][1])/delta if delta>=5 else 0
    minutes=free/rate/60 if rate>0 else None
    return dict(state="Recording volume",key=str(bool(rate)),pages=[
        page("DISK RUNWAY","--" if minutes is None else f"{minutes:.0f}min","Waiting for growth" if not rate else f"Growth {rate*60/1e6:.1f} MB/min",f"Free {free/1e9:.1f} GB"),
        page("FOLDER SIZE",f"{used/1e6:.1f}MB","Rolling 2-minute window","Uses allocated disk blocks")])
def snapshot(o,m):
    used,free=measurements(o);return estimate(used,free,time.monotonic(),m)

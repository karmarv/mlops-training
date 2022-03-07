import time
import sys
from tqdm import tqdm

def sleep_for_a_sec():
    time.sleep(1)

def progress_sleep():
    with tqdm(total=10, file=sys.stdout) as pbar:
        for i in range(10):
            sleep_for_a_sec()
            # Manually update the progress bar, useful for streams such as reading files.
            pbar.update(1) # Updates in increments of 1 stops at 100

def operate(x,y, type="product"):
    if type == "product":
        return int(x*y)
    elif type == "sum":
        return int(x+y)
    else:
        return None
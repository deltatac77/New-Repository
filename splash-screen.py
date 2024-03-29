import time, sys
#CREDIT - STACKEXCHANGE USER JAROSLAV JERRYNO NOVOTNY
def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += "\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

# Test
for i in range(100):
    time.sleep(0.01)
    update_progress("[INFO] Compiling build...", i/100.0)
update_progress("[INFO] Compiling build...", 1)

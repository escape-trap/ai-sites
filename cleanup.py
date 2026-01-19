import os, shutil, time

BASE = "sites"
MAX = 30

dirs = sorted(os.listdir(BASE))
for d in dirs[:-MAX]:
    shutil.rmtree(os.path.join(BASE,d))
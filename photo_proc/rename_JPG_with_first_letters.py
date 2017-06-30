import os


for fname in os.listdir('.'):
    if fname.endswith('_CaseConflict.JPG'):
        os.rename(fname, fname[:8]+'.JPG')
